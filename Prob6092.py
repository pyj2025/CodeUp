# 10
# 1 3 2 2 5 6 7 4 5 9

# 1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(23):
    result.append(0)

for j in arr:
    result[j - 1] += 1
    
for value in result:
    print(value, end=" ")