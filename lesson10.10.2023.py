# task 1

a = float(input())
b = float(input())
c = float(input())

average = (a + b + c) / 3
harmonic_mean = 3 / (1 / a + 1 / b + 1 / c)
median = a + b + c - min(a, b, c) - max(a, b, c)
max_min_divided_by_average = max(a, b, c) ** min(a, b, c) / average

print(f"{average:.3f};{harmonic_mean:.3f};{median:.3f};{max_min_divided_by_average:.3f}")

# task 2
name = input()
age = int(input())

print(f"Hello, {name}, with age {age}")

# task 3
n = int(input())

hours_passed = n // 60 % 24
minutes_passed = n % 60

print(f"{hours_passed} {minutes_passed}")

# task 4
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

need_class_1 = (class_1 + 1) // 2
need_class_2 = (class_2 + 1) // 2
need_class_3 = (class_3 + 1) // 2

total = need_class_1 + need_class_2 + need_class_3

print(total)

# task 5
a, b, c = map(float, input().split())
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"{area:.3f}")

# task 6
a, b, c = map(float, input().split())
d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
if x1 < x2:
    print(f"{x1:.3f} {x2:.3f}")
else:
    print(f"{x2:.3f} {x1:.3f}")
