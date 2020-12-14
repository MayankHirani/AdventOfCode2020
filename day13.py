import math

with open('day13_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

time = int(data[0])
buses = data[1]

earliest = 9999999999
earliestBus = 0
for bus in buses.split(","):
	if bus != "x":
		if int(bus) * math.ceil(time / int(bus)) < earliest:
			earliest = int(bus) * math.ceil(time / int(bus))
			earliestBus = int(bus)

print((earliest - time) * earliestBus)
