'''
수정이 답안
'''


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:



    def flatten(self, head: Node) -> Node:

        '''
        head부터 시작해서 순환하다가 child가 not None일떄
        next로 연결
        이때, 원래 next는 외부 저장을 했다가 잇기.
        '''
        if head is None:
            return None

        cur_node = head
        while(cur_node): # 마지막 노드까지 : 마지막 노드에서 child가 있을 수 있어서
            
            if cur_node.child is not None:

                '''
                child node를 잇고, 그 다음 head를 반환
                이어서 계속 순환하다가 child를 찾는다는 느낌.
                뭔가 재귀함수 느낌이 난다.
                '''
                next = cur_node.next
                child_head = self.flatten(cur_node.child) # find child and like with cur_node

                #linke with child
                cur_node.child = None
                cur_node.next = child_head
                child_head.prev = cur_node


                #find child last
                child_last = child_head
                while(child_last.next):
                    child_last = child_last.next

                #link with cur_node's next
                if (next is not None):
                    child_last.next = next
                    next.prev = child_last
                    cur_node = child_last

            
            cur_node = cur_node.next # 계속 순회
        
        return head

