with open('day14_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]


def applyMask(val, mask):
	val = list(val)
	mask = list(mask)
	
	for i, char in enumerate(mask):
		if char != "X":
			val[i] = mask[i]
	return "".join(val)

addresses = {}

for i, m in enumerate(data):
	if m[0:4] == "mask":
		mask = m.split(" ")[2]
		j = i + 1
		while j < len(data) and data[j][0:3] == "mem":
			val = '{0:36b}'.format(int(data[j].split(" ")[2])).replace(" ", "0")
			addresses[data[j][data[j].index("[") + 1:data[j].index("]")]] = applyMask(val, mask)
			j += 1

answer = 0
for key in addresses.keys():
	if int(addresses[key]) > 0:
		answer += int(addresses[key], 2)

print(answer)
		