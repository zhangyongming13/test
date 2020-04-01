# https://www.nowcoder.com/practice/dbace3a5b3c4480e86ee3277f3fe1e85?tpId=37&tqId=21299&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
if __name__ == '__main__':
    while True:
        try:
            m = int(input())
            if m < 1 or m > 100:
                continue
            else:
                m_3 = m * m * m
                tmp_list = [i for i in range(1, m_3 + 1)[::2]]
                i = 0
                # print(tmp_list)
                result = []
                while i + m < len(tmp_list):
                    if sum(tmp_list[i:i+m]) == m_3:
                        result = tmp_list[i:i+m]
                    i += 1
                result = list(map(str, result))
                print('+'.join(result))
        except Exception as e:
            break
