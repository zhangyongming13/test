# https://www.nowcoder.com/practice/34a597ee15eb4fa2b956f4c595f03218?tpId=37&tqId=21262&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 该题测试用例存在问题
import sys


def split_ip(ip_or_mask):
    result = list(map(int, ip_or_mask.split('.')))
    return result


def Ob_ip(ip_or_mask):
    result = []
    for i in ip_or_mask:
        temp = bin(i).split('b')[-1]
        pre_zero = ''
        for i in range(8 - len(temp)):
            pre_zero += '0'
        temp = pre_zero + temp
        result.append(temp)
    return result


def mask_ip(mask, ip):
    result = []
    for mask_split, ip_split in zip(mask, ip):
        for i, j in zip(mask_split, ip_split):
            if i == '1' and j == '1':
                result.append('1')
            else:
                result.append('0')
    return result


def check_ip(ip, mask_flag):
    for index, i in enumerate(ip):
        if index == 0:
            if i ==0 or i > 223:
                if mask_flag:
                    pass
                else:
                    return False
        elif i < 0 or i > 255:
            return False
    return True


if __name__ == '__main__':
    while True:
        try:
            # input_data = input()
            mask = split_ip(sys.stdin.readline().strip())
            ip_1 = split_ip(sys.stdin.readline().strip())
            ip_2 = split_ip(sys.stdin.readline().strip())
            if check_ip(mask, True) and check_ip(ip_1, False) and check_ip(ip_2, False):
                mask = Ob_ip(mask)
                ip_1 = Ob_ip(ip_1)
                ip_2 = Ob_ip(ip_2)
                result_1 = mask_ip(mask, ip_1)
                result_2 = mask_ip(mask, ip_2)
                if result_1 == result_2:
                    print(0)
                else:
                    print(2)
            else:
                print(1)
        except:
            break
