# 2 2 2 

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# 8

r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(f"{i} {j} {k}")

print(r * g * b)