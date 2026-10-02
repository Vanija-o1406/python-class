alerts = ["L2", "L8"]

print(alerts)

alerts.append("L5")
print("Updated list:", alerts)

alerts.insert(1, "L1")
print("After insert:", alerts)

alerts.remove("L8")
print("Final alerts:", alerts)

# ----------------------------------------

data = [5, 10, 15]
same_data = data
separate_data = data.copy()

same_data.append(20)
separate_data.append(50)

print("data:", data)
print("same_data:", same_data)
print("separate_data:", separate_data)

print("same_data is data:", same_data is data)
print("separate_data is data:", separate_data is data)

# ----------------------------------------

measurements = [18, -1, 25, -1, 31, -1]

valid_measurements = [value for value in measurements if value != -1]

print("Valid measurements:", valid_measurements)

# ----------------------------------------

values = [8, 19, 32, 44, 57]

converted = [value + 5 for value in values]
large_values = [value for value in values if value >= 40]

print("Converted:", converted)
print("Large values:", large_values)