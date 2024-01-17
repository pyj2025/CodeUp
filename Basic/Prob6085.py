# 1024 768 24

w, h, b = map(int, input().split())
result = format(w * h * b / 8 / 1024 / 1024, ".2f")
print(f"{result} MB")