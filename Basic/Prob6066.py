# 1 2 4

# odd
# even
# even

nums = list(map(int, input().split()))

for n in nums:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")