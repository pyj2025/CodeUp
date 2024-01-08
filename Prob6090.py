# 1 -2 1 8 => -85

a, m, d, n = map(int, input().split())
result = a

for i in range(n-1):
    result *= m
    result += d
    
print(result)