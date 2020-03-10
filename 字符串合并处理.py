# 字符串合并处理
# https://www.nowcoder.com/practice/d3d8e23870584782b3dd48f26cb39c8f?tpId=37&tqId=21253&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 将输入的两个字符串合并。
# 对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
# 对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。
# 如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
# 举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
import re


def join_and_sort(string_1, string_2):
    string_total = string_1 + string_2
    odd_string = sorted(string_total[::2])
    even_string = sorted(string_total[1::2])
    result = []
    for i in range(len(string_total)):
        if i % 2 == 1:
            result.append(even_string.pop(0))
        else:
            result.append(odd_string.pop(0))
    return result


def hex_change(input_string):
    result = []
    for i in input_string:
        if re.search(r'[0-9a-fA-F]', i):
            if i.upper() == 'A':
                i = '5'
            elif i.upper() == 'B':
                i = 'D'
            elif i.upper() == 'C':
                i = '3'
            elif i.upper() == 'D':
                i = 'B'
            elif i.upper() == 'E':
                i = '7'
            elif i.upper() == 'F':
                i = 'F'
            else:
                i = bin(int(i))[2:]
                i = hex(int(((4-len(i)) * '0' + i)[::-1], 2))
                i = i.split('x')[-1]
                if re.search(r'[a-fA-F]', i):
                    i = i.upper()
            result.append(i)
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    while True:
        try:
            input_data = input().split(' ')
            string_1 = input_data[0]
            string_2 = [-1]
            string_3 = join_and_sort(string_1, string_2)
            result = hex_change(string_3)
            print(''.join(result))
        except Exception as e:
            break
