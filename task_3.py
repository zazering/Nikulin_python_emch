# task 3
n = int(input())

hours_passed = n // 60 % 24
minutes_passed = n % 60

print(f"{hours_passed} {minutes_passed}")