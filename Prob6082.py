# 9 => 1 2 X 4 5 X 7 8 X

n = list(map(str, range(1, int(input())+1)))

for i in n:
    if "3" in i or "6" in i or "9" in i:
        n[n.index(i)] = "X"
        
print(" ".join(n))
