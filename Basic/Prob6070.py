# 12 => winter

def getSeason(a):
    if(a // 3 == 1):
        return "spring"
    elif(a // 3 == 2):
        return "summer"
    elif(a // 3 == 3):
        return 'fall'
    else:
        return "winter"

a = int(input())

print(getSeason(a))