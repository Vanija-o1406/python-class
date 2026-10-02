robot_id = "Nova-7"
charge_level = 42.5
connected_to_base = False
mission_count = 9

print("Robot:", robot_id)
print("Battery:", charge_level)
print("Connected:", connected_to_base)
print("Missions:", mission_count)

power = 80
print("Initial power:", power)

power = power - 20
print("After movement:", power)

power -= 10
print("After scanning:", power)

charge_level = 42

if charge_level < 50:
    print("Warning: Battery level is low")
    print("Return to base for charging")

print("Robot status check completed")