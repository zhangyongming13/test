# https://www.nowcoder.com/practice/66ca0e28f90c42a196afd78cc9c496ea?tpId=37&tqId=21256&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
def change_ip_to_number(ip):
    bin_sys = []
    for i in ip.split('.'):
        zhang = bin(int(i))[2:]
        # 不够八位，在前面加0进行补全
        if len(zhang) < 8:
            zhang = list(zhang)
            lenght = len(zhang)
            for i in range(8 - lenght):
                zhang.insert(0, '0')
        bin_sys.append(''.join(zhang))
    result = int(str(''.join(bin_sys)), 2)
    return result


def change_number_to_ip(number):
    bin_sys = str(bin(int(number)))[2:]
    if len(list(bin_sys)) < 32:
        zhang = list(bin_sys)
        lenght = len(zhang)
        for i in range(32 - lenght):
            zhang.insert(0, '0')
        bin_sys = ''.join(zhang)
    result = []
    result.append(str(int(bin_sys[0:8], 2)))
    result.append(str(int(bin_sys[8:16], 2)))
    result.append(str(int(bin_sys[16:24], 2)))
    result.append(str(int(bin_sys[24:32], 2)))
    return '.'.join(result)


if __name__ == '__main__':
    while True:
        try:
            Ip = input()
            Number = input()
            result_1 = change_ip_to_number(Ip)
            result_2 = change_number_to_ip(Number)
            print(result_1)
            print(result_2)
        except:
            break
