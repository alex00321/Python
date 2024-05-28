import threading
from threading import Lock,RLock,Condition

total = 0
lock = RLock()

def add():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        total +=1
        lock.release()
def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -=1 
        lock.release()
thread1 = threading.Thread(target = add)
thread2 = threading.Thread(target = desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)