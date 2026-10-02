alpha = 11
beta = 27
gamma = 68

for name, level in [("Alpha", alpha), ("Beta", beta), ("Gamma", gamma)]:
    if level < 15:
        status = "CRITICAL"
    elif level < 30:
        status = "LOW"
    else:
        status = "OK"

    print(f"{name}: {status}")


def check_battery(level, robot="Scout"):
    if level < 15:
        print(f"{robot}: CRITICAL")
    elif level < 30:
        print(f"{robot}: LOW")
    else:
        print(f"{robot}: OK")


check_battery(11, "Alpha")
check_battery(27, "Beta")
check_battery(68)


def battery_status(level):
    if level < 15:
        return "critical"
    if level < 30:
        return "low"
    return "ok"


robots = {
    "Scout": 11,
    "Rover": 27,
    "Atlas": 68,
    "Nova": 45
}

for robot, level in robots.items():
    print(f"{robot:<8} {level:>3}% {battery_status(level)}")


def rectangle_area(length):
    print(length * length)


rectangle_area(4)


def rectangle_area(length):
    return length * length


combined_area = rectangle_area(4) + rectangle_area(6)
print("combined:", combined_area)


def navigate(row, column, speed=1.5):
    print(f"Position ({row}, {column}) | Speed: {speed} m/s")


navigate(2, 5)
navigate(2, 5, 0.8)
navigate(column=5, row=2)
navigate(2, speed=2.5, column=5)


def record(*items, **settings):
    print("items:", items)
    print("settings:", settings)


record("boot")
record("move", 2, 6.5)
record("warning", priority="high", attempts=3)
record()


def store_point(point, path=[]):
    path.append(point)
    return path


first_path = store_point((2, 3))
second_path = store_point((7, 8))

print("first path:", first_path)
print("second path:", second_path)
print("shared object:", first_path is second_path)