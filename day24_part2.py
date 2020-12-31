import copy

with open('day24_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

blackTiles = set()
def findLocation(coord, path):
	global blackTiles
	if len(path) == 0:
		return coord
	else:
		if path[0:1] == "e":
			return findLocation((coord[0] + 1, coord[1]), path[1:])
		elif path[0:1] == "w":
			return findLocation((coord[0] - 1, coord[1]), path[1:])
		elif path[0:2] == "se":
			return findLocation((coord[0] + 0.5, coord[1] - 1), path[2:])
		elif path[0:2] == "sw":
			return findLocation((coord[0] - 0.5, coord[1] - 1), path[2:])
		elif path[0:2] == "nw":
			return findLocation((coord[0] - 0.5, coord[1] + 1), path[2:])
		elif path[0:2] == "ne":
			return findLocation((coord[0] + 0.5, coord[1] + 1), path[2:])

for path in data:
	if findLocation((0, 0), path) in blackTiles:
		blackTiles.remove(findLocation((0, 0), path))
	else:
		blackTiles.add(findLocation((0, 0), path))

# Count the number of black tiles around a tile
def countBlackNearby(coord, blackTiles):
	count = 0
	for tile in blackTiles:
		if tile in [(coord[0] + 1, coord[1]), (coord[0] - 1, coord[1]), \
					(coord[0] + 0.5, coord[1] - 1), (coord[0] - 0.5, coord[1] - 1), \
					(coord[0] - 0.5, coord[1] + 1), (coord[0] + 0.5, coord[1] + 1)]:
			count += 1
	return count

# Get the coordinates of the tiles around the current black tiles
def getSurrounding(blackTiles):
	surrounding = set()
	for coord in blackTiles:
		for s in [(coord[0] + 1, coord[1]), (coord[0] - 1, coord[1]), \
					(coord[0] + 0.5, coord[1] - 1), (coord[0] - 0.5, coord[1] - 1), \
					(coord[0] - 0.5, coord[1] + 1), (coord[0] + 0.5, coord[1] + 1)]:
			surrounding.add(s)
	return surrounding

tiles = []
for day in range(100):
	# Add the tiles around the black tiles and get rid of repeats
	tiles += list(getSurrounding(blackTiles)) + list(blackTiles)
	tiles = set(tiles); tiles = list(tiles)
	print()
	print("Day " + str(day + 1))

	# Do the game of life stuff
	tempBlackTiles = copy.deepcopy(blackTiles)
	for tile in tiles:
		# Black tile
		if tile in blackTiles:
			if countBlackNearby(tile, blackTiles) == 0 or countBlackNearby(tile, blackTiles) > 2:
				tempBlackTiles.remove(tile)
		# White tile
		else:
			if countBlackNearby(tile, blackTiles) == 2:
				tempBlackTiles.add(tile)

	blackTiles = copy.deepcopy(tempBlackTiles)
	print(len(blackTiles))

print("\nAnswer: " + str(len(blackTiles)))