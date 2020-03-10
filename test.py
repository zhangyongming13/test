from collections import deque
from threading import Lock
from threading import Thread


class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    # 注意这里的put不是指上传照片等操作，而是将任务放入双头向队列self.items中
    # 担任生产者的角色
    def put(self, item):
        with self.lock:
            # 放到双向队列的右边，确保做到fifo先进先出
            self.items.append(item)

    # 将任务从双向队列中取出
    # 担任消费者的角色
    def get(self):
        with self.lock:
            # 取出双向队列最左边的元素，确保做到fifo先进先出
            return self.items.popleft()
