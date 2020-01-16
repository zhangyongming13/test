# https://www.nowcoder.com/practice/184edec193864f0985ad2684fbc86841?tpId=37&tqId=21243&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 1.长度超过8位。 2.包括大小写字母.数字.其它符号,以上四种至少三种。
import re


if __name__ == '__main__':
    while True:
        try:
            password_string = str(input())
            print(password_string[0:2])
            # 判断密码长度是否符合要求
            if len(password_string) <= 8:
                print('NG')
                continue
            # 判断是否含有大小写字母、数字和其他字符不少于2种
            count = 0
            if re.search('[a-z]', password_string):
                count += 1
            if re.search('[A-Z]', password_string):
                count += 1
            if re.search('[0-9]', password_string):
                count += 1
            if re.search('[^a-zA-Z0-9]', password_string):
                count += 1
            if count < 3:
                print('NG')
                continue
            # 判断是否含有长度超过2的字符串重复，这里只需要判断长度为3的字符串在password中
            # 出现次数是否超过2，子串的原因
            flag = 0
            for i in range(len(password_string) - 3):
                if password_string.count(password_string[i:i + 3]) > 1:
                    flag = 1
                    print('NG')
                    break
            if flag == 0:
                print('OK')
        except Exception as e:
            print(e)
            break
