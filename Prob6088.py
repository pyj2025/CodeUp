# 1 3 5 => 13

a, d, n = map(int, input().split())
result = a

for i in range(n-1):
    result += d
    
print(result)