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

print(len(blackTiles))