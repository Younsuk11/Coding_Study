'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.



For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.

'''


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        '''
        you may construct new graph object from giveen node object
        dft traversal construction

        all connected graph
        '''

        #initialize 
        if node is None:
            return None
        
        #dft
        if node in self.visited:
            return self.visited[node] # Node()
        
        #if not visited then
        new_graph = Node(node.val)
        self.visited[node] = new_graph # visited 처리
        
        for neighbor in node.neighbors:
            new_graph.neighbors.append(self.cloneGraph(neighbor))
            
        
        return new_graph
    

    def cloneGraph2(self, node: Node) -> Node:

        '''
        위 함수랑 같은데 간단하게 짠 코드
        '''
        old_to_new ={}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None
    
    def cloneGraph_bft(self, node : Node)-> Node:
        if node is None:
            return None
        
        visited = {} # {old node : new node}
        from collections import deque

        q = deque([node])
        new_graph = Node(node.val)
        visited[node] = new_graph # first node

        while q:
            n= q.popleft()

            if n not in visited:
                visited[n] = Node(n.val) # new node
            
            for nei in n.neighbors:
                if nei not in visited:
                    q.append(nei)
                    visited[nei] = Node(nei.val)
                
                visited[n].neighbors.append(visited[nei])
        
        
        return visited[node]

   
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    sol = Solution()
    print(sol.cloneGraph(node1))    

    # Test the cloneGraph_bft function
    cloned_graph_bft = sol.cloneGraph_bft(node1)
    print(cloned_graph_bft)
    