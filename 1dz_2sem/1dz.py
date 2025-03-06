def read_graph():
    N, M = map(int, input().split())
    res = []
    for i in range(M):
        x, y = (int(x) for x in input().split())
        res.append((x, y))
    return N, res

# Мы не знаем, ориентированный граф или нет, поэтому считаем, что ориентированный
def mk_adj_matrix(N, edge_list):
    res = [[0 for j in range(N)] for i in range(N)]
    for x, y in edge_list:
        res[x][y] = 1
    return res

def reverse_adj_matrix(N, matrix):
    for i in range(N):
        for j in range(i, N):
            if matrix[i][j] == 1:
                if matrix[j][i] == 1:
                    continue
                matrix[j][i] = 1
                matrix[i][j] = 0
    return matrix

def print_matrix(matrix):
    for line in matrix:
        print(*line)

def adj_list(N, edge_list):
    res = [[] for i in range(N)]

    for x, y in edge_list:
        res[x].append(y)
        res[y].append(x)

    return res

def bfs(graph, start, visited):
	queue = [start]
	visited[start] = True

	while queue:
		v = queue.pop(0)
		for neighbor in graph[v]:
			if not visited[neighbor]:
				visited[neighbor] = True
				queue.append(neighbor)


def count_connected_components(graph, N):
	visited = [False] * N
	component_count = 0
	for i in range(N):
		if not visited[i]:
			bfs(graph, i, visited)
			component_count += 1

	return component_count

def dfs(graph, vertex, visited):
    print(f"Входим в вершину {vertex}")
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    print(f"Выходим из вершины {vertex}")

def dfs_trav(graph, N):
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            dfs(graph, i, visited)


N, edge_list = read_graph()
res_alist = adj_list(N, edge_list)
res = mk_adj_matrix(N, edge_list)
print_matrix(res)
print()
print_matrix(reverse_adj_matrix(N, res))
print()
print(count_connected_components(res_alist, N))
print()
dfs_trav(res_alist, N)

def bellman_ford(graph, start, N):
	dist = [float('inf')] * N
	dist[start] = 0

	for _ in range(N - 1):
		for u in range(N):
			for v, weight in graph[u]:
				if dist[u] + weight < dist[v]:
					dist[v] = dist[u] + weight

	for u in range(N):
		for v, weight in graph[u]:
			if dist[u] + weight < dist[v]:
				print("negative_cycle")
				return

	return dist


graph = {
	0: [(1, -1), (2, 4)],
	1: [(2, 3), (3, 2), (4, 2)],
	2: [(3, 5)],
	3: [(4, -3)],
	4: []
}

N = 5
start = 0
distances = bellman_ford(graph, start, N)

print(distances)