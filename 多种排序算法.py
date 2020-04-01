# 冒泡排序，平均时间复杂度为O(n**2)，最好情况为O(n)，最坏情况为O(n**2)，稳定
def mao_pao(sort_list):
    tmp_list = sort_list.copy()
    length = len(tmp_list)
    for i in range(length):
        for j in range(length - i - 1):
            if tmp_list[j] > tmp_list[j + 1]:
                tmp_list[j], tmp_list[j + 1] = tmp_list[j + 1], tmp_list[j]
    print(tmp_list)


# 选择排序，无论最好还是最坏时间复杂度O(n**2)，不稳定
def choice_sort(sort_list):
    tmp_list = sort_list.copy()
    length = len(tmp_list)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if tmp_list[j] < tmp_list[min_index]:
                min_index = j
        if min_index != i:
            tmp_list[i], tmp_list[min_index] = tmp_list[min_index], tmp_list[i]
    print(tmp_list)


# 采用小根堆的形式的堆排序，无论最好还是最坏时间复杂度都是O(nlogn)，空间复杂度是O(1)，不稳定
def heap_sort(elems):
    # 构造小根堆，这里的小根堆使用list表示，第一个元素就是根节点，之后的两个元素最为左右节点
    # [1, 2, 4, 6, 5, 8, 9]
    def siftdown(elems, e, begin, end):
        # j为i的左节点
        i, j = begin, begin*2+1
        while j < end:
            # 如果左节点大于右节点，将j指向右节点
            if j < end - 1 and elems[j] > elems[j+1]:
                j += 1
            # j已经指向了两个子节点中最小的了，如果插入的e元素小于j对应的值，则e作为根节点合适，后面不需要运行了
            if e < elems[j]:
                break
            # e比j指向的值大，所以要将j指向的值作为根节点
            elems[i] = elems[j]
            # 将左节点作为根节点，继续构造小堆根
            i, j = j, j*2+1
        # 将e插入到合适的位置
        elems[i] = e

    end = len(elems)
    # 构造小根堆
    for i in range(end//2-1, -1, -1):
        siftdown(elems, elems[i], i, end)
    # 进行堆排序
    print(elems)
    for i in range(end-1, 0, -1):
        # 堆顶元素与堆后一个元素交换
        e = elems[i]
        elems[i] = elems[0]
        # 将最后一个元素当做堆顶，所以插入的位置是0，进行堆调整
        siftdown(elems, e, 0, i)
    return elems


# 快速排序，平均时间复杂度和最好情况时间复杂度都是O(nlogn)，最坏情况是O(n**2)
# 空间复杂度是O(logn)，快速排序是不稳定的
def quick_sort(elems, low, high):
    def partitong(elems, low, high):
        # i用来记录基准值pivot放到哪里
        i = low - 1
        pivot = elems[high]
        # 将比基准值pivot小的放到左边，
        for j in range(low, high):
            if elems[j] <= pivot:
                i = i + 1
                elems[i], elems[j] = elems[j], elems[i]
        # 将基准值放到比他小的区域和比他大的区域之间
        elems[i+1], elems[high] = elems[high], elems[i+1]
        return i + 1
    if low < high:
        pi = partitong(elems, low, high)
        # 对两部分递归使用快速排序
        quick_sort(elems, low, pi-1)
        quick_sort(elems, pi+1, high)


if __name__ == '__main__':
    sort_list = [5, 6, 8, 1, 2, 9, 4]
    mao_pao(sort_list)
    choice_sort(sort_list)
    print(heap_sort(sort_list.copy()))

    length = len(sort_list)
    quick_sort(sort_list, 0, length-1)
    print(sort_list)
