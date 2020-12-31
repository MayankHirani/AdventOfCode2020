with open('day3_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]
count = 0
i = 0
j = 0
while i < len(data):
	if (data[i][j] == "#"):
		count += 1
	i += 1
	j += 3
	j = j % len(data[0])
print(count)
