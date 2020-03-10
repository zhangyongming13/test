class BTree(object):

    # 初始化二叉树
    def __init__(self, data, left=None, right=None):
        # 数据域
        self.data = data
        # 左子树
        self.left = left
        # 右子树
        self.right = right

    # 先序遍历，这里使用的是递归的形式
    def preorder(self, result):
        # 访问父节点的数据
        if self.data is not None:
            result.append(self.data)
        # 左边子节点存在，则递归调用左边子节点的先序遍历方法
        if self.left is not None:
            self.left.preorder(result)
        # 右边子节点存在，则递归调用右边子节点的先序遍历方法
        if self.right is not None:
            self.right.preorder(result)

    # 中序遍历，也是使用递归的形式
    def inorder(self, result):
        if self.left is not None:
            self.left.inorder(result)
        if self.data is not None:
            result.append(self.data)
        if self.right is not None:
            self.right.inorder(result)

    # 后序遍历，也是递归的形式
    def postorder(self, result):
        if self.left is not None:
            self.left.postorder(result)
        if self.right is not None:
            self.right.postorder(result)
        if self.data is not None:
            result.append(self.data)

    # 层次遍历，利用队列的性质（先进先出）。这里的队列实现是靠list，并通过pop实现先出
    def levelorder(self, result):
        if self.data is not None:
            myqueue = []
            myqueue.append(self)
            while myqueue:
                node = myqueue.pop(0)
                result.append(node.data)
                if node.left is not None:
                    myqueue.append(node.left)
                if node.right is not None:
                    myqueue.append(node.right)

    # 返回二叉树的高度，求二叉树的高度也是一个递归的过程
    def height(self):
        # 传入的是一个空节点，二叉树高度为0
        if self.data is None:
            return 0
        # 根节点之后，左右两边都没有孩子节点，高度为1
        if self.right is None and self.left is None:
            return 1
        # 左边的孩子为空，右边的不为空，高度等于1 + 右边子树的高度
        elif self.right is not None and self.left is None:
            return 1 + self.right.height()
        # 左边的孩子不为空，右边的为空，高度等于1 + 左边子树的高度
        elif self.right is None and self.left is not None:
            return 1 + self.left.height()
        else:
            # 两边的孩子节点都不为空，高度等于1 + 左右子树中高度最高的
            return 1 + max(self.left.height(), self.right.height())

    # 输出叶子节点，也是通过递归的方式
    def leaves(self, result):
        if self.data is not None:
            if self.left is None and self.right is None:
                result.append(self.data)
            elif self.left is not None and self.right is None:
                self.left.leaves(result)
            elif self.left is None and self.right is not None:
                self.right.leaves(result)
            else:
                self.left.leaves(result)
                self.right.leaves(result)


if __name__ == '__main__':
    tree_node_7 = BTree(7)
    tree_node_8 = BTree(8)
    tree_node_3 = BTree(3)
    tree_node_3.left = tree_node_7
    tree_node_3.right = tree_node_8

    tree_node_9 = BTree(9)
    tree_node_4 = BTree(4)
    tree_node_4.left = tree_node_9

    tree_node_1 = BTree(1)
    tree_node_1.left = tree_node_3
    tree_node_1.right = tree_node_4

    tree_node_5 = BTree(5)
    tree_node_6 = BTree(6)
    tree_node_2 = BTree(2)
    tree_node_2.left = tree_node_5
    tree_node_2.right = tree_node_6

    tree_node_0 = BTree(0)
    tree_node_0.left = tree_node_1
    tree_node_0.right = tree_node_2

    result = []
    print('先序遍历二叉树：')
    tree_node_0.preorder(result)
    print(result)

    result = []
    print('中序遍历二叉树：')
    tree_node_0.inorder(result)
    print(result)

    result = []
    print('后序遍历二叉树：')
    tree_node_0.postorder(result)
    print(result)

    result = []
    print('层序遍历二叉树：')
    tree_node_0.levelorder(result)
    print(result)

    print('二叉树的高度是：')
    print(tree_node_0.height())

    result = []
    print('二叉树的叶子节点有：')
    tree_node_0.leaves(result)
    print(result)
