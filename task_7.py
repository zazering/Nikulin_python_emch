a, b, c, d = map(int, input("enter the lengths of the sides: ").split(";"))
if a + c == b + d:
    print("YES")
else:
    print("NO")
