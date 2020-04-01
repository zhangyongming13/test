# https://www.nowcoder.com/practice/e896d0f82f1246a3aa7b232ce38029d4?tpId=37&tqId=21282&rp=0&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tPage=3
# 由于这里是字符串，而且只要求第一次出现，所以不能使用异或操作符^
if __name__ == '__main__':
    while True:
        try:
            input_str = str(input())
            if input_str == None:
                print(-1)
            else:
                flag = 0
                for i in input_str:
                    if input_str.count(i) == 1:
                        print(i)
                        flag += 1
                        break
                if flag == 0:
                    print(-1)
        except Exception as e:
            break
