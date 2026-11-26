class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root = None
        self.cnt=0



 #insert function
    def insert(self,new_node):
        if self.root is None:   #check if tree is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left

                if new_node.data > temp.data: #right subtree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
                
    def search(self,value):
        temp=self.root

        while temp:
            if temp.data==value:
                print("element founnd")
                return
            elif temp.data > value:
                temp=temp.left
            else:
                temp=temp.right
        print("element not fount") 

    def inorder(self,temp):
        if temp is None:
         return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.cnt+=1
            self.inorder(temp.right)

    def preorder(self,temp):
        if temp is None:
            return
        else:
            print(temp.data,end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)  

    def postorder(self,temp):
        if temp is None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right) 
            print(temp.data,end=" ")   
      



b1=BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\ninorder")
b1.inorder(b1.root)


print("\npreorder")
b1.preorder(b1.root)

print("\npostorder")
b1.postorder(b1.root)

print("\nnode count",b1.cnt)










