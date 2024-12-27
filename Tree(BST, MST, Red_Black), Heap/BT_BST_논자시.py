class TNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(T: TNode) -> int:
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


def is_balanced(T: TNode) -> bool:

    currnode = T
    if (currnode is None):return True
    left_height = height(currnode.left)
    right_height = height(currnode.right)
    if abs(left_height-right_height) <=1:
        return True

    return False


def is_bst(T: TNode) -> bool:

    currnode = T
    if (currnode is None): return True
    left_bst = is_bst(currnode.left)
    right_bst = is_bst(currnode.right)
    if (left_bst and right_bst):
        if (currnode.left is not None and currnode.val >= currnode.left.val):
            return True
        if (currnode.right is not None and currnode.val <= currnode.right.val):
            return True
        if (currnode.left is None and currnode.right is None): return True
    return False


def common_ancestors(T: TNode, U: TNode, V: TNode) -> list[int]:

    '''
    U와 V의 common ancestors : ancestor들을 쭉 뽑은 다음 같은 것만 추리자.
    root에서 시작한 DFT를 통해 anscestor를 U,V에 대해서 구하고, 같은 ancestor들만 추린다.
    '''
 
    
    def dfs(curnode : TNode, target : TNode, path):
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


def lca(T: TNode, U: TNode, V: TNode) -> int:

    '''
    lca : lowest common ancestor
    U, V의 common ancestors 중, 가장 멀리 있는 노드를 찾는 것.
    '''

    common_ancestor = common_ancestors(T, U, V)
    return [common_ancestor[0]]




def main():
    T7, T8, T9 = TNode(4), TNode(9), TNode(13)
    T3, T4 = TNode(1), TNode(6, T7, None)
    T5, T6 = TNode(11, T8, T9), TNode(20)
    T1, T2 = TNode(3, T3, T4), TNode(15, T5, T6)
    T0 = TNode(8, T1, T2)

    print(height(T0)) # 3
    print(height(T7)) # 1

    print(is_balanced(T0)) # True
    print(is_bst(T0)) # True

    # 1(b)
    T7, T8, T9 = TNode(7), TNode(5), TNode(9)
    T3, T4 = TNode(1), TNode(4, T7, None)
    T5, T6 = TNode(20, T8, T9), TNode(6)
    T1, T2 = TNode(3, T3, T4), TNode(15, T5, T6)
    T0 = TNode(8, T1, T2)

    print(is_bst(T0)) # False

    print(common_ancestors(T0, T6, T8)) # [8, 15]
    print(lca(T0, T6, T8))



if __name__ =="__main__":
    main()