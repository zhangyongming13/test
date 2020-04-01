# https://www.nowcoder.com/practice/5821836e0ec140c1aa29510fd05f45fc?tpId=37&tqId=21301&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 设计一个算法完成两个超长正整数的加法
if __name__ == '__main__':
    while True:
        try:
            number_1 = str(input())[::-1]
            number_2 = str(input())[::-1]
            flag = 0
            tmp_list = []
            for j,k in zip(number_1, number_2):
                tmp = int(j) + int(k) + flag
                if tmp >= 10:
                    tmp_list.append(str(tmp % 10))
                    flag = int(tmp / 10)
                else:
                    tmp_list.append(str(tmp))
                    flag = 0
            length_1 = len(number_1)
            length_2 = len(number_2)
            if length_1 > length_2:
                for i in number_1[length_2:]:
                    tmp = int(i) + flag
                    if tmp >= 10:
                        tmp_list.append(str(tmp % 10))
                        flag = int(tmp / 10)
                    else:
                        tmp_list.append(str(tmp))
                        flag = 0
            else:
                for i in number_2[length_1:]:
                    tmp = int(i) + flag
                    if tmp >= 10:
                        tmp_list.append(str(tmp % 10))
                        flag = int(tmp / 10)
                    else:
                        tmp_list.append(str(tmp))
                        flag = 0
            if flag != 0:
                tmp_list.append(str(flag))
            print(''.join(tmp_list[::-1]))
        except Exception as e:
            break
