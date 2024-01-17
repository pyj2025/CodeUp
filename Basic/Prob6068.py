# 73 => B

a = int(input())

def getGrade(a):
    if(a >= 90):
        return "A"
    elif(a >=70 and a < 90):
        return "B"
    elif(a >= 40 and a < 70):
        return 'C'
    else:
        return "D" 

print(getGrade(a))

