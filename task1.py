# task 1
n = int(input())
sum = 0
ssum = 0
for i in range(n):
    n1 = int(input())
    sum += n1
    ssum += 1 / n1
harmonic_mean = n / ssum
av = sum / n
print(f"{av:.3f} {harmonic_mean:.3f}")
