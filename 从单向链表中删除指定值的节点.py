# https://www.nowcoder.com/practice/f96cd47e812842269058d483a11ced4f?tpId=37&tqId=21271&tPage=3&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
class Node(object):
    def __init__(self, node_value, next=None):
        self.node_value = node_value
        self.next = next


def create_listnode(node_head, node_value, data):
    # 构建单向链表
    create_data = data
    for i in range(len(create_data) - 1)[::2]:
        temp_node = node_head
        tail = int(create_data[i])
        head = int(create_data[i + 1])
        # 该值已经在链表中了
        if tail in node_value:
            continue
        else:
            node_value.append(tail)
        # 寻找tail在链表中的位置，并插入
        while temp_node != None:
            if temp_node.node_value == head:
                # 插入位置下一个链表不为空，需要避免链表断裂
                if temp_node.next:
                    next_node = Node(tail)
                    next_node.next = temp_node.next
                    temp_node.next = next_node
                    break
                else:
                    temp_node.next = Node(tail)
                    break
            else:
                temp_node = temp_node.next


def del_one_node(node_head, del_node):
    if node_head.node_value == del_node.node_value:
        return node_head.next
    temp_node = node_head
    temp_node_next = temp_node.next
    while temp_node_next:
        # 找到要删除的链表节点，删除
        if temp_node_next.node_value == del_node.node_value:
            temp_node.next = temp_node_next.next
            break
        temp_node = temp_node_next
        temp_node_next = temp_node_next.next
    return node_head


if __name__ == '__main__':
    while True:
        try:
            data = input().split(' ')
            # 用来保存已经在链表的值，避免重复值
            node_value = []
            node_number = int(data[0])
            head_value = int(data[1])
            # 链表头
            node_head = Node(head_value)
            node_value.append(head_value)
            # 创建链表
            create_listnode(node_head, node_value, data[2:-1:])
            del_node = Node(int(data[-1]))
            node_head = del_one_node(node_head, del_node)

            temp_node = node_head
            result = ''
            while temp_node:
                result = result +str(temp_node.node_value) + ' '
                temp_node = temp_node.next
            print(result)
        except Exception as e:
            print(e)
            break
