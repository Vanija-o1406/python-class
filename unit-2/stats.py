def summarize(data):
    average = sum(data) / len(data)
    return average, min(data), max(data)


temperatures = [19.6, 21.4, 20.2, 23.7, 22.1]

result = summarize(temperatures)
print("statistics:", result)
print("result type:", type(result))


def announce(robot):
    print("Robot ready:", robot)


answer = announce("Rover")
print("function result:", answer)
print("result type:", type(answer))


def divide_values(first, second):
    if second == 0:
        return None
    return first / second


print("8 / 4 =", divide_values(8, 4))
print("8 / 0 =", divide_values(8, 0))


def record_value(values, number):
    values.append(number)


sensor_values = [5, 15]
record_value(sensor_values, 25)
print("updated values:", sensor_values)


def replace_values(values):
    values = [100, 200]
    return values


original_values = [5, 15]
new_values = replace_values(original_values)

print("original:", original_values)
print("replacement:", new_values)


def path_length(route):
    distance = 0

    for index in range(len(route) - 1):
        x_start, y_start = route[index]
        x_end, y_end = route[index + 1]

        dx = x_end - x_start
        dy = y_end - y_start

        distance += (dx ** 2 + dy ** 2) ** 0.5

    return distance


route = [(1, 1), (4, 5)]
length = path_length(route)

print("route length:", length)
print("next value:", length + 2 if length is not None else "no distance available")