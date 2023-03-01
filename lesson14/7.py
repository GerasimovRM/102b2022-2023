def str_point_to_tuple(point):
    x, y = point.split(";")
    return float(x), float(y)


def equation(point1, point2):
    point1 = str_point_to_tuple(point1)
    point2 = str_point_to_tuple(point2)
    dx = point1[0] - point2[0]
    if dx == 0:
        print(point1[0])
        return
    dy = point1[1] - point2[1]
    if dy == 0:
        print(point1[1])
        return
    k = dy / dx
    b = point1[1] - k * point1[0]
    print(k, b)


print(str_point_to_tuple("3.4;3.5"))
equation("0; 0", "4;4")