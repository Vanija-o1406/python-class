def product_to_one(value):
    if value <= 1:
        return 1
    return value * product_to_one(value - 1)


print(product_to_one(6))
print(product_to_one(0), product_to_one(1))


def trace_product(value, level=0):
    spaces = "." * level
    print(f"{spaces}enter: {value}")

    if value <= 1:
        print(f"{spaces}return: 1")
        return 1

    answer = value * trace_product(value - 1, level + 1)
    print(f"{spaces}return: {answer}")
    return answer


trace_product(4)


def launch(count):
    if count < 1:
        print("Go!")
        return

    print(count)
    launch(count - 1)


launch(4)


def fibonacci(position):
    if position < 2:
        return position

    return fibonacci(position - 1) + fibonacci(position - 2)


for position in range(10):
    print(fibonacci(position), end=" ")


def factorial_iterative(number):
    answer = 1

    for value in range(2, number + 1):
        answer *= value

    return answer


def factorial_recursive(number):
    if number < 2:
        return 1

    return number * factorial_recursive(number - 1)


print()
print("Loop:", factorial_iterative(6))
print("Recursion:", factorial_recursive(6))