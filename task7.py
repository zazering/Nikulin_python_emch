# task 7
n = int(input())
f0 = 0
f1 = 1
for i in range(n):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(n, fn)
