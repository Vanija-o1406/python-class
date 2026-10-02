# Battery drain simulation

battery = 95
elapsed_minutes = 0

while battery > 20:
    battery -= 8
    elapsed_minutes += 1

print(f"Low battery alert after {elapsed_minutes} minutes ({battery}%)")


# Show battery level after every minute
battery = 95
elapsed_minutes = 0

while battery > 20:
    elapsed_minutes += 1
    battery -= 8
    print(f"Minute {elapsed_minutes:2d} -> Battery {battery}%")

print("Alert: battery level is low")


# Validate battery percentage
while True:
    entered = float(input("Enter battery percentage (0-100): "))

    if 0 <= entered <= 100:
        break

    print("Invalid value, try again")

print("Accepted:", entered)


# Countdown
count = 10

while count >= 1:
    print(count)
    count -= 1

print("Lift off!")


# Sum numbers from 1 to 100
number = 1
total = 0

while number <= 100:
    total += number
    number += 1

print("Total from 1 to 100:", total)