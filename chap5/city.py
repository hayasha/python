# size
N, M, K, X = map(int, input().split())

# init graph
graph = []
for i in range(N):
    row = []
    for j in range(N):
        if i == j:
            row.append(0)
        else:
            row.append(99)
    graph.append(row)

for i in range(M):
    _from, _to = map(int, input().split())
    graph[_from - 1][_to - 1] = 1

from collections import deque

q = deque([X - 1])
depth = 0
while q:
    now_city = q.popleft()
    depth += 1
    for next_city in range(N):
        x_next_distance = graph[X-1][next_city]
        now_next_distance = graph[now_city][next_city]
        if x_next_distance == 99 and now_next_distance != 99:
            graph[X-1][next_city] = now_next_distance + depth
            q.append(next_city)

print(graph)

# 모든 거리가 1인 거랑 BFS 무슨 관계?