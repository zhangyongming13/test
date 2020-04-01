# https://www.nowcoder.com/practice/769d45d455fe40b385ba32f97e7bcded?tpId=37&tqId=21296&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 根据输入的日期，计算是这一年的第几天。。
# 详细描述：
# 输入某年某月某日，判断这一天是这一年的第几天？。


def dijitian(year, month, day):
    if year < 0 or month < 0 or month > 12 or day < 0 or day > 31:
        return -1
    tmp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = sum(tmp[:month - 1]) + day
    if year % 4 == 0:
        result += 1
    return result


while True:
    try:
        input_string = input().split(' ')
        year = int(input_string[0])
        month = int(input_string[1])
        day = int(input_string[-1])
        result = dijitian(year, month, day)
        print(result)
    except Exception as e:
        break
