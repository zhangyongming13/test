# https://www.nowcoder.com/practice/2f6f9339d151410583459847ecc98446?tpId=37&tqId=21261&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
# 最后的误差判断是小数点3位
if __name__ == '__main__':
    while True:
        try:
            height = int(input())
            print(height * 2.875)
            print(height * 0.03125)
        except:
            break
