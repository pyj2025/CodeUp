# 55 => 10

a = int(input())
total = 0
idx = 0

while(total < a):
    total += idx
    idx += 1
    
print(idx - 1)