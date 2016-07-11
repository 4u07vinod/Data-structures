class BinaryTree(object):

    def __init__(self, root):
        self.key = root
        self.leftnode = None
        self.rightnode = None


    def insertleft(self, leftnode):
        if self.leftnode is None:
            self.leftnode = BinaryTree(leftnode)
            return
        t = BinaryTree(leftnode)
        t.leftnode = self.leftnode
        self.leftnode = t

    def insertright(self, rightnode):
        if self.rightnode is None:
            self.rightnode = BinaryTree(rightnode)
            return
        t = BinaryTree(rightnode)
        t.rightnode = self.rightnode
        self.rightnode = t

    def getRightChild(self):
        return self.rightnode

    def getLeftChild(self):
        return self.leftnode

    def setRootValue(self, value):
        self.key = value

    def getRootval(self):
        return self.key

    def preorder(self):
        print self.key
        if self.leftnode:
            self.leftnode.preorder()
        if self.rightnode:
            self.rightnode.preorder()

    def inorder(self):
        if self.leftnode:
            self.leftnode.inorder()
        print self.key
        if self.rightnode:
            self.rightnode.inorder()

    def postorder(self):
        if self.rightnode:
            self.rightnode.postorder()
        if self.leftnode:
            self.leftnode.postorder()
        print self.key

    def insert(self, data):
        if data > self.key:
            if self.leftnode is not None:
                self.leftnode.insert(data)
            else:
                self.leftnode = BinaryTree(data)
        else:
            if self.rightnode is not None:
                self.rightnode.insert(data)
            else:
                self.rightnode = BinaryTree(data)




if __name__ == '__main__':

    t = BinaryTree(10)
    t.insert(2)
    t.insert(30)
    t.insert(1)
    t.insert(50)

    t.postorder()

