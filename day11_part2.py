import copy
import numpy as np

with open('day11_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

new_data = copy.deepcopy(data)

def checkOk(x, y, i, j, data):
	if x < len(data) and y < len(data[0]) and x >=0 and y >= 0 and not (x == i and y == j):
		return True
	else:
		return False

def checkState(pos, data):
	i = pos[0]; j = pos[1]

	if data[i][j] == "L":
		for x in range(i + 1, len(data)):
			if checkOk(x, j, i, j, data) and data[x][j] != ".":
				if data[x][j] == "#":
					return "L"
				else:
					break
		for y in range(j + 1, len(data[0])):
			if checkOk(i, y, i, j, data) and data[i][y] != ".":
				if data[i][y] == "#":
					return "L"
				else:
					break
		for x in range(i - 1, -1, -1):
			if checkOk(x, j, i, j, data) and data[x][j] != ".":
				if data[x][j] == "#":
					return "L"
				else:
					break
		for y in range(j - 1, -1, -1):
			if checkOk(i, y, i, j, data) and data[i][y] != ".":
				if data[i][y] == "#":
					return "L"
				else:
					break
		# Diagonals
		coord = [i - 1, j - 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				return "L"
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] - 1, coord[1] - 1]
		coord = [i - 1, j + 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				return "L"
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] - 1, coord[1] + 1]
		coord = [i + 1, j + 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				return "L"
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] + 1, coord[1] + 1]
		coord = [i + 1, j - 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				return "L"
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] + 1, coord[1] - 1]
		return "#"



	elif data[i][j] == "#":

		count = 0
		
		for x in range(i + 1, len(data)):
			if checkOk(x, j, i, j, data) and data[x][j] != ".":
				if data[x][j] == "#":
					count += 1
				break
		for y in range(j + 1, len(data[0])):
			if checkOk(i, y, i, j, data) and data[i][y] != ".":
				if data[i][y] == "#":
					count += 1
				break
		for x in range(i - 1, -1, -1):
			if checkOk(x, j, i, j, data) and data[x][j] != ".":
				if data[x][j] == "#":
					count += 1
				break
		for y in range(j - 1, -1, -1):
			if checkOk(i, y, i, j, data) and data[i][y] != ".":
				if data[i][y] == "#":
					count += 1
				break
		# Diagonals
		coord = [i - 1, j - 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				count += 1
				break
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] - 1, coord[1] - 1]
		coord = [i - 1, j + 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				count += 1
				break
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] - 1, coord[1] + 1]
		coord = [i + 1, j + 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				count += 1
				break
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] + 1, coord[1] + 1]
		coord = [i + 1, j - 1]
		while checkOk(coord[0], coord[1], i, j, data):
			if data[coord[0]][coord[1]] == "#":
				count += 1
				break
			elif data[coord[0]][coord[1]] == "L":
				break
			coord = [coord[0] + 1, coord[1] - 1]

		if count >= 5:
			return "L"
		else:
			return "#"

	else:
		return "."

prev = []

while new_data != prev:
	
	print("\nData")
	for x in new_data:
		print(x)

	prev = copy.deepcopy(new_data)

	for i, row in enumerate(data):
		string = list(new_data[i])
		for j, col in enumerate(row):
			string[j] = checkState([i, j], prev)
		new_data[i] = ''.join(string)



	
answer = 0
for row in new_data:
	for col in row:
		if col == "#":
			answer += 1

print(answer)








