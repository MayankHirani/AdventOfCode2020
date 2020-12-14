with open('day12_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

# Rotate waypoint around ship
def rotate(ship, waypoint, direction):
	coord = [waypoint[0] - ship[0], waypoint[1] - ship[1]]
	if direction[0] == "L":
		if direction[1:] == "90":
			return [ship[0] - coord[1], ship[1] + coord[0]]
		elif direction[1:] == "180":
			return [ship[0] - coord[0], ship[1] - coord[1]]
		elif direction[1:] == "270":
			return [ship[0] + coord[1], ship[1] - coord[0]]
	elif direction[0] == "R":
		if direction[1:] == "90":
			return [ship[0] + coord[1], ship[1] - coord[0]]
		elif direction[1:] == "180":
			return [ship[0] - coord[0], ship[1] - coord[1]]
		elif direction[1:] == "270":
			return [ship[0] - coord[1], ship[1] + coord[0]]

facing = "E"
waypoint = [10, 1]
ship = [0, 0]

for direction in data:
	op = direction[0]
	if op == "W":
		waypoint[0] = waypoint[0] - int(direction[1:])
	elif op == "E":
		waypoint[0] = waypoint[0] + int(direction[1:])
	elif op == "N":
		waypoint[1] = waypoint[1] + int(direction[1:])
	elif op == "S":
		waypoint[1] = waypoint[1] - int(direction[1:])
	elif op in ["L", "R"]:
		waypoint = rotate(ship, waypoint, direction)
	elif op == "F":
		x = int(direction[1:]) * (waypoint[0] - ship[0])
		y = int(direction[1:]) * (waypoint[1] - ship[1])
		waypoint = [waypoint[0] + x, waypoint[1] + y]
		ship = [ship[0] + x, ship[1] + y]

print(ship)

