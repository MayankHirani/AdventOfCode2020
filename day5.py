with open('day5_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

rows = [i for i in range(128)]
cols = [i for i in range(8)]

maxId = 0

def findRow(seat, rows):
	if seat == "":
		return rows
	if seat[0] == "F":
		return findRow(seat[1:], rows[0:int(len(rows)/2)])
	elif seat[0] == "B":
		return findRow(seat[1:], rows[int(len(rows)/2):])
	else:
		return rows

def findCol(seat, cols):

	if seat == "":
		return cols
	if seat[0] == "L":
		return findCol(seat[1:], cols[0:int(len(cols)/2)])
	elif seat[0] == "R":
		return findCol(seat[1:], cols[int(len(cols)/2):])
	else:
		return cols

for seat in data:
	seatId = findRow(seat[0:7], rows)[0] * 8 + findCol(seat[7:], cols)[0]
	if seatId > maxId:
		maxId = seatId

print(maxId)