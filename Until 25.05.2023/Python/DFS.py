'''graph={
    'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]
}
visited=set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')'''


a={
    0:[1,2],
    1:[0,3,4],
    2:[0],
    3:[1],
    4:[2,3]
}
visited=[False for i in range(len(a))]
dfs=[]

def DFS(g,start):
    visited[start]=True
    dfs.append(start)
    for i in g[start]:
        if not visited[i]:
            DFS(g,i)
    return dfs
print(DFS(a,0))