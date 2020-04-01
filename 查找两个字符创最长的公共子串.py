# https://www.nowcoder.com/practice/181a1a71c7574266ad07f9739f791506?tpId=37&tqId=21288&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
def get_str(short_str, long_str):
    short_length = len(short_str)
    # 从最短的字符串最长开始找起，直到找到
    for i in range(short_length)[::-1]:
        j = 0
        while j + i < short_length:
            if short_str[j:j+i+1] in long_str:
                return short_str[j:j+i+1]
            j += 1


if __name__ == '__main__':
    while True:
        try:
            tmp1 = str(input())
            tmp2 = str(input())
            if len(tmp1) > len(tmp2):
                short_str = tmp2
                long_str = tmp1
            else:
                short_str = tmp1
                long_str = tmp2
            print(get_str(short_str, long_str))
        except Exception as e:
            break
