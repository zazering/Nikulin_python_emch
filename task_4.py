x, y, z = map(int, input("Enter three natural numbers on one line: ").split())
if x == y == z:
    count = 3
elif x == y or y == z or x == z:
    count = 2
else:
    count = 0
print(count)
