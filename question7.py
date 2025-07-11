# Get points
pts = []
n = int(input("Number of points: "))
for i in range(n):
    x = int(input(f"x{i+1}: "))
    y = int(input(f"y{i+1}: "))
    pts.append((x,y))

# Check if straight line
straight = True
if n > 2:
    x0,y0 = pts[0]
    x1,y1 = pts[1]
    for x,y in pts[2:]:
        if (y1-y0)*(x-x0) != (y-y0)*(x1-x0):
            straight = False
            break

print("Straight line!" if straight else "Not straight")