battery_percent = int(input("Enter battery percentage: "))
print("Battery after charging:", battery_percent + 10)

robot_name = "Nova"
battery_level = 78.456

print("Robot", robot_name, "at", battery_level, "%")
print(f"Robot {robot_name} at {battery_level}%")
print(f"Robot {robot_name} at {battery_level:.1f}%")
print(f"{robot_name:<10} | {battery_level:>6.2f}%")


capacity = float(input("Enter battery capacity (mAh): "))
current = float(input("Enter current drawn by the robot (mA): "))

estimated_hours = capacity / current

print(f"Estimated runtime: {estimated_hours:.2f} hours")