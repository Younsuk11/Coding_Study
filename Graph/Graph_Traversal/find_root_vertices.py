

'''
2023-09 programming 시험
'''
class GNode:
    def __init__(self, id, color = "W", d = 0, p = None):
        self.id = id # id is a string
        self.color = color 
        self.distance = d
        self.parent = p
    def __str__(self):
        return self.id


def find_root_vertices(G:dict):
    '''
    root vertex : a vertex from which, when started, we can visit all other vertices in the graph
    from vertex : check all connected : using "are all connected"
    '''
    
    ans = []
    for v in G:
        #각 노드에 대해 DFS 진행할 때마다 모든 node 방문이면, 해당 노드는 root vertex임
        visited = {v : False for v in G}
        DFS_help(visited, G, v)

        if all(visited.values()): # 모든 노드 값 true인 경우
            ans.append(v)
    
    ans = [v.id for v in ans]
    print(ans)


        
def DFS_help(visited: dict,G: dict, v:GNode):
    if not visited[v]:
        visited[v] = True
        for w in G[v]:
            DFS_help(visited, G, w)


def are_all_connected(G:dict):
    for v in G:
        visited = {v: False for v in G}
        DFS_help(visited, G, v)
        if not all(visited.values()):
            return False
    return True

def check_path(visited:dict, G: dict, start :GNode, end :GNode)->bool:
    '''
    DFS 풀이
    '''
    if start == end:
        return True
    visited[start] = True

    for w in G[start]:
        if not visited[w]:

            if check_path(visited, G, w, end):
                return True
    return False

 

def main():
    A,B,C = GNode('A'), GNode('B'), GNode('C')
    D,E,F = GNode('D'), GNode('E'),GNode('F')


    G = dict()
    G[A],G[B], G[C] = [C,D], [A,E], [B,D]
    G[D], G[E], G[F] = [F], [F], []
    find_root_vertices(G)

def main2():
    A,B,C = GNode('A'), GNode('B'), GNode('C')
    D,E,F = GNode('D'), GNode('E'),GNode('F')

    G = dict()
    G[A],G[B], G[C] = [D], [E], [B,D]
    G[D], G[E], G[F] = [F], [F], []
    find_root_vertices(G)


if __name__ == "__main__":
    main()
    main2()