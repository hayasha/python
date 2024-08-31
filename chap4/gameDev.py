# world size
n, m = map(int, input().split())
# init location
x, y, direction = map(int, input().split())

# world init
world = []
for i in range(n):
    row = list(map(int, input().split()))
    world.append(row)

# record init
record = [[0] * m for _ in range(n)]   # list comprehension ?
record[x][y] = 1

# action definitions
def turn_left():
    global direction
    direction = 3 if direction == 0 else direction - 1

def move():
    global x, y, direction
    return {
        0: lambda: [x, y - 1],
        1: lambda: [x + 1, y],
        2: lambda: [x, y + 1],
        3: lambda: [x - 1, y]
    }.get(direction, [x, y])()

# exec
count = 1
turn_time = 0
while True:
    turn_left()

    nx, ny = move()
    if record[nx][ny] == 0 and world[nx][ny] == 0:
        record[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # escape condition
    if turn_time == 4:
        # move back or die
        # move back function is undefined

print(count)



