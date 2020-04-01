# https://www.nowcoder.com/practice/bfd8234bb5e84be0b493656e390bdebf?tpId=37&tqId=21284&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。


def count_method(m, n):
    if m == 0 or n == 1:
        return 1
    # 盘子比苹果多，那样多出来的盘子是空的，计算的时候只需要和苹果一样多的盘子就行了
    elif n > m:
        return count_method(m, m)
    else:
        # n-1表示减少一个盘子，m-n就是想把n个苹果放到n个盘子上
        return count_method(m, n - 1) + count_method(m - n, n)


if __name__ == '__main__':
    while True:
        try:
            input_data = input()
            m = int(input_data.split(' ')[0])
            n = int(input_data.split(' ')[-1])
            print(count_method(m, n))
        except Exception as e:
            break
