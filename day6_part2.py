with open('day6_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

total_sum = 0

index = 0
while index < len(data):
	group = []
	for item in data[index:]:
		index += 1
		if item == "":
			break
		group.append(item)

	q = {}
	for person in group:
		for char in person:
			if char in q.keys():
				q[char] += 1
			else:
				q[char] = 1
	for char in q.keys():
		if (q[char] == len(group)):
			total_sum += 1

print(total_sum)