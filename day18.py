with open('day18_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

answer = 0

def findOp(operation, line):
	return [i for i, char in enumerate(line) if char == operation]

def getNextNum(line, i):
	num = ""
	for char in line[i:]:
		if char not in ["(", ")", "+", "*"]:
			num += char
		else:
			break
	return int(num)

def doOperations(line):
	newLine = line
	# No operations left
	if newLine.find("+") < 0 and newLine.find("*") < 0:
		return line
	# No addition left
	if newLine.count("+") == 0:
		num = str(getNextNum(newLine, 0) * getNextNum(newLine, newLine.find("*") + 1))
		end = len(str(getNextNum(newLine, 0)) + str(getNextNum(newLine, newLine.find("*") + 1))) + 1
		return doOperations(num + newLine[end:])
	# No multiplication left
	elif newLine.count("*") == 0:
		num = str(getNextNum(newLine, 0) + getNextNum(newLine, newLine.find("+") + 1))
		end = len(str(getNextNum(newLine, 0)) + str(getNextNum(newLine, newLine.find("+") + 1))) + 1
		return doOperations(num + newLine[end:])

	# Next one is addition
	elif newLine.find("+") < newLine.find("*"):
		num = str(getNextNum(newLine, 0) + getNextNum(newLine, newLine.find("+") + 1))
		end = len(str(getNextNum(newLine, 0)) + str(getNextNum(newLine, newLine.find("+") + 1))) + 1
		return doOperations(num + newLine[end:])
	# Next one is multiplication
	elif newLine.find("*") < newLine.find("+"):
		num = str(getNextNum(newLine, 0) * getNextNum(newLine, newLine.find("*") + 1))
		end = len(str(getNextNum(newLine, 0)) + str(getNextNum(newLine, newLine.find("*") + 1))) + 1
		return doOperations(num + newLine[end:])

for i, line in enumerate(data):
	line = line.replace(" ", "")
	while line.count("(") > 0:
		parIndex = max(findOp("(", line))
		line = line[0:parIndex] \
			+ doOperations(line[parIndex + 1:findOp(")", line[parIndex:])[0] + len(line[0:parIndex])]) \
			+ line[findOp(")", line[parIndex:])[0] + len(line[0:parIndex]) + 1:]
	answer += int(doOperations(line))

print("\n" + "Answer: " + str(answer))
