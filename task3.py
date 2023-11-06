# task 3
a, b = map(int, input().split())
step = 0
if a < b:
    print(*range(a, b + 1), sep=",")
else:
    print(*range(a, b - 1, -1), sep=",")
