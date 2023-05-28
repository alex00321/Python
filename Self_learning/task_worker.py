import time, sys, queue
from multiprocessing.managers import BaseManager

# Inherited from base manager
class QueueManager(BaseManager):
    pass

# this is only to get queue from network, only name provided
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# connecting to the server(here this PC) where it runs task master
server_addr = '127.0.0.1'
print(f'Connect to server {server_addr}')

# this is what is registered in task master
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# connect from network
m.connect()

# get the queue object:
task = m.get_task_queue()
result = m.get_result_queue()

# put n tasks into queue
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print(f"Run task {n}*{n}..")
        r = f"{n}*{n} = {n*n}"
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task is empty.")

print("worker exit.")