# https://www.nowcoder.com/practice/668603dc307e4ef4bb07bcd0615ea677?tpId=37&tqId=21297&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
while True:
    try:
        input_string = str(input())
        result = []
        # flag用来记录遇到“和”
        flag = 0
        start = 0
        for index, value in enumerate(input_string):
            if value == '“':
                flag += 1
            if value == '”':
                flag -= 1
            if value == ' ' and flag == 0:
                tmp = input_string[start:index]
                result.append(tmp.strip('“”'))
                tmp = []
                start = index + 1
        result.append(input_string[start:].strip('“”'))
        print(len(result))
        for i in result:
            print(i)
    except Exception as e:
        break
