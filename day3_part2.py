with open('day3_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]
total_count = 1
movements = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for movement in movements:
	i = 0
	j = 0
	count = 0
	while i < len(data):
		if (data[i][j] == "#"):
			count += 1
		i += movement[1]
		j += movement[0]
		j = j % len(data[0])
	total_count *= count
print(total_count)