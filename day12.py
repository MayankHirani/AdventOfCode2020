with open('day12_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

directions1 = ["E", "S", "W", "N"]
directions2 = ["E", "N", "W", "S"]

facing = "E"
pos = [0, 0]

for direction in data:

	if direction[0] == "F":
		op = facing
	else:
		op = direction[0]

	if op == "W":
		pos[0] = pos[0] - int(direction[1:])
	elif op == "E":
		pos[0] = pos[0] + int(direction[1:])
	elif op == "N":
		pos[1] = pos[1] + int(direction[1:])
	elif op == "S":
		pos[1] = pos[1] - int(direction[1:])
	elif op == "R":
		index = directions1.index(facing)
		for x in range(0, int(direction[1:]), 90):
			index = (index + 1) % 4
			facing = directions1[index]
	elif op == "L":
		index = directions2.index(facing)
		for x in range(0, int(direction[1:]), 90):
			index = (index + 1) % 4
			facing = directions2[index]

print(pos)