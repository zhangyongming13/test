# https://www.nowcoder.com/practice/f8538f9ae3f1484fb137789dec6eedb9?tpId=37&tqId=21283&tPage=3&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对
def sushu(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_all_sushu(number):
    result = []
    for i in range(2, number):
        if sushu(i):
            result.append(i)
    return result


def get_fuhe_sushu(input_data, number):
    li_length = len(input_data)
    tmp1 = 0
    tmp2 = 0
    for i in range(li_length):
        for j in range(i, li_length):
            if input_data[i] + input_data[j] == number:
                tmp1 = input_data[i]
                tmp2 = input_data[j]
    return tmp1, tmp2


if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            if number <= 2:
                continue
            else:
                input_data = get_all_sushu(number)
                tmp1, tmp2 = get_fuhe_sushu(input_data, number)
                print(tmp1)
                print(tmp2)
        except Exception as e:
            break
