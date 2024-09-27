# 아이스크림 문제와 유사한 것 같기도 하다

n, m = map(int, input().split())

# init lab
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

# virus movement definition
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# test-lab
test = []

def virus_init(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                virus_init(nx, ny)

def calc_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                score += 1
    return score

max_score = 0
def start(wall):
    global max_score

    # when the walls are all set
    if wall == 3:
        # test_lab init
        for i in range(n):
            for j in range(m):
                test[i][j] = lab[i][j]
        # virus_init
        for i in range(n):
            for j in range(m):
                if test[i][j] == 2:
                    virus_init(i, j)
        # get score
        max_score = max(max_score, calc_score())
        return

    # else set more walls
    # 생각해보면 이해는 되는데, 아마도 이 부분을 생각해내는 것이 가장 어려웠을 것 같다
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                start(wall)
                lab[i][j] = 0
                wall -= 1

start(0)
print(max_score)