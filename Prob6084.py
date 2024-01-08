# 44100 16 2 10 => 1.7 MB

h, b, c, s = map(int, input().split())
result = format( h * b * c * s / 8 / 1024 / 1024, ".1f")

print(f"{result} MB")