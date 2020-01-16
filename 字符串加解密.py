# https://www.nowcoder.com/practice/2aa32b378a024755a3f251e75cbf233a?tpId=37&tqId=21252&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 1、对输入的字符串进行加解密，并输出。
# 2加密方法为：
# 当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
# 当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
# 其他字符不做变化。
# 3、解密方法为加密的逆过程。
import re


def encrypt(input_string):
    input_string_list = list(input_string)
    for i in range(len(input_string_list)):
        # 是字母的时候
        if re.search('[a-z]', input_string_list[i]):
            if input_string_list[i] == 'z':
                input_string_list[i] = 'A'
            else:
                input_string_list[i] = chr(ord(input_string_list[i]) + 1).upper()
        elif re.search('[A-Z]', input_string_list[i]):
            if input_string_list[i] == 'Z':
                input_string_list[i] = 'a'
            else:
                input_string_list[i] = chr(ord(input_string_list[i]) + 1).lower()
        # 是数字的时候
        elif re.search('[0-9]', input_string_list[i]):
            if int(input_string_list[i]) == 9:
                input_string_list[i] = '0'
            else:
                input_string_list[i] = str(int(input_string_list[i]) + 1)
    return ''.join(input_string_list)


def un_encrypt(input_string):
    input_string_list = list(input_string)
    for i in range(len(input_string_list)):
        # 是字母的时候
        if re.search('[a-z]', input_string_list[i]):
            if input_string_list[i] == 'a':
                input_string_list[i] = 'Z'
            else:
                input_string_list[i] = chr(ord(input_string_list[i]) - 1).upper()
        elif re.search('[A-Z]', input_string_list[i]):
            if input_string_list[i] == 'A':
                input_string_list[i] = 'z'
            else:
                input_string_list[i] = chr(ord(input_string_list[i]) - 1).lower()
        # 是数字的时候
        elif re.search('[0-9]', input_string_list[i]):
            if int(input_string_list[i]) == 0:
                input_string_list[i] = '9'
            else:
                input_string_list[i] = str(int(input_string_list[i]) - 1)
    return ''.join(input_string_list)


if __name__ == '__main__':
    while True:
        try:
            OriginalString = input()
            EncryptString = input()
            Result1 = encrypt(OriginalString)
            print(Result1)
            Result2 = un_encrypt(EncryptString)
            print(Result2)
        except:
            break
