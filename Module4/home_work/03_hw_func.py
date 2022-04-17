# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def inside(b1, b2, r1, r2):
    # betc = between centre
    betc = distance(*b1, *b2)
    # radif = radius difference
    radif = r1 - r2
    if radif < 0:
        radif = -radif
    return betc < radif

print(inside((5, 10), (7, 10), 6, 10))
print(inside((5, 10), (7, 10), 5, 2))
print(inside((5, 10), (17, 10), 4, 6))
print(inside((15, 10), (7, 10), 6, 4))
print(inside((15, 10), (15, 10), 6, 4))
print(inside((15, 10), (15, 10), 6, 6))
