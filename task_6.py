# task 6
a, b, c = map(float, input().split())
d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
if x1 < x2:
    print(f"{x1:.3f} {x2:.3f}")
else:
    print(f"{x2:.3f} {x1:.3f}")
