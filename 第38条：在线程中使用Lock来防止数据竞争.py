from threading import Thread
from threading import Lock
import time


def timer(kind):
    def decorate(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            print('%s程序运行了%0.3f秒' % (kind, end_time - start_time))
        return wrapper
    return decorate


# 定义一个counter类
class Counter(object):
    def __init__(self):
        # 在类中创建一个lock属性
        self.lock = Lock()
        self.count = 0

    # 对收集到的数据进行相加
    def increment(self, value):
        # 获取锁，语句执行完毕之后释放锁（和文件打开操作的with类似）
        # with self.lock:
        self.count += value


def woker(sensor_index, times, counter):
    for _ in range(times):
        # 假设每次从传感器中读到的数据都是1
        counter.increment(1)


# 创建5个线程运行目标func
@timer('多线程')
def run_thread(func, times, counter):
    threads = []
    for i in range(5):
        args = (i, times, counter)
        thread = Thread(target=func, args=args)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    counter = Counter()
    times = 10 ** 5
    worker = woker
    # 将函数作为参数传递
    run_thread(worker, times, counter)
    print('count应该是500000，但实际是%s' % counter.count)
