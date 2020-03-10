# https://www.nowcoder.com/practice/995b8a548827494699dc38c3e2a54ee9?tpId=37&tqId=21313&tPage=5&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此不需要用正号出现）
# 如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
# 现在需要你用程序来判断IP是否合法。
if __name__ == '__main__':
    while True:
        try:
            ip = input()
            try:
                # int如果遇到不是数字字符的话会报错
                ip_list = list(map(int, ip.split('.')))
            except:
                print('NO')
                continue
            # 必须是四个元素组成的，并且第一个不能为0
            if len(ip_list) == 4 and ip_list[0] != 0:
                flag = 0
                for i in ip_list:
                    if i < 0 or i >= 255:
                        print('NO')
                        flag += 1
                        break
                if flag == 0:
                    print('YES')
            else:
                print('NO')
                continue
        except:
            break

