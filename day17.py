import copy

with open('day17_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

for x in data:
	print(x)

# Array of layers (z), each is an array of rows (x), each row is an array of points (y)
space = [[["." for x in range(len(data[0]))] for y in range(len(data))]]

for row in range(len(data)):
	for col in range(len(data[0])):
		if data[row][col] == "#":
			space[0][row][col] = "#"



def get(coord, oldSpace):
	return space[coord[0]][coord[1]][coord[2]]

def change(coord, newValue, newSpace):
	newSpace[coord[0]][coord[1]][coord[2]] = newValue

def findNearby(coord, oldSpace):
	nearby = []
	for z in [coord[0] - 1, coord[0], coord[0] + 1]:
		for y in [coord[1] - 1, coord[1], coord[1] + 1]:
			for x in [coord[2] - 1, coord[2], coord[2] + 1]:
				if [z, y, x] != coord and z in range(len(oldSpace)) \
					and y in range(len(oldSpace[0])) \
					and x in range(len(oldSpace[0][0])):
					nearby.append([z, y, x])
	return nearby

def enlargeSpace(space):


	for z in space:
		z.insert(0, ['.' for i in range(len(z[0]))])
		z.append(['.' for i in range(len(z[0]))])
		for y in z:
			y.insert(0, '.')
			y.append('.')

	space.insert(0, [["." for x in range(len(space[0][0]))] for y in range(len(space[0]))])
	space.append([["." for x in range(len(space[0][0]))] for y in range(len(space[0]))])

def changeValues(oldSpace):
	newSpace = copy.deepcopy(oldSpace)
	for z in range(len(oldSpace)):
		for y in range(len(oldSpace[z])):
			for x in range(len(oldSpace[z][y])):
				coord = [z, y, x]
				# print(coord, get(coord, oldSpace))
				nearbyCoords = findNearby(coord, oldSpace)

				if get(coord, oldSpace) == "#":
					count = 0
					for nearbyCoord in nearbyCoords:
						if get(nearbyCoord, oldSpace) == "#":
							count += 1
					if count not in [2, 3]:

						change(coord, ".", newSpace)


				elif get(coord, oldSpace) == ".":
					count = 0
					for nearbyCoord in nearbyCoords:
						if get(nearbyCoord, oldSpace) == "#":
							count += 1
					if count == 3:
						change(coord, "#", newSpace)

				# print(coord, get(coord, newSpace))
				# print()
	return newSpace

def countActive(space):
	count = 0
	for z in range(len(space)):
		for y in range(len(space[z])):
			for x in range(len(space[z][y])):
				if space[z][y][x] == "#":
					count += 1
	return count

for cycle in range(1, 7):

	enlargeSpace(space)

	newSpace = changeValues(space)
	space = copy.deepcopy(newSpace)

	print("Cycle", cycle, ":", countActive(space))
	

