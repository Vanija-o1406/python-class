label = "  Falcon Scout  "

print(f"<{label}>")

clean_label = label.strip()

print(f"<{clean_label}>")
print(clean_label.lower())
print(clean_label.upper())
print(clean_label.replace(" ", "-"))
print("Scout" in clean_label)

packet = "TEMP=28.5|PRESSURE=101.2|VOLTAGE=11.8"

items = packet.split("|")

for item in items:
    name, reading = item.split("=")
    print(name, "->", float(reading))

telemetry = "position=12,45;speed=3.5;battery=82"

records = telemetry.split(";")

for record in records:
    name, data = record.split("=")

    if name == "position":
        coordinates = data.split(",")
        print(name, "->", coordinates)
    else:
        print(name, "->", float(data))