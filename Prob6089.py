# 2 3 7 => 1458

a, r, n = map(int, input().split())
result = a

for i in range(n-1):
    result *= r
    
print(result)