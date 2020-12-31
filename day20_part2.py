import numpy as np

f = open("day20_data.txt")
data = f.read().split("\n\n")[0:-1]
tiles = {}

for tile in data:
	tiles[int(tile.split(":")[0].split(" ")[1])] = tile.split(":")[1].split("\n")[1:]

for tile in tiles.keys():
	tiles[tile] = np.array([list(i) for i in tiles[tile]])

# Get all edges of a tile, flipped and straight
def findEdges(tile):
	edges = []
	edges.append(tile[0].tolist()); edges.append(tile[0].tolist()[::-1])
	edges.append(tile[-1].tolist()); edges.append(tile[-1].tolist()[::-1])
	left = []; right = []
	for y in tile:
		left.append(y[0])
		right.append(y[-1])
	edges.append(left); edges.append(left[::-1])
	edges.append(right); edges.append(right[::-1])
	return edges

# Find corner pieces
for tile in tiles.keys():
	adjacent = 0
	for tile2 in tiles.keys():
		count = 0
		if tile != tile2:
			for edge in findEdges(tiles[tile]):
				for edge2 in findEdges(tiles[tile2]):
					if edge == edge2:
						count += 1
			if count == 2:
				adjacent += 1
	if adjacent == 2:
		print(tile)


def checkCornerOrientedCorrectly(tile, tiles):
	count = 0
	for t in tiles:
		for edge in [tile[0].tolist(), getLeft(tile).tolist()]:
			if edge in findEdges(t):
				count += 1
	if count == 0:
		return True
	else:
		return False

# Get left edge of tile
def getLeft(tile):
	left = []
	for y in tile:
		left.append(y[0])
	return np.array(left)

def addNextTile(pos, tiles, graph):
	# Its the first one in the row
	nextTile = []
	if pos[1] == 0:
		# tiles.remove(graph[pos[0] - 1][0])
		matchEdge = graph[pos[0] - 1][0][-1]
		for i, tile in enumerate(tiles):
			for edge in findEdges(tile):
				if np.all(edge == matchEdge):
					nextTile = tile
					del tiles[i]

		# Orient it the right way
		for orientation in [nextTile, np.rot90(nextTile, 1), np.rot90(nextTile, 2), \
			np.rot90(nextTile, 3)]:
			if np.all(orientation[0] == matchEdge):
				graph[pos[0]][pos[1]] = orientation
			elif np.all(np.flipud(orientation)[0] == matchEdge):
				graph[pos[0]][pos[1]] = np.flipud(orientation)

	# Finding a tile that matches left hand side of one next to it
	else:
		# tiles.remove(graph[pos[0]][pos[1] - 1].tolist())
		matchEdge = []
		for y in range(10):
			matchEdge.append(graph[pos[0]][pos[1] - 1][y][-1])
		matchEdge = np.array(matchEdge)
		for i, tile in enumerate(tiles):
			for edge in findEdges(tile):
				if np.all(edge == matchEdge):
					nextTile = tile
					del tiles[i]



		# Orient it the right way
		for orientation in [nextTile, np.rot90(nextTile, 1), np.rot90(nextTile, 2), \
			np.rot90(nextTile, 3)]:
			if np.all(getLeft(orientation) == matchEdge):
				graph[pos[0]][pos[1]] = orientation
			elif np.all(getLeft(np.flipud(orientation)) == matchEdge):
				graph[pos[0]][pos[1]] = np.flipud(orientation)



# Graph is where we place each tile one by one
graph = [[[] for x in range(12)] for y in range(12)]
corner = 1061
graph[0][0] = tiles[corner] # A random corner (2521, 2633, 3067, 1061)
del tiles[corner]

# Convert dictionary of tiles to a list because we don't need IDs anymore
tiles = list(tiles.values())



rotate = 1
# Rotate corner piece until it is facing the right direction
while not checkCornerOrientedCorrectly(graph[0][0], tiles):
	graph[0][0] = np.flipud(graph[0][0])
	if rotate % 2 == 0:
		graph[0][0] = np.rot90(graph[0][0], 1)
	rotate += 1

# Add all the tiles correctly into the full map
for y in range(12):
	for x in range(12):
		pos = (y, x)
		# Dont include corner we already have
		if pos == (0, 0):
			continue
		addNextTile(pos, tiles, graph)


# Trim each tile
def trimTile(tile):
	newTile = []
	for row in tile[1:-1]:
		newTile.append(row[1:-1])
	return newTile

for y in range(12):
	for x in range(12):
		graph[y][x] = trimTile(graph[y][x])

# Combine everything into one giant map
MAP = [ ]
for y1, row in enumerate(graph):
	for y2 in range(len(row[0])):
		addRow = [ ]
		for tile in row:
			for item in tile[y2]:
				addRow.append(item)
		MAP.append(addRow)

# Find seamonster
for orientation in [MAP, np.rot90(MAP, 1), np.rot90(MAP, 2), np.rot90(MAP, 3), \
		np.flipud(MAP), np.flipud(np.rot90(MAP, 1)), np.flipud(np.rot90(MAP, 2)), \
		np.flipud(np.rot90(MAP, 3)), np.fliplr(MAP), np.fliplr(np.rot90(MAP, 1)), \
		np.fliplr(np.rot90(MAP, 2)), np.fliplr(np.rot90(MAP, 3))]:
	found = False
	# print(orientation)
	for y in range(96):
		for x in range(96):
			count = 0
			seamonster = [[y, x+18], [y+1, x+0], [y+1, x+5], [y+1, x+6], [y+1, x+11], [y+1, x+12], [y+1, x+17], [y+1, x+18], [y+1, x+19], [y+2, x+1], [y+2, x+4], [y+2, x+7], [y+2, x+10], [y+2, x+13], [y+2, x+16]]
			for coord in seamonster:
				if coord[0] < 96 and coord[1] < 96 and orientation[coord[0]][coord[1]] == "#":
					count += 1
			if count >= len(seamonster):
				found = True
	if found:
		print("Found")
		MAP = orientation
		break

# Turn seamonsters into dots
for y in range(96):
	for x in range(96):
		count = 0
		seamonster = [[y, x+18], [y+1, x+0], [y+1, x+5], [y+1, x+6], [y+1, x+11], [y+1, x+12], [y+1, x+17], [y+1, x+18], [y+1, x+19], [y+2, x+1], [y+2, x+4], [y+2, x+7], [y+2, x+10], [y+2, x+13], [y+2, x+16]]
		for coord in seamonster:
			if coord[0] < 96 and coord[1] < 96 and MAP[coord[0]][coord[1]] == "#":
				count += 1
		if count >= len(seamonster):
			for coord in seamonster:
				MAP[coord[0]][coord[1]] = "."

print(str(MAP[0]))

answer = sum([str(MAP[x]).count('#') for x in range(96)])
print("\nAnswer: " + str(answer))

