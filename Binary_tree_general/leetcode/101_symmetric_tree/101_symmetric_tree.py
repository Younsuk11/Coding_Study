
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
traverse the tree in a BFT mammaner 
compare the left and right child of each node 
level by level


'''


from typing import Optional , List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
    
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


    def separate_each_level(self, root: Optional[TreeNode]) -> List:

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
    


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    # node4 = TreeNode(3)
    node5 = TreeNode(4)
    # node6 = TreeNode(3)
    node7 = TreeNode(4)



    node1.left = node2
    node1.right = node3
    # node2.left = node4
    node2.right = node5
    # node3.left = node6
    node3.right = node7

    tree = TreeNode(node1)
    sol = Solution()
    
    levels = sol.separate_each_level(node1)
    return sol.isSymmetric(node1)

if __name__ == "__main__":
    result = main()  