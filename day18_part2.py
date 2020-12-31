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

def getLastNum(line, i):
	num = ""
	while i >= 0 and line[i] not in ["(", ")", "+", "*"]:
		num = line[i] + num
		i -= 1
	return [int(num), i + 1]

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

	# Do first addition one
	num = str(getLastNum(newLine, newLine.find("+") - 1)[0] + getNextNum(newLine, newLine.find("+") + 1))
	start = getLastNum(newLine, newLine.find("+") - 1)[1]
	end = newLine.find("+") + len(str(getNextNum(newLine, newLine.find("+") + 1))) + 1
	return doOperations(newLine[0:start] + num + newLine[end:])

for i, line in enumerate(data):
	line = line.replace(" ", "")
	while line.count("(") > 0:
		parIndex = max(findOp("(", line))
		line = line[0:parIndex] \
			+ doOperations(line[parIndex + 1:findOp(")", line[parIndex:])[0] + len(line[0:parIndex])]) \
			+ line[findOp(")", line[parIndex:])[0] + len(line[0:parIndex]) + 1:]
	print(doOperations(line))
	answer += int(doOperations(line))

print("\n" + "Answer: " + str(answer))
