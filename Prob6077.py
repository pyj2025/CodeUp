# 5 => 6

def getSum(a):
    total = 0
    for i in range(a):
        if(i % 2 == 0):
            total += i
    return total

a = int(input())
print(getSum(a))
