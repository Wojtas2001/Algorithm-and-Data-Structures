
# Depth First Search algortihm for graph in matrix representation
# Time complexity: O(V^2)
# where V - number of vertex
# It could be done in O(V*log(E)) in list representation

def dfs(G):
    n = len(G)
    time = 0
    visited = [False]*n
    entry = [0]*n
    parent = [-1]*n
    process = [0]*n


    def dfs_visit(u):
        nonlocal G, visited, entry, parent, process, time
        time += 1
        visited[u] = True
        entry[u] = time
        for v in range(n):
            if not visited[v] and G[u][v] != -1:
                parent[v] = u
                dfs_visit(v)
        time += 1
        process[u] = time

    for ver in range(n):
        if not visited[ver]:
            dfs_visit(ver)

