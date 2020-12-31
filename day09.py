with open('day9_data.txt') as f:
	data = [int(line.strip('\n')) for line in f.readlines()]

def findPair(num, numList):
	for x in numList:
		for y in numList:
			if x + y == num:
				return True
	return False

for i, num in enumerate(data):
	if i > 24:
		if not findPair(num, data[i - 25:i]):
			print(num)
