x1, y1, x2, y2 = map(int, input("enter coordinates: ").split())
if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
