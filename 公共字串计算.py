# https://www.nowcoder.com/practice/98dc82c094e043ccb7e0570e5342dd1b?tpId=37&tqId=21298&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 计算两个字符串的最大公共字串的长度，字符不区分大小
def cal_length(long_list, short_list):
    for i in range(len(short_list))[::-1]:
        j = 0
        while j + i + 1 <= len(short_list):
            if short_list[j:j + i + 1] in long_list:
                return len(short_list[j:j+i+1])
            j += 1
    return 0


if __name__ == '__main__':
    while True:
        try:
            tmp2 = str(input())
            tmp1 = str(input())
            length = 0
            if len(tmp1) >= len(tmp2):
                length = cal_length(tmp1, tmp2)
            elif len(tmp1) < len(tmp2):
                length = cal_length(tmp2, tmp1)
            print(length)
        except Exception as e:
            break
