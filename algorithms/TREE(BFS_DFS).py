#Graph(directed, 단방향 그래프)
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

#BFS
#노드 방문하면서, 인접한 노드 중 방문하지 않았던, 노드만 큐에 넣어서, 큐에 들어있었던 노드부터 방
문
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
    
  
print(BFS_with_adj_list(graph_list, root_node))

#%%
#DFS
#이전에 방문한 노드보다 현재 방문한 노드에 연결된 노드를 방문(먼저 들어간 것부터 처리))

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))


#%%백준 12060


#그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
#단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
#더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.



#input
#정점 : vertex,간선 :edge
#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
#first line : N, M, V
#그다음 각 M에 대해 연결  vertex number 제시 
#입력으로 주어지는 간선은 양방향이다.

#output
#첫째줄에 DFS, 둘째줄 BFS

#Graph 형성 부분(bidirected)
#양방향 그래프
graph = {}
n = input().split(' ') # 공백 기준으로 모두 나눈다.
node, edge, start = [int(i) for i in n] #각각 할당

for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    
    #한줄씩 읽어서 양방향으로  graph형성
    if n1 not in graph:
        graph[n1] = [n2]
        
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)




#BFS
from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft() #들어가있는 것부터, edge 바로 따라가지 않고,
        if n not in visited:
            visited.append(n)
            
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort() #popleft 이기에 제일 작은 것임
                queue += temp
                
    return " ".join(str(i) for i in visited)
        
#DFS


def DFS(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        
        if n not in visited:
            visited.append(n)
            
            if n in graph:
                
                temp = list(set(graph[n]) - set(visited)) # 다녀온 것은 지운다.
                
                temp.sort(reverse = True) #내림차순으로 바꿔서, pop 할때, 작은 것부터
                
                stack += temp
    
    return " ".join(str(i) for i in visited)







print(DFS(graph, start))
print(BFS(graph, start))

#%% 토마토 문제







#%%
#TREE

class Tree(object):
    def __init__(self, x, l=None, r=None): # 'None' means empty Node
        self.x = x	# value of Node
        self.l = l	# left child of Node
        self.r = r	# right child of Node
        


T = Tree(4, Tree(5, Tree(4, Tree(5, None, None), None), None), Tree(6, Tree(1, None, None), Tree(6, None, None)))


#루트 노드부터 리프 노드까지의 경로 중 가장 다양한 값을 가진 경로에서 볼 수 있는 값의 갯수를 구하는 것 입니다.
#예상 답: 3 [4,6,1]
#%%


def solution(T):
    distinct = {1: set([])}
    stack = [(T, [T], set([T.x]))]
    i = 1  # number of path
    while stack:  # DFS
        n, path, value = stack.pop()
        if n.l == None and n.r == None:  # leaf node
            distinct[i] = value
            i = i + 1
        else:
            if n.r != None:
                stack.append((n.r, path + [n.r], value | set([n.r.x])))
            if n.l != None:
                stack.append((n.l, path + [n.l], value | set([n.l.x])))

    answer = 1

    for key in distinct.keys():
        temp = len(distinct[key])
        if temp > answer:
            answer = temp
    print(distinct)
    return answer


