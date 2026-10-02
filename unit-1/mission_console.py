LIMIT = 65.0
measurements = []

while True:
    print("\n1 - Add value")
    print("2 - Show report")
    print("3 - Exit")

    option = input("Select: ")

    if option == "1":
        value = float(input("Enter sensor value: "))
        measurements.append(value)
        print("Value added")

    elif option == "2":
        if len(measurements) == 0:
            print("No readings available")
            continue

        warnings = 0

        for value in measurements:
            if value >= LIMIT:
                warnings += 1

        total = sum(measurements)
        average = total / len(measurements)

        print("Readings:", len(measurements))
        print(f"Average: {average:.2f}")
        print("Warnings:", warnings)

    elif option == "3":
        print("Monitoring stopped")
        break

    else:
        print("Invalid option")