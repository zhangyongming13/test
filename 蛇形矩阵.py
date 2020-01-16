# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形
# 样例输入
#
# 5
#
# 样例输出
#
# 1 3 6 10 15
#
# 2 5 9 14
#
# 4 8 13
#
# 7 12
#
# 11

if __name__ == '__main__':
    while True:
        # 每一行的除了第一个元素之外，都是a[n + 1] = a[n] + i + j + 1，i为行数j为列数
        # 第一列除了第一个元素之外，都是a[j + 1] = a[j] + j
        try:
            N = int(input())
            # zhang为记录每一行第一个元素的变量
            zhang = 1
            for i in range(N):
                add_mount = []
                for j in range(N - i):
                    # 每一行的第一个
                    if j == 0:
                        add_mount.append(str(zhang))
                        # yong用来计算每一行各个元素
                        yong = zhang
                    else:
                        add_mount.append(str(yong + j + 1 + i))
                        yong = yong + j + 1 + i
                print(' '.join(add_mount))
                zhang = zhang + i + 1
        except Exception as e:
            print(e)
            break
