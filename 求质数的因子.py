# https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tqId=21229&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            i = 2
            li = []
            # 默认人求质数因子的时候，i从2开始尝试，遇到能整除的时候，这个就是质数因子。number就要变为
            # 被整除的数number 90，质数因子2，剩下就是45
            while i <= number:
                if number % i == 0:
                    li.append(str(i))
                    li.append(' ')
                    number = number // i
                    i = 2
                else:
                    i += 1
            print(''.join(li))
        except:
            break
