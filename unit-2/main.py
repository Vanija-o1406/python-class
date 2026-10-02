import sensors

samples = [58, 76, 91]

print("limit:", sensors.LIMIT)
print("mean:", sensors.calculate_mean(samples))

for sample in samples:
    status = "ALERT" if sensors.check_limit(sample) else "normal"
    print(sample, "->", status)


import sensors

print("main module:", __name__)
print("sensors module:", sensors.__name__)


import sensors
from sensors import check_limit
import sensors as sensor_tools

print(sensors.check_limit(80))
print(check_limit(80))
print(sensor_tools.check_limit(80))


from sensors import *

LIMIT = 40.0

print("local LIMIT:", LIMIT)
print("check_limit(50):", check_limit(50))