# 任给一个数组，元素有20M，1T，300G之类的，其中1T=1000G，1G=1000M
# 按从小到大输出结果
# 例如：输入：3
# 20M
# 1T
# 300G
# 输出：
# 20M
# 300G
# 1T
class Node(object):
    def __init__(self, orginal, value):
        self.orginal = orginal
        self.value = value


def chang_to_m(orginal):
    value = int(orginal[:-1:])
    M_G_T = orginal[-1]
    if M_G_T.upper() == 'G':
        value *= 1000
    elif M_G_T.upper() == 'T':
        value *= 1000000
    return value


if __name__ == '__main__':
    number = int(input())
    li = []
    for _ in range(number):
        orginal = input()
        value = chang_to_m(orginal)
        node = Node(orginal, value)
        li.append(node)
    # 冒泡排序的方式
    # for i in range(number):
    #     for j in range(number - i - 1):
    #         if li[j].value > li[j + 1].value:
    #             li[j], li[j + 1] = li[j + 1], li[j]
    # 使用python内置的排序
    li.sort(key=lambda x:x.value)
    for node in li:
        print(node.orginal)
