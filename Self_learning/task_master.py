# the explaination lays here: https://blog.csdn.net/licheetools/article/details/82946312
# In order to run it, you need to open two cmd windows and one is using "Python task_manager.py", the other is using "python task_worker.py"
import random, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# queue to send task
task_queue = queue.Queue()
# queue to receive task
result_queue = queue.Queue()

# Inherited from base manager
class QueueManager(BaseManager):
    pass
def return_task_queue():
    global task_queue
    return task_queue  # 返回发送任务队列
def return_result_queue():
    global result_queue
    return result_queue # 返回接收结果队列

def test():

    # register both queues into network, callable functions collated the queue object
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # binding port 5000, set the auth key as abc
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # start queue
    manager.start()

    # get the queue object:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # put n tasks into queue
    for i in range(10):
        n = random.randint(0,10000)
        print(f"Put task {n}")
        task.put(n)

    # getting result from queue
    print("Try getting results....")
    for i in range(10):
        try:
            r = result
            r = result.get(timeout=5)
            print('Result: %s' % r)
        except queue.Empty:
             print('result queue is empty.')

    manager.shutdown()
    print("master exit.")

if __name__ == "__main__":
    freeze_support()
    print("start!")
    test()
