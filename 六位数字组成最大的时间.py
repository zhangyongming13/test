# 给定包含6个数字的数组，求出能组成的最大时间，不能组成返回invalid
# [0,2,3,0,5,6]返回23:56:00。[9,9,9,9,9,9]返回invalid


def judage_(number, result, data):
    for j in range(number)[::-1]:
        if j in data:
            result.append(str(j))
            data.remove(j)
            break


def max_time(data):
    result = []
    for i in range(6):
        # 小时的十位数
        if i == 0:
            judage_(3, result, data)
        # 小时的个位数
        if i == 1:
            judage_(5, result, data)
        # 分钟或秒的十位数
        if i == 2 or i == 4:
            judage_(6, result, data)
        # 分数或秒的个位数
        if i == 3 or i == 5:
            judage_(7, result, data)
    if len(result) == 6:
        return result
    else:
        return 'invalid'


if __name__ == '__main__':
    while True:
        try:
            input_list = list(input())
            data = []
            for i in input_list:
                try:
                    tmp = int(i)
                    # 输入的数字已经有大于6的，后面就不用判断，肯定组不成时间
                    if tmp > 6:
                        break
                    data.append(tmp)
                except:
                    pass
            # 输入的数字中有大于6的，不用判断直接输出invalid
            if len(data) == 6:
                result = max_time(data)
                if result == 'invalid':
                    print(result)
                else:
                    # 输出时间
                    for key, value in enumerate(result):
                        print(value, end='')
                        if key == 1 or key == 3:
                            print(':', end='')
                    print()
            else:
                print('invalid')
        except Exception as e:
            break
