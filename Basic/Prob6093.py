# 10
# 10 4 2 3 6 6 7 9 8 5

# 5 8 9 7 6 6 3 2 4 10

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

for value in arr:
    print(value, end=" ")