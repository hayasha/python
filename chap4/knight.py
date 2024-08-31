size = int(input())
moves = input().split()

x, y = 1, 1
for move in moves:
    if move == 'L':
        if x - 1 < 1:
            continue
        else:
            x = x - 1
    if move == 'R':
        if x + 1 > size:
            continue
        else:
            x = x + 1
    if move == 'U':
        if y - 1 < 1:
            continue
        else:
            y = y - 1
    if move == 'D':
        if y + 1 > size:
            continue
        else:
            y = y + 1

print(x, y)
