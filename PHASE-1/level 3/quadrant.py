quadrant = lambda x, y: (
    "Quadrant I" if x > 0 and y > 0 else
    "Quadrant II" if x < 0 and y > 0 else
    "Quadrant III" if x < 0 and y < 0 else
    "Quadrant IV" if x > 0 and y < 0 else
    "On X-axis" if y == 0 and x != 0 else
    "On Y-axis" if x == 0 and y != 0 else
    "Origin"
)

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(quadrant(x, y))