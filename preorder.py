class binarytreenode:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    print(root.data,end=":")
    preorder(root.left)
    preorder(root.right)
btn1=binarytreenode(1)
btn2=binarytreenode(2)
btn3=binarytreenode(3)
btn4=binarytreenode(4)
btn5=binarytreenode(5)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
preorder(btn1)
        

"""
1:2:4:5:3:
"""
