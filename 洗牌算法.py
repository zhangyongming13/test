# https://www.zymblog.top/blog/156
import random


if __name__ == '__main__':
    test = list(range(25))
    print('原始数组')
    print(test)
    for i in range(25)[::-1]:
        # 在前i个中（包括i）随机选出一个数与test[i]进行交换
        temp = random.choice(range(0, i + 1))
        test[i], test[temp] = test[temp], test[i]
    print('洗牌算法处理过之后的数组')
    print(test)
    print('需要的5个数')
    print(test[0:5])
