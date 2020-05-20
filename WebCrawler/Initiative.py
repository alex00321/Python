import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

name,lat,lng,star,strategy,comment=[],[],[],[],[],[]

for i in range(1,21):
    url='http://travel.qunar.com/p-cs299914-beijing-jingdian-1-%s'%i
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    ul=soup.find('ul',class_='list_item clrfix')
    li=ul.find_all('li')
    for i in range(len(li)):
        name.append(li[i].find('span',class_='cn_tit').text)
        lat.append(li[i]['data-lat'])
        lng.append(li[i]['data-lng'])
        star.append(li[i].find('span',class_='cur_star')['style'])
        strategy.append(li[i].find('div',class_='strategy_sum').text)
        comment.append(li[i].find('div',class_='comment_sum').text)

Attractions=pd.DataFrame({'景点名称':name,'纬度':lat,'经度':lng,'评级':star,'评论数':comment,'攻略数':strategy})
print(Attractions)
