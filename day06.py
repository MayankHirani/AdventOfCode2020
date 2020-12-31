with open('day6_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

total_sum = 0

index = 0
while index < len(data):
	group = ""
	for item in data[index:]:
		index += 1
		if item == "":
			break
		group += item
	print(group)

	q = set()
	for char in group:
		q.add(char)
	total_sum += len(q)

print(total_sum)
