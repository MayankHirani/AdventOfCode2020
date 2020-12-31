with open('day9_data.txt') as f:
	data = [int(line.strip('\n')) for line in f.readlines()]

val = data[0]

def findPair(num, numList):
	for x in numList:
		for y in numList:
			if x + y == num:
				return True
	return False

for i, num in enumerate(data):
	if i > 24:
		if not findPair(num, data[i - 25:i]):
			val = num

for length in range(2, len(data) - 1):
	for start in range(0, len(data) - length + 1):
		if sum(data[start:start + length]) == val:
			print("Answer:", max(data[start:start+length]) + min(data[start:start+length]))
			break
