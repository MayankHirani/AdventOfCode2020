f = open("day20_data.txt")
data = f.read().split("\n\n")[0:-1]

tiles = {}

for tile in data:
	tiles[int(tile.split(":")[0].split(" ")[1])] = tile.split(":")[1].split("\n")[1:]

def findEdges(id):
	edges = []
	edges.append(tiles[id][0]); edges.append(tiles[id][-1])
	left = ""
	right = ""
	for y in tiles[id]:
		left += y[0]
		right += y[-1]
	edges.append(left); edges.append(right)

	for i in range(len(edges)):
		edges.append(edges[i][::-1])

	return edges

answer = 1
for tile in tiles.keys():
	count = 0
	for edge in findEdges(tile):
		for compareTile in tiles.keys():
			if edge in findEdges(compareTile) and compareTile != tile:
				count += 1
	if count <= 4:
		print(tile)
		answer *= tile

print(answer)