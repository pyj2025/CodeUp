# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 1 0 0 0 0 0 1
# 1 0 0 1 1 1 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 1 0 1 0 1
# 1 0 0 0 0 1 2 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

# 1 1 1 1 1 1 1 1 1 1
# 1 9 9 1 0 0 0 0 0 1
# 1 0 9 1 1 1 0 0 0 1
# 1 0 9 9 9 9 9 1 0 1
# 1 0 0 0 0 0 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

result = []
for _ in range(10):
    result.append(input().split())
    
x = 1
y = 1

while(True):
    if(x > 8 or y > 8):
        break
    else:
        if(result[x][y] == "2"):
            result[x][y] = "9"
            break
        
        result[x][y] = "9"
        if result[x][y+1] == "1" and result[x+1][y] == "1":
            break
        elif result[x][y+1] == "1":
            x += 1
        else:
            y += 1
            
for k in result:
    print(" ".join(k))