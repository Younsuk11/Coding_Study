from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(T: TreeNode) -> int:
    '''
    tree traversal로 
    '''
    currnode = T
    if (currnode is None):
        return -1
    left_height = height(currnode.left)
    right_height = height(currnode.right)
    if left_height > right_height:
        return left_height+1
    else:
        return right_height +1


def is_balanced(T: TreeNode) -> bool:

    currnode = T
    if (currnode is None):return True
    left_height = height(currnode.left)
    right_height = height(currnode.right)
    if abs(left_height-right_height) <=1:
        return True

    return False


def is_bst(T: TreeNode, left=float('-inf'), right=float('inf')) -> bool:
    if T is None:
        return True
    if not (left < T.val < right):
        return False
    return is_bst(T.left, left, T.val) and is_bst(T.right, T.val, right)


def common_ancestors(T: TreeNode, U: TreeNode, V: TreeNode) -> list[int]:

    '''
    U와 V의 common ancestors : ancestor들을 쭉 뽑은 다음 같은 것만 추리자.
    root에서 시작한 DFT를 통해 anscestor를 U,V에 대해서 구하고, 같은 ancestor들만 추린다.
    '''
 
    
    def dfs(curnode : TreeNode, target : TreeNode, path):
        if curnode is None : return False

        path.append(curnode)

        if target == curnode:
            return True
        
        if (curnode.left and dfs(curnode.left, target, path)) or (curnode.right and dfs(curnode.right, target, path)):
            return True
        
        path.pop() # 해당 경로에 target이 없는 경우임.
        return False


    ancestor_U = []
    dfs(T, U, ancestor_U)

    ancestor_V  = []
    dfs(T, V, ancestor_V)


    ancestor_U = [node.val for node in ancestor_U]
    ancestor_V = [node.val for node in ancestor_V]
    
    common_ancestor = list(set(ancestor_U).intersection(set(ancestor_V)))

    return common_ancestor


def lca(T: TreeNode, U: TreeNode, V: TreeNode) -> int:

    '''
    lca : lowest common ancestor
    U, V의 common ancestors 중, 가장 멀리 있는 노드를 찾는 것.
    '''

    common_ancestor = common_ancestors(T, U, V)
    return [common_ancestor[0]]


def invertTree( root: Optional[TreeNode]) -> Optional[TreeNode]:

    '''
    Given the root of a binary tree, invert the tree, and return its root.
    가운데를 기준으로 바꾸기.

    t = [4,2,7,1,3,6,9] : BFT order

    [4,7,2,9,6,3,1]

    1. level by level로 파악해서 -> flip하고 tree 만들어서 반환
    2. recursively
        right to left, left to right
    '''
    
    if not root:
        return None
    

    #swap
    temp_r= root.right
    root.right = root.left
    root.left= temp_r
    root.right, root.left = invertTree(root.right), invertTree(root.left)
    

    return root




