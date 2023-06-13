import time, threading

# #This is the first practice
# def loop():

#     print(f"thread {threading.current_thread().name} is running..")
#     n = 0
#     while n<5:
#         n+=1
#         print(f'thread {threading.current_thread().name} >>> {n}')
#         time.sleep(1)
    
#     print(f'thread {threading.current_thread().name} ended.')

# print(f"thread {threading.current_thread().name} is running..")
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print(f"thread {threading.current_thread().name} ended.")

balance = 0
def change_it(n):

    global balance
    balance = balance+n
    balance = balance-n

def run_thread(n):
    for i in range(20000000):
        change_it(n)

t1 = threading.Thread(target=run_thread(5))
t2 = threading.Thread(target=run_thread(8))
#t1 = threading.Thread(target=run_thread, args=(5,))
#t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(f"balance is {balance}")

