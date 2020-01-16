# https://www.nowcoder.com/practice/caf35ae421194a1090c22fe223357dca?tpId=37&tqId=21330&tPage=6&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 计算一个数字的立方根，不使用库函数，double  输入参数的立方根，保留一位小数


def get_number(number):
    Min = 0.0
    Max = number
    # 利用二分查找法
    while Max - Min > 0.001:
        Mid = (Max + Min) / 2.0
        # 表示结果在上半区，所以右边界左移max=mid
        if Mid * Mid * Mid > Number:
            Max = Mid
        # 表示结果在下半区，所以左边界右移min=mid
        elif Mid * Mid * Mid < Number:
            Min = Mid
        else:
            return Mid
    return Max


if __name__ == '__main__':
    while True:
        try:
            Number = float(input())
            result = get_number(Number)
            print('%.1f' % result)
        except:
            break
