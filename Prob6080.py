# 2 3

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

a, b = map(int, input().split())

for i in range(a):
    for j in range(b):
        print(f"{i+1} {j+1}")