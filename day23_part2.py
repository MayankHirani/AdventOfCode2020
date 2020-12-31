import copy

n = [9, 6, 3, 2, 7, 5, 4, 8, 1] + [x for x in range(10, 1000001)]
current = 9

# n = [3, 8, 9, 1, 2, 5, 4, 6, 7] + [x for x in range(10, 1000001)]
# current = 3

def printN(d):
	a = []
	start = 9
	i = d[start]
	a.append(start);
	while i != start:
		a.append(i)
		i = d[i]
	print(a)

d = {}
for i in range(len(n)):
	if i == len(n) - 1:
		d[n[i]] = n[0]
	else:
		d[n[i]] = n[i + 1]

for move in range(10000000):
	print()
	print("Move: " + str(move + 1))
	# printN(d)
	destination = current - 1
	if destination < 1:
		destination = max(d.keys())
	nextThree = [d[current], d[d[current]], d[d[d[current]]]]
	while destination in nextThree or destination < 1:
		if destination < 1:
			destination = max(d.keys())
		else:
			destination -= 1
	print("Destination: " + str(destination) + " | " + "Current: " + str(current))

	# Change the three values
	temp = d[destination]
	tempNext = d[d[d[d[current]]]]
	d[destination] = nextThree[0]
	d[d[d[d[current]]]] = temp

	# Change the current
	d[current] = tempNext
	current = tempNext

answer = d[1] * d[d[1]]
print("\nAnswer: " + str(answer))
