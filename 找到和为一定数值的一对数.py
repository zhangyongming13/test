# 输入一维数组array和n，找出和值为n的任意两个元素。例如： array = [2, 3, 1, 10, 4, 30] n = 31 则结果应该输出1, 30 顺序不重要 如果有多个
# 满足条件的，返回任意一对即可，不能使用哈希表
while True:
    try:
        n = int(input())
        array = input().split(' ')
        flag = 0
        for i in range(len(array) - 1):
            if flag != 0:
                break
            for j in range(i + 1, len(array)):
                if int(array[i]) + int(array[j]) == n:
                    print(array[i] + ' ' + array[j])
                    flag += 1
                    break
        if flag == 0:
            print('不存在！')
    except Exception as e:
        print(e)
        break
