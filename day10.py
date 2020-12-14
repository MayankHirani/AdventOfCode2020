with open('day10_data.txt') as f:
	data = [int(line.strip('\n')) for line in f.readlines()]

data.sort()

data.insert(0, 0)

diff3 = 0
diff1 = 0

for i, adapter in enumerate(data):
	print(adapter)
	if (i == len(data) - 1 or adapter + 3 == data[i+1]):
	
		diff3 += 1
	elif (adapter + 1 == data[i+1]):
		diff1 += 1
		print("Diff 1")

print(diff3 * diff1)
