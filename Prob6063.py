# 123 456 => 456

def getLarger(a, b):
    if(a >= b):
        return a
    else:
        return b

a, b = map(int, input().split())
print(getLarger(a, b))