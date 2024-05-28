# # import threading
# # total = 0

# # def add():
# #     global total
# #     for i in range(1000000):
# #         i += 1
# #         total +=1
    
# # def desc():
# #     global total
# #     for i in range(1000000):
# #         i += 1
# #         total -=1

# # thread1 = threading.Thread(target = add)
# # thread2 = threading.Thread(target = desc)

# # thread1.start()
# # thread2.start()

# # thread1.join()
# # thread2.join()
# # print(total)

# import time
# import threading
# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")

# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(4)
#     print("get detail url end")

# if __name__ == "__main__":
#     thread1= threading.Thread(target = get_detail_html,args=("",))
#     thread2= threading.Thread(target = get_detail_url,args=("",))

#     start_time = time.time()
#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print("last time {}".format(time.time()-start_time))

