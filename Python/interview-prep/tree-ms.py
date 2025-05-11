"""
For chatgpt: https://chatgpt.com/share/6820d03a-3fdc-800b-a3e7-e466b273529b
"""

from collections import defaultdict, deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
    farthest = dist.index(max(dist))
    return farthest, dist

def find_nodes_not_on_any_diameter_path(n, edges):
    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Find one end of the diameter
    u, _ = bfs(1, graph, n)

    # Step 3: Find the other end of the diameter from u
    v, dist_u = bfs(u, graph, n)

    # Step 4: Get distances from v
    _, dist_v = bfs(v, graph, n)

    diameter_len = dist_u[v]

    # Step 5: Nodes on any diameter path satisfy: dist_u[i] + dist_v[i] == diameter_len
    nodes_on_diameter = set()
    for i in range(1, n + 1):
        if dist_u[i] + dist_v[i] == diameter_len:
            nodes_on_diameter.add(i)

    # Step 6: Return nodes not on any diameter path
    result = [i for i in range(1, n + 1) if i not in nodes_on_diameter]
    return result

# === Example Usage ===
n = 5
edges = [(1, 4), (1, 2), (2, 3), (2, 5)]
print(find_nodes_not_on_any_diameter_path(n, edges))  # Output: []