class Solution:


    def __init__(self):
        self.prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        DFT preorder라 생각하고 거꾸로 배열을 조정한다.
        뒤에서부터(right subtree), right child : prev node(이전꺼) / left child : None

        
        """

   
  

        if root == None:
            return
        

  
        
        self.flatten(root.right) 
        self.flatten(root.left) 

        '''
        재귀 함수 call에 의한 하단 코드 실행 노드 순서
        node6 -> node 5 -> node 4 -> node 3 -> node 2 -> node 1
        
        '''

        root.right = self.prev
        root.left = None

        self.prev = root
    


    def flatten_preorder(self, root: Optional[TreeNode]) -> None:
        if not root : 
            return
        
        stack = [root]
        prev = None

        '''
        root 부터 시작해서 left child 먼저 prev의 right으로 옮기기. (prev의 left는 None으로)
        stack을 쓰면 preorder로 순회 가능.

        stack에 의한 노드 처리 순서
        node1 -> node2 -> node3 -> node4 -> node5 -> node6
        '''

        while stack:
            current = stack.pop()


            if prev:
                prev.right = current
                prev.left = None

            # push right first so that left is processed first
            if current.right: stack.append(current.right) #오른쪽부터 넣는 이유는 stack이기 때문에, 나중에 들어간게 먼저 나옴.
            if current.left: stack.append(current.left)
            

            prev = current

class Solution2:
    def isSymmetric(self, root : TreeNode) -> bool:
        
    
        def is_mirror(left, right) -> bool:
            
            # base case 1 : both none
            if (not left) and (not right): 
                return True
            #one of them is none
            if (not left) or (not right): 
                return False
            # both not none : both value are same, mirror
            ''' 
            같다면 recursively, and mirror 형태로.
            left.left vs right right비교
            left.right vs right.left 비교
            '''
            if (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left): 
                return True
   
            return False
            
        if root == None:
            return True
        
        ans = is_mirror(root.left, root.right)
        return ans


    def separate_each_level(self, root:TreeNode) -> List:

        #separate each level of the tree by BFT

        if root == None:
            return []
        
        q = [root]
        result = []

        while q:# empty 여부 조건 검사 할 때가 한 level 임.(depth)
            level = []

            # For each level
            for _ in range(len(q)):
                curNode = q.pop(0)
                level.append(curNode.val)

                if curNode.left:
                    q.append(curNode.left)
   
                if curNode.right:
                    q.append(curNode.right)
                

            result.append(level)

        return result



#129 sum root to leaf numbers

def sumNumbers(root: Optional[TreeNode]) -> int:
    '''
    You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.
    
    root 부터 leaf까지 도달하면서 얻어지는 숫자들의 합. (root -> leaf순으로 숫자를 만들어간다.)

    참고로 path는 dft를 통해서 만들어진다.
    '''
    ans = 0
    def dfs(node: TreeNode, path : int):

        if node is None:
            return

        path   = node.val + path * 10 # 현재 노드 더해주기 : 누적 계산 없어야 함.

        if node.left is None and node.right is None: #leaf node
            nonlocal ans
            ans += path # 지금까지 만든거 누적 합산
        
        else:
            dfs(node.left, path)
            dfs(node.right, path)

        path = (path - node.val) // 10 #backtrack : 갈림길에서 다른 방향으로 가기 위해 이전 노드로 돌아가는 것.

    dfs(root, 0)  

    return ans

    
def maxPathSum( root: Optional[TreeNode]) -> int:
    '''
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
    A node can only appear in the sequence at most once. 
    Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    반드시 root에서 시작하거나, root을 지나가는 path말고, 어떤 노드에서 시작해서 어떤 노드에서 끝나는 path도 가능하다. 그 중, 가장 최대 합을 구하는 것.
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

    Strategy : Dynamic programming, DFT, backtracking
    - 이미 계산된 값들은 저장 (반복 계산 방지) : 재귀적으로 푼다.
    - 어디서 시작을 해야 하나? : 모든 노드를 다 방문해야 하므로, 모든 노드를 다 방문해야 한다.
    - 모든 노드를 방문하면서 각 노드에서 시작하는 path의 합을 구한다.
    - 각 level의 노드에서 left, right child을 더해서 얻을 수 있는 max값으로 갱신한다.
    '''

    max_sum = float('-inf') #최대 값 저장 및 갱신
    def dfs(node : TreeNode) -> int:

        '''
        현재 노드에서 dfs로 출발해서 얻을 수 있는 최대 값.
        '''
        if node is None:
            return 0
        
        #left subtree max
        left = max(dfs(node.left), 0) # left subtree결과가 0보다 작으면 더하지 않을려고, max처리
        right = max(dfs(node.right), 0)

        # 현재 노드를 포함한 path의 합
        nonlocal max_sum
        max_sum = max(max_sum, node.val + left + right)
        
        return node.val + max(left, right) # 현재 노드에서 시작해서 얻을 수 있는 최대값: 왜 max(left, right)인가? : 어차피 한쪽만 선택해야 하기 때문에 : path라서.

    dfs(root)
    return max_sum




def construct_every_path(root : TreeNode) -> List:
    '''
    by following dft, construct every pathway from root to leaf
    '''

    ans = []
    def dfs(node, path):
        if node is None:
            return
        
        path.append(node.val) # 현재 방문한 node를 path에 추가

        if node.left is None and node.right is None:  #leaf node
            ans.append(path.copy())

        else:
            # 둘다 있거나, 둘중 하나만 있거나.
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop() #backtrack : 갈림길에서 다른 방향으로 가기 위해 이전 노드로 돌아가는 것.

    dfs(root, [])

    return ans




def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
    '''
    return sum of all left leaves
    left leaf : leaf that is the left child of another node (with no child)
    - no children tree node
    - 어떤 노드의 left child 이면서, children이 아무것도 없을 때.



    Input: root = [3,9,20,null,null,15,7] : BFT ordering
    Output: 24
    Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.


    Example 2:

    Input: root = [1] : root만 있을 경우는 leaf가 아님.
    Output: 0
    '''
    ans = 0
    q = [root]
    
    while q:
        cur = q.pop(0)

        if cur.left is not None:
            

            temp = cur.left
            if (temp.left is None) and (temp.right is None): #left leaf
                ans += temp.val
            
            
            else: # child가 있을 때 traversal할 이유가 있기에. leaf node는 필요없다.
                q.append(cur.left)


        if cur.right is not None:
            q.append(cur.right)


    return ans



### 번외
def builds_tree(node_vals):
    if not node_vals:
        return None
    
    root =TreeNode(node_vals[0])
    q = [root]
    i  = 1 # indexing and counting

    while q and i<len(node_vals):
        node = q.pop(0)

        if node_vals[i] is not None:
            node.left = TreeNode(node_vals[i])
            q.append(node.left)
        i+=1

        if i<len(node_vals) and node_vals[i] is not None:
            node.right = TreeNode(node_vals[i])
            q.append(node.right)
        i+=1

    return root

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            '''
            Given the root of a binary search tree, and an integer k, 
            return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
            '''


            self.count = 0
            self.result = None
            self.inorderHelp(root, k)

            return self.result
        

    def inorderHelp(self, curNode, k) -> int :

        if not curNode or self.result is not None:
            return
        
        self.inorderHelp(curNode.left, k)
        self.count +=1 

        if self.count == k :
            self.result = curNode.val
        
        self.inorderHelp(curNode.right, k)







class Tree():

    def __init__(self, root: TreeNode = None):
        self.root = root

    def visit(self, node : TreeNode):
        print(node.val)
        '''
        사실 visit  할 때, 찾고자 하는 node인지 여부를 확인하면
        BFT-> BFS(search)
        DFT-> DFS(search)
        가 되는 것. 찾아보니 그냥 동일한 개념이랜다.
        '''
    
    #BFT
    def BFT(self):
        if self.root == None:
            return
        q = [self.root] #or q = deque([self.root])

        while q: # empty 여부 조건 검사 할 때가 한 level 임.(depth)
            curNode = q.pop(0)

            self.visit(curNode) #
            if curNode.left is not None:
                q.append(curNode.left)
            if curNode.right is not None:
                q.append(curNode.right)


    #DFT
    ## preorder
    def __DFT_preorderHelp(self, curNode):
        if curNode == None: ##  curNode가 leaf 이상으로 넘어갔을 경우, 함수 종료.
            return
        
        #먼저 방문하고, 다음 child 로 넘어가기. child 먼저.
        self.visit(curNode)
        self.__DFT_preorderHelp(curNode.left)
        self.__DFT_preorderHelp(curNode.right)

    def DFT_preorder(self):
        self.__DFT_preorderHelp(self.root) # root부터 시작

    
    ##inorder
    def __DFT_inorderHelp(self, curNode):
        if curNode == None:
            return
        
        self.__DFT_inorderHelp(curNode.left)
        self.visit(curNode)
        self.__DFT_inorderHelp(curNode.right)

    def DFT_inorder(self):
        self.__DFT_inorderHelp(self.root)
    
    ##post order
    def __DFT_postorderHelp(self, curNode):
        if curNode == None:
            return
        
        self.__DFT_postorderHelp(curNode.left)
        self.__DFT_postorderHelp(curNode.right)
        self.visit(curNode)

    def DFT_postorder(self):
        self.__DFT_postorderHelp(self.root)




def main():
    T7, T8, T9 = TreeNode(4), TreeNode(9), TreeNode(13)
    T3, T4 = TreeNode(1), TreeNode(6, T7, None)
    T5, T6 = TreeNode(11, T8, T9), TreeNode(20)
    T1, T2 = TreeNode(3, T3, T4), TreeNode(15, T5, T6)
    T0 = TreeNode(8, T1, T2)

    print(height(T0)) # 3
    print(height(T7)) # 1

    print(is_balanced(T0)) # True
    print(is_bst(T0)) # True

    # 1(b)
    T7, T8, T9 = TreeNode(7), TreeNode(5), TreeNode(9)
    T3, T4 = TreeNode(1), TreeNode(4, T7, None)
    T5, T6 = TreeNode(20, T8, T9), TreeNode(6)
    T1, T2 = TreeNode(3, T3, T4), TreeNode(15, T5, T6)
    T0 = TreeNode(8, T1, T2)

    print(is_bst(T0)) # False

    print(common_ancestors(T0, T6, T8)) # [8, 15]
    print(lca(T0, T6, T8))



if __name__ =="__main__":
    main()