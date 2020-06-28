import re
import requests
import os
import urllib.request
import ssl

from urllib.parse import urlsplit
from os.path import basename

ssl._create_default_https_context=ssl._create_unverified_context

headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate'
}

failed_image_list=[]

def mkdir(path):
    if not os.path.exists(path):
        print('新建文件夹：',path)
        os.makedirs(path)
        return True
    else:
        print(u"图片存放于：",os.getcwd()+os.sep+path)
        return False

def download_pic2(img_lists,answer_list,dir_name):
    print("一共有{num}张照片".format(num=len(img_lists)))

    index=1
    for i in range(len(img_lists)):
        image_url=img_lists[i]
        answer_id=answer_list[i]
        file_name=dir_name+os.sep+answer_id+\
            '_'+basename(urlsplit(image_url)[2])
        if os.path.exists(file_name):
            print("文件{file_name}已存在。".format(file_name=file_name))
            index +=1
            continue
        
        retry_time=3
        auto_download(image_url,file_name,retry_time)
        print("下载{pic_name}完成！({index}/{sum})".format(pic_name=image_url,index=index,sum=len(img_lists)))

        index +=1
    
    if len(failed_image_list):
        print("以下文件下载失败：")
        for failed_image_url in failed_image_list:
            print(failed_image_url)
    
    print('\n图片已保存至',dir_name+'\\')
    os.system("pause")
    
def auto_download(image_url,file_name,retry_time):
    try:
        if retry_time<=0:
            print("下载失败，请检查{image_url}链接是否正确（必要是可以手动下载）".format(image_url=image_url))
            failed_image_list.append(image_url)
            return
        
        urllib.request.urlretrieve(image_url,file_name)
    except urllib.request.ContentTooShortError:
        print("文件下载不完整，尝试重新下载，剩余尝试次数{retry_time}".format(retry_time=retry_time))
        retry_time-=1
        auto_download(image_url,file_name,retry_time)

    except urllib.request.URLError as e:
        print("网络连接出错，尝试重新下载，剩余尝试次数{retry_time}".format(retry_time=retry_time))
        retry_time-=1
        auto_download(image_url,file_name,retry_time)

def download_pic(img_lists,dir_name):
    print("一共有{num}张照片".format(num=len(img_lists)))
    for image_url in img_lists:
        response=requests.get(image_url,stream=True)
        if response.status_code==200:
            image=response.content
        else:
            continue

        file_name=dir_name+os.sep+basename(urlsplit(image_url)[2])

        try:
            with open(file_name,"wb") as picture:
                picture.write(image)
        
        except IOError:
            print("IO Error\n")
            continue
        finally:
            picture.close()
        
        print("下载{pic_name}完成！".format(pic_name=file_name))

def get_image_url(qid,headers,path):
    tmp_url="https://www.zhihu.com/node/QuestionAnswerListV2"
    size=10
    offset=0
    image_urls=[]
    answer_ids=[]
    session=requests.Session()
    while True:
        postdata={'method':'next',
                'params':'{{"url_token":{question_id},"pagesize":{pagesize},"offset":{offset}}}'.format(question_id=qid,pagesize=size,offset=offset)}
        page=session.post(tmp_url,headers=headers,data=postdata)
        ret=eval(page.text)
        answers=ret['msg']
        print(u"答案数：",len(answers))

        offset +=size

        if not answers:
            print("图片URL获取完毕，页数：",(offset-size)/size)
            return image_urls,answer_ids
        
        imgreg = re.compile('data-original="(.*?)"', re.S)

        answerreg = re.compile(
            'data-entry-url="\\\\/question\\\\/{question_id}\\\\/answer\\\\/(.*?)"'.format(question_id=qid), re.S)

        for answer in answers:
            tmp_list=[]
            url_items=re.findall(imgreg,answer)
            answer_id=re.findall(answerreg,answer)[0]
            for item in url_items:
                image_url=item.replace("\\","")
                tmp_list.append(image_url)

            tmp_list=list(set(tmp_list))

            for item in tmp_list:
                if item.endswith('r.jpg'):
                    print(item)
                    write_image_url_to_file(path,[item,answer_id])
                    image_urls.append(item)
                    answer_ids.append(answer_id)
        print('offset:',offset,',','num:',len(image_urls))

def write_image_url_to_file(file_name,image_url):
    file_full_name=file_name+'.txt'
    f=open(file_full_name,'a')
    f.write(image_url[0]+'\t'+image_url[1]+'\n')
    f.close()

def read_image_url_from_file(file_name):

    file_full_name=file_name+'.txt'

    image_url_list=[]
    answer_id_list=[]

    if not os.path.exists(file_full_name):
        return image_url_list,answer_id_list
    with open(file_full_name,'r') as f:
        for line in f:
            line=line.replace("\n","")
            line=line.split("\t")
            image_url_list.append(line[0])
            answer_id_list.append(line[1])
    print("从文件中读取下载链接完毕，总共有{num}个文件".format(num=len(image_url_list)))
    return image_url_list,answer_id_list

def main_download():
    title=input('title(命名用):\n')
    question_id=input(
        'question_id(知乎问题网址 https://www.zhihu.com/question/********/answer/######## 中的 ********) : \n)')
    
    title = '拥有一副令人羡慕的好身材是怎样的体验？'
    question_id = 297715922
    path=os.path.dirname(os.path.abspath(__file__))+\
        '\\'+str(question_id)+'_'+title
    mkdir(path)

    img_list,answer_list=read_image_url_from_file(path)
    if not len(img_list):
        img_list,answer_list=get_image_url(question_id,headers,path)
    download_pic2(img_list,answer_list,path)

if __name__=='__main__':
    main_download()
