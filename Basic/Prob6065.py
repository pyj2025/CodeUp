# 1 2 4

# 2
# 4

nums = list(map(int, input().split()))

for n in nums:
    if n % 2 == 0:
        print(n)