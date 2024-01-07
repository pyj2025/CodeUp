# A => best!!!

a = input()

def getComment(a):
    if(a == "A"):
        return "best!!!"
    elif(a == "B"):
        return "good!!"
    elif(a == "C"):
        return 'run!'
    elif(a == "D"):
        return "slowly~" 
    else:
        return "what?"

print(getComment(a))

