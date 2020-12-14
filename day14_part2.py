import copy

with open('day14_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

def applyMask(val, mask):
	val = list(val)
	mask = list(mask)
	
	for i, char in enumerate(mask):
		if char == "X" or char == "1":
			val[i] = char
	return "".join(val)

# Val added as list
def generatePossibilities(val, i, array):
	v = copy.deepcopy(val)
	if i == len(v):
		array.append("".join(v))
	else:
		if v[i] == "X":
			v[i] = "0"; generatePossibilities(v, i + 1, array)
			v[i] = "1"; generatePossibilities(v, i + 1, array)
		else:
			generatePossibilities(v, i + 1, array)

addresses = {}

# Main iteration of creating the address dictionary
for i, m in enumerate(data):
	if m[0:4] == "mask":
		mask = m.split(" ")[2]
		# print("\n" + mask)
		j = i + 1
		while j < len(data) and data[j][0:3] == "mem":
			val = '{0:36b}'.format(int(data[j].split(" ")[2])).replace(" ", "0")
			address = '{0:36b}'.format(int(data[j][data[j].index("[") + 1:data[j].index("]")])).replace(" ", "0")
			arr = []
			generatePossibilities(list(applyMask(address, mask)), 0, arr)
			for address in arr:
				addresses[address] = val
			j += 1

# Count at end
answer = 0
for key in addresses.keys():
	if int(addresses[key]) > 0:
		answer += int(addresses[key], 2)

print(answer)
		