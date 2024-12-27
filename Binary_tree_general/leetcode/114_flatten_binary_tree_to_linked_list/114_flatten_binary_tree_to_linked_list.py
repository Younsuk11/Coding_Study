'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

DFT pre-order
마찬가지로 tree구조이지만, 항상 right child만 있고, left child는 모두 null인 형태를 말함.

'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)


    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node6

    tree = TreeNode(node1)
    sol = Solution()

    print(sol.flatten(node1))


if __name__ == "__main__":
    main()  