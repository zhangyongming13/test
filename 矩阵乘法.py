# https://www.nowcoder.com/practice/ebe941260f8c4210aa8c17e99cbc663b?tpId=37&tqId=21292&tPage=4&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的
while True:
    try:
        x=int(input())
        y=int(input())
        z=int(input())
        a=[]
        b=[]
        for i in range(x):
            line=input().split()
            line=[int(i) for i in line]
            a.append(line)
        for i in range(y):
            line=input().split()
            line=[int(i) for i in line]
            b.append(line)
        for p in range(x):
            for q in range(z):
                sum = 0
                # a=[[1,2,3], [3,2,1]] b=[[1,2],[2,1],[3,3]]
                # q为1的时候a[p]=[1,2,3] i[q]=[1,2,3]
                for j, k in zip(a[p], [i[q] for i in b]):
                    sum += j * k
                print(sum, end=' ')
            print()
    except:
        break
