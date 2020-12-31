import copy

n = [9, 6, 3, 2, 7, 5, 4, 8, 1]
current = 9

# n = [3, 8, 9, 1, 2, 5, 4, 6, 7]
# current = 3

def findNextThree(n, current):
	nextNums = []
	for nextNum in [n.index(current) + 1, n.index(current) + 2, n.index(current) + 3]:
		if nextNum >= len(n):
			nextNum = (nextNum % len(n))
		nextNums.append(n[nextNum])
	return nextNums

for move in range(100):

	# Remove the three next ones
	temp = copy.deepcopy(n)
	for nextN in findNextThree(n, current):
		temp.remove(nextN)

	# Find the destination
	destination = current - 1
	if destination < 1:
		destination = 9
	while destination in findNextThree(n, current) or destination < 1:
		print(destination)
		if destination < 1:
			destination = 9
		else:
			destination -= 1

	# print(destination)

	# Place cups
	for i, nextNum in enumerate(findNextThree(n, current)):
		temp.insert(temp.index(destination) + 1 + i, nextNum)

	n = copy.deepcopy(temp)
	if n.index(current) == 8:
		current = n[0]
	else:
		current = n[n.index(current) + 1]

	print("Final N")
	print(n)
	print()

answer = ""
n = n[n.index(1) + 1:] + n[0:n.index(1)]
for x in n:
	answer += str(x)
print("\nAnswer: " + answer)