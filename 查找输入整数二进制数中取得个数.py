# https://www.nowcoder.com/practice/1b46eb4cf3fa49b9965ac3c2c1caf5ad?tpId=37&tqId=21285&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            result = 0
            while number != 0:
                if number % 2 == 1:
                    result += 1
                number = int(number / 2)
            print(result)
        except Exception as e:
            break


if __name__ == '__main__':
    while True:
        try:
            number = int(input())
            number_list = list(bin(number))[2:]
            print(number_list.count('1'))
        except Exception as e:
            break
