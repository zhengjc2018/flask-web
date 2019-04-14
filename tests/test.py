class Node():
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        queue = ［self.root］
        if self.root is None:
             self.root = node
        cur_node = queue.pop(0)
        while queue:
        if cur_node.lchild is None:
            cur_child.lchild = node
            return
        else:
             queue.append(cur_node.lchild)
        if cur_node.rchild is None:
            cur_child.rchild = node
            return
        else:
             queue.append(cur_node.rchild)


# 四大遍历
# * 广度遍历 上到下 左到右
# * 前序遍历  根 左 右
# * 中序遍历  左 根 右
# * 后序遍历  左 右 根


def preorder(self, node):
  if node is None:
      return
    print (node.elem)
    preorder (node.lchild)
    preorder (node.rchild)
