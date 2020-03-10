# https://blog.csdn.net/xiuxiu_1204/article/details/102491662


if __name__ == '__main__':
    while True:
        try:
            numberofWeights = int(input())
            eachWeight = [int(i) for i in input().split()]
            eachNumber = [int(i) for i in input().split()]
            # 砝码重量包括0
            allWeights = [0]
            for i in range(numberofWeights):
                temp = allWeights.copy()
                # 遍历同一个砝码，第1个，2个之类的
                for j in range(eachNumber[i]):
                    # 遍历已经有的砝码重量，避免重复
                    for k in temp:
                        d = k + eachWeight[i] * (j + 1)
                        if d not in temp:
                            allWeights.append(d)
            print(allWeights)
            print(len(sorted(allWeights)))
        except Exception as e:
            # print(e)
            break
