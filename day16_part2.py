import itertools
import copy
import time

start = time.time()
f = open("day16_data.txt")
data = f.read().split("\n\n")[0:]

fields = data[0].split("\n")
nearby = data[2].split("\n")[1:-1]
yourTicket = data[1].split("\n")[1]

def checkNum(num):
	for field in fields:
		ranges = field.split(":")[1].split(" ")[1:]
		if (num >= int(ranges[0].split("-")[0]) and num <= int(ranges[0].split("-")[1])) \
		 or (num >= int(ranges[2].split("-")[0]) and num <= int(ranges[2].split("-")[1])):
		 return 0
	return num

def checkNumInField(num, field):
	f = field.split(":")[1].split(" ")[1:]
	if (num >= int(f[0].split("-")[0]) and num <= int(f[0].split("-")[1])) \
		 or (num >= int(f[2].split("-")[0]) and num <= int(f[2].split("-")[1])):
		 return 0
	else:
		return num



# Remove tickets
new = []
for ticket in nearby:
	bad = False
	for num in ticket.split(","):
		if checkNum(int(num)) != 0:
			bad = True
	if not bad:
		new.append(ticket)
nearby = copy.deepcopy(new)

# Check if a column satisfies a field
def checkColumn(i, field):
	for ticket in nearby:
		if checkNumInField(int(ticket.split(",")[i]), field) != 0:
			return False
	return True

# Make the dictionary
assignment = {}
for i in range(0, 20):
	assignment[i] = []
	for field in fields:
		if checkColumn(i, field):
			assignment[i].append(field)


# Remove a field from every column unless it only appears there once
def removeField(field):
	for i in assignment.keys():
		if field in assignment[i] and len(assignment[i]) != 1:
			assignment[i].remove(field)

# Check that each column only has one field
def checkAssignment():
	for i in assignment.keys():
		if len(assignment[i]) != 1:
			return False
	return True


beenTo = set()
while not checkAssignment():
	for i in assignment.keys():
		if len(assignment[i]) == 1 and i not in beenTo:
			removeField(assignment[i][0])
			beenTo.add(i)
			break

answer = 1
for i in range(0, 20):
	if assignment[i][0].split(" ")[0] == "departure":
		answer *= int(yourTicket.split(",")[i])
print(answer)
print(time.time() - start)