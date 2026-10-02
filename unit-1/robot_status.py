machine = {
    "id": "Rover-3",
    "charge": 84,
    "status": "standby"
}

print(machine)
print(machine["id"])

machine["charge"] -= 7
machine["velocity"] = 0.6

print(machine)
print("Keys:", list(machine.keys()))
print("Values:", list(machine.values()))

# ----------------------------------------

device = {
    "id": "Rover-3",
    "charge": 84
}

print(device.get("temperature"))
print(device.get("temperature", 25.0))
print("temperature" in device)

# ----------------------------------------

events = ["W1", "W3", "W1", "W5", "W3", "W1"]

counts = {}

for event in events:
    counts[event] = counts.get(event, 0) + 1

print(counts)

for event in sorted(counts, key=counts.get):
    print(f"{event} occurred {counts[event]} time(s)")

# ----------------------------------------

name = "mufeed"
letter_count = {}

for letter in name:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for letter in sorted(letter_count, key=letter_count.get, reverse=True):
    print(f"{letter} occurred {letter_count[letter]} time(s)")

most_common = max(letter_count, key=letter_count.get)
print("Most frequent letter:", most_common)