class binarytreenode:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def printtree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("l",root.left.data,end=",")
    if root.right!=None:
        print("r",root.right.data,end="")
    print()
    printtree(root.left)
    printtree(root.right)
btn1=binarytreenode(1)
btn2=binarytreenode(2)
btn3=binarytreenode(3)
btn4=binarytreenode(4)
btn5=binarytreenode(5)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
printtree(btn1)
        

"""
1:l 2,r 3
2:l 4,r 5
4:
5:
3:
"""
