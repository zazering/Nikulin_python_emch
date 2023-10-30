a, b, c, d = map(int, input("Enter the coordinates of two cells separated by commas: ").split(","))
if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
    if (a + b) % 2 == (c + d) % 2:
        print("YES")
    else:
        print("NO")
else:
    print("Wrong input")
