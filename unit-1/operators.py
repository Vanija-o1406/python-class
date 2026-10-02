heading = 355
turn_amount = 12

wrapped_heading = (heading + turn_amount) % 360

print("Original heading:", heading)
print("Turn amount:", turn_amount)
print("Wrapped heading:", wrapped_heading)
print("Negative angle:", (-45) % 360)


travel_distance = 7.5
maximum_distance = 10

print("Below limit:", travel_distance < maximum_distance)
print("At limit:", travel_distance == maximum_distance)
print("Within range:", 0 <= travel_distance < maximum_distance)

battery_level = 60

print("Distance and battery OK:",
      travel_distance > 5 and battery_level > 20)

print("Either condition OK:",
      travel_distance > 5 or battery_level > 90)

print("Distance above 5:", travel_distance > 5)


distance = 25
battery = 65
is_docked = False

safe_to_move = distance > 10 and battery > 20 and not is_docked

print("Safe to move:", safe_to_move)