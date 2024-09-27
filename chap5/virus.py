from collections import deque

n, k = map(int, input().split())

# init map
lab = [[0] * n] * n
viruses = []
for i in range(n):
    row = list(map(int, input().split()))
    lab[i] = row

    for j in range(n):
        if lab[i][j] != 0:
            # 종류, 시간, 좌표
            viruses.append((lab[i][j], 0, i, j))

# time, x, y
s, x, y = map(int, input().split())

# movement
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

viruses.sort()
q = deque(viruses)

while q:
    # 종류, 시간, 좌표
    level, time, x, y = q.popleft()

    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if lab[nx][ny] == 0:
                lab[nx][ny] = level
                q.append((level, s + 1, nx, ny))

print(lab[x - 1][y - 1])
