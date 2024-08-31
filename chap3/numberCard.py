n, m = map(int, input().split())

result = 0
for i in range(n):
    row = list(map(int, input().split()))
    min_value = min(row)
    result = max(result, min_value)

print(result)