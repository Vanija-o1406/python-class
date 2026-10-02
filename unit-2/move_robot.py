def save_coordinate(coordinate, points=None):
    if points is None:
        points = []

    points.append(coordinate)
    return points


first_route = save_coordinate((2, 4))
second_route = save_coordinate((7, 9))

print("first route:", first_route)
print("second route:", second_route)
print("same list?", first_route is second_route)