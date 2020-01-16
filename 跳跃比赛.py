# https://blog.csdn.net/hewhys/article/details/79888315
# 给出一组正整数，你从第一个数向最后一个数方向跳跃，每次至少跳跃1格，每个数的值表示你从这个位置可以跳跃的最大长度。计算如何以最少的跳跃次数跳到最后一个数。
import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    NumberList = []
    for i in range(n):
        line = int(sys.stdin.readline().strip())
        NumberList.append(line)
    Result = 0
    Start = 0
    Flag = 0
    while True:
        Result += 1
        for i in range(Start + 1):
            if NumberList[i] + i > Flag:
                Flag = NumberList[i] + i
        Start = Flag
        if Start + 1 >= n:
            break
    print(Result)
