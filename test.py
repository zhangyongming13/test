while True:
    try:
        month=int(input())
        if month<3:
            print(1)
        else:
            a=1
            b=1
            for i in range(3,month+1):
                temp = b
                b = a + b
                a = temp
            print(b)
    except:
        break
