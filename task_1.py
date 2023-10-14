# task 1
a = float(input())
b = float(input())
c = float(input())

average = (a + b + c) / 3
harmonic_mean = 3 / (1 / a + 1 / b + 1 / c)
median = a + b + c - min(a, b, c) - max(a, b, c)
max_min_divided_by_average = max(a, b, c) ** min(a, b, c) / average

print(f"{average:.3f};{harmonic_mean:.3f};{median:.3f};{max_min_divided_by_average:.3f}")