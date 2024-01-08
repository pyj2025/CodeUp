# 5 5
# 3
# 2 0 1 1
# 3 1 2 3
# 4 1 2 5

# 1 1 0 0 0
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 0 0 1

w, h = map(int, input().split())
result = []

for _ in range(w):
    row = []
    for _ in range(h):
        row.append("0")
    result.append(row)

n = int(input())

for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(y - 1, y + l - 1):
            result[x - 1][i] = "1"
    else:
        for i in range(x - 1, x + l - 1):
            result[i][y - 1] = "1"

for k in result:
    print(" ".join(k))

