temperature = 42.5

if temperature > 40:
    print("Cooling activated")

print("Temperature check complete")


temperature = float(input("Enter enclosure temperature: "))

if temperature < 20:
    operating_mode = "heater on"
elif temperature <= 40:
    operating_mode = "normal"
elif temperature <= 60:
    operating_mode = "cooling"
else:
    operating_mode = "shutdown"

print("Operating mode:", operating_mode)