# https://www.nowcoder.com/practice/3cd4621963e8454594f00199f4536bb1?tpId=37&tqId=21255&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关
# 的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab
# 可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
# import time
#
#
import time
from numba import jit


@jit(nopython=True)
def getFast(InputString):
    zhang = []
    for i in range(len(InputString) - 1, -1, -1):
        zhang.append(i)
    flag = 0
    freq = 0
    for j in zhang:
        if flag != 0:
            break
        for i in range(len(InputString)):
            freq += 1
            if i + j >= len(InputString):
                break
            yong = InputString[i:i + j + 1]
            if yong[0:] == yong[::-1]:
                print(yong)
                print(len(yong))
                flag += 1
                break
    return freq


if __name__ == '__main__':
    while True:
        try:
            InputString = input()
            start_time = time.time()
            freq = getFast(InputString)
            print('循环次数%s' % freq)
            print('运行时间%s' % (time.time() - start_time))
        except Exception as e:
            print(e)
            break



while True:
    try:
        a = input()
        if a:
            maxLen = 0
            if a == a[::-1]:
                maxLen = len(a)
            else:
                for i in range(len(a)):
                    if i - maxLen >= 1 and a[i - maxLen - 1:i + 1] == a[i - maxLen - 1:i + 1][::-1]:
                        maxLen += 2
                        continue
                    if i - maxLen >= 0 and a[i - maxLen:i + 1] == a[i - maxLen:i + 1][::-1]:
                        maxLen += 1
            print(maxLen)
    except:
        break
