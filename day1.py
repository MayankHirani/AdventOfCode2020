with open('day1_data.txt') as f:
	data = [int(line.strip('\n')) for line in f.readlines()]
print(data)
for x in range(len(data)):
	for y in range(len(data)):
		if (x != y and data[x] + data[y] == 2020):
			print(data[x] * data[y])
