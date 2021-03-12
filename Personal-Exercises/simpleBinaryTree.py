class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def AddLeft(self, data):
        if self.left is None:
            self.left = Node(data)
        
    def AddRight(self, data):
        if self.right is None:
            self.right = Node(data)

    def PrintTreeByWidth(self):
        print(self.data, end=" ")
        if self.left:
            self.left.PrintTreeByWidth()
        if self.right:
            self.right.PrintTreeByWidth()

    def PrintTreeByBreadth(self):
        q = []
        q.append(self)
        while (q):
            currentNode = q.pop(0)
            print(currentNode.data, end=" ")
            if not (currentNode.left is None):
                q.append(currentNode.left)
            if not (currentNode.right is None):
                q.append(currentNode.right)



# Example Tree
#          3
#       /    \
#      7      5
#    /  \      \
#   2    6      9
#      /  \    /
#     5   11  4


root = Node(2)
root.AddLeft(7)
root.left.AddLeft(2)
root.left.AddRight(6)
root.left.right.AddLeft(5)
root.left.right.AddRight(11)
root.AddRight(5)
root.right.AddRight(9)
root.right.right.AddLeft(4)

root.PrintTreeByWidth()
print("")
root.PrintTreeByBreadth()