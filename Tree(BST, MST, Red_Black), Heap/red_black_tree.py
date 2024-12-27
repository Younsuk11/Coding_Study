class Node:
    def __init__(self,key, color = "BLACK", left=None, right = None, parent = None):
        self.key =key
        self.color = color
        self.left = left if left is not None else None
        self.right = right if right is not None else None
        self.parent = parent if parent is not None else None

    
class RBT:
    def __init__(self):
        self.TNull = Node(0) # as T.Nill, external node
        self.TNull.color = "BLACK"
        self.root = self.TNull

    def search_helper(self, node, key):
        #node부터 시작해서 key를 찾기
        if node == self.TNull or key == node.key:
            return node ## 없거나 찾았거나.
        if node<node.key:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)

    def search(self, key):
        return self.search_helper(self.root, key)
    

    def Insert(self, key):

        x = self.root # 삽입할 곳.
        y = None # 삽입할 곳의 parent
        z = Node(key)
        z.parent = None
        
        while(x !=self.TNull):
            y = x
            if(key < x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y

        
        if (y == None):## root
            self.root = z
        elif (key < y.key):
            y.left = z
        else:
            y.right = z

        z.color = "RED"
        z.left = self.TNull
        z.right = self.TNull
        self.InsertFixUP(z)

    def InsertFixUP(self, z):
        '''
        if
        case 1: red uncle y 
        -> recolor : parent(black), grandparent(red), uncle(black)
        -> move z to grandparent -> fixup again
        
        else
        // case2 & 3 모두 왼쪽 기준임. 오른쪽은 반대로 해야함.
        case2 : black uncle y & z = right child
        -> parent left rotate -> case 3

        case 3 : black uncle y & z = left child
        -> recolor : parent(black), grandparent(red), -> grandparent right rotate
        '''
        while(z!=self.root and z.parent.color == "RED"):

            
            if (z.parent == z.parent.parent.right):
                #uncle이 left child일 경우
                uncle = z.parent.parent.left
                if uncle.color =="RED" : # case 1
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent ## fix up again
                
                else: #case2 and 3

                    if z ==z.parent.left : ##case 2
                        z = z.parent
                        ## right rotation
                        self.RotateRight(z)

                    #case 3
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.RotateLeft(z.parent.parent)


            else:
                #uncle이 right child일 경우
                uncle = z.parent.parent.right
                if uncle.color =="RED" : # case 1
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent ## fix up again
                
                else: #case2 and 3

                    if z ==z.parent.right : ##case 2
                        z = z.parent
                        ## right rotation
                        self.RotateLeft(z)

                    #case 3
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.RotateRight(z.parent.parent)

        self.root.color = "BLACK"


    def IsKey(self,key):
        z = self.root

        while(z !=self.TNull and z.key != key):
   
            if key < z.key:
                z = z.left
            else:
                z =z.right
        return z # TNull or key node


    def Delete(self,key):
        '''
        Case1 : no child
        -> y = z
        ->simply remove it and replace with z

        Case2: just one child
        -> y = z
        ->elevate child , z 대체

        Case3 : two child
        y = right least : no left child
        -> 3-1 : y가 z의 child인 경우 -> just replace with it
        -> 3-2 : y가 z의 child가 아닌 경우 -> rightrotate(y)
        '''

        z = self.IsKey(key)

        if z== self.TNull:
            return
        
        y = z
        y_original_color = y.color

        # delete as bst
        # 근데,x가 될 친구를 골라야 한다.

        if (z.left == self.TNull):
            x = z.right
            self.Transplant(z, z.right)
        
        elif(z.right == self.TNull):
            x = z.left
            self.Transplant(z, z.left)


        else: ## two child
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right

            ## case 3.2
            if (y != z.right): #replace by its right child
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            else:
                x.parnet = y ## 단순 명시
            
            ## replace z with y
            self.Transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == "BLACK":
            self.DeleteFixUp(x)
    



    def DeleteFixUp(self, x):
        '''
        operation with siblings
        '''


        # while(x !=self.root and x.color =="BLACK"):
        #     s = x.parent.right

        pass
        





    def RotateLeft(self, x):
        y = x.right
        x.right = y.left

        if (y.left != self.TNull):
            y.left.parent = x
        y.parent = x.parent

        if (x.parent ==None):
            self.root = y ## 바로 rooot

        elif (x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right =y
        
        y.left = x
        x.parent = y
    
    def RotateRight(self, x):
        y = x.left
        x.left = y.right

        if(y.right !=self.TNull):
            y.right.parent = x
        
        y.parent = x.parent
        if (x.parent == None):
            self.root = y

        elif(x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.right = x
        x.parent = y


    def Transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u== u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v
        
        v.parent = u.parent

    def tree_minimum(self, x):
        while (x.left != self.TNull):
            x = x.left

        return x
    
    def tree_maximum(self, x):
        while(x.right != self.TNull):
            x = x.right
        return x

    def print_tree(self, node, indent, last):
        if node != self.TNull:
            print(indent, end=" ")
            if last:
                print("R----", end = " ")
                indent +="     "
            else:
                print("L----", end = " ")
                indent += "|     "
            
            s_color = "RED" if node.color == "RED" else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
        
    def pretty_print(self):
        self.print_tree(self.root, "", True)


def main():
    rbt = RBT()
    node_value = [15,14,13,12,11,10]
    for n in node_value:
        rbt.Insert(n)

    rbt.pretty_print()

    





if __name__ == "__main__":
    main()


        