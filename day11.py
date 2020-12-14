import copy
import numpy as np

with open('day11_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

new_data = copy.deepcopy(data)


def checkState(pos, data):
	i = pos[0]; j = pos[1]

	if data[i][j] == "L":
		for x in [i - 1, i, i + 1]:
			for y in [j - 1, j, j + 1]:
				if x < len(data) and y < len(data[0]) and x >= 0 and y >= 0 and not (x == i and y == j):
					if data[x][y] == "#":
						return "L"
		return "#"

	elif data[i][j] == "#":

		count = 0
		for x in [i - 1, i, i + 1]:
			for y in [j - 1, j, j + 1]:
				if x < len(data) and y < len(data[0]) and x >=0 and y >= 0 and not (x == i and y == j):
					if data[x][y] == "#":
						count += 1
		if count >= 4:
			return "L"
		else:
			return "#"

	else:
		return "."

def compareTo(data1, data2):
	if len(data2[0]) == 0:
		return False
	for x in range(len(data1)):
		for y in range(len(data1[0])):
			if data1[x][y] != data2[x][y]:
				return False
	return True


prev = []

while new_data != prev:
	
	print("Current new data: ", new_data)
	print(prev)
	prev = copy.deepcopy(new_data)

	for i, row in enumerate(data):
		string = list(new_data[i])
		for j, col in enumerate(row):
			string[j] = checkState([i, j], prev)
		new_data[i] = ''.join(string)


	print("Current new data 2: ", new_data)
	print(prev)
	print()
	
answer = 0

for row in new_data:
	for col in row:
		if col == "#":
			answer += 1

print(answer)










