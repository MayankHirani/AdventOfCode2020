with open('day13_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

buses = data[1]

def checkNum(t, buses):

	for increase, bus in enumerate(buses):
		if bus == "x":
			continue
		else:
			if (t + increase) % int(bus) != 0:
				return False
	return True

def findIncrement(index, buses):
	inc = 1
	for bus in buses:
		if bus != "x":
			inc *= int(bus)
	return inc

t = 1
increment = 1
for index, bus in enumerate(buses.split(",")):
	while not checkNum(t, buses.split(",")[0:index + 1]):
		t += increment
	increment = findIncrement(index, buses.split(",")[0:index + 1])
print(t)



