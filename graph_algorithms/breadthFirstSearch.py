from queue import Queue


# Breadth First Search algortihm for graph in matrix representation
# Time complexity: O(V^2)
# where V - number of vertex
# It could be done in O(V*log(E)) in list representation

def bfs(G, s):
    n = len(G)
    queue = Queue()
    dist = [0]*n
    parent = [-1]*n
    visited = [False]*n
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(n):
            if not visited[v] and G[u][v] != -1:
                dist[v] = dist[u]+1
                parent[v] = u
                queue.put(v)
        visited[u] = True
    print(dist)


if __name__ == '__main__':
    G = [
        [-1, 1, 1, 1, -1],
        [1, -1, -1, -1, -1],
        [1, -1, -1, -1, 1],
        [1, -1, -1, -1, 1],
        [-1, -1, 1, 1, -1],
         ]
    bfs(G, 1)