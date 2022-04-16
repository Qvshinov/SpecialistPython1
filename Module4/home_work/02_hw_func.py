# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def min_distance(p1, p2, p3):
    # d1 = distance(p1[0], p1[0], p2[0], p2[1])
    ab = distance(*p1, *p2)
    bc = distance(*p2, *p3)
    ac = distance(*p1, *p3)
    min_d = ""
    if ab <= bc and ab <= ac:
        min_d = "AB"
    else:
        if bc <= ab and bc <= ac:
            min_d = "BC"
        else:
            if ac <= bc and ac <= ab:
                min_d = "AC"
    return min_d
print("Самый короткий отрезок:", min_distance((1, 12), (5, 12), (7, 12)))  # Выводим название отрезка, например “АС”.
