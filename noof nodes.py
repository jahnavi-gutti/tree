class binarytreenode:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def numnodes(root):
    if root==None:
        return 0
    leftcount=numnodes(root.left)
    rightcount=numnodes(root.right)
    return 1+leftcount+rightcount
btn1=binarytreenode(1)
btn2=binarytreenode(2)
btn3=binarytreenode(3)
btn4=binarytreenode(4)
btn5=binarytreenode(5)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
print(numnodes(btn1))
