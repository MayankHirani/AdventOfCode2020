f = open("day8_data.txt")
data = f.read().split("\n")[0:-1]

switch = 0
for j, test in enumerate(data):
	original = test + ""

	if test.split(" ")[0] == "nop":
		data[j] = "jmp " + test.split(" ")[1]

	elif test.split(" ")[0] == "jmp":
		data[j] = "nop " + test.split(" ")[1]

	been_to = []
	i = 0
	acc = 0
	found = False
	while i not in been_to:
		if (i >= len(data)):
			found = True
			print(test)
			switch = j
			break

		instruction = data[i]
		been_to.append(i)
		if instruction.split(" ")[0] == "acc":
			acc += int(instruction.split(" ")[1])
			i += 1
		elif instruction.split(" ")[0] == "jmp":
			i += int(instruction.split(" ")[1])
		elif instruction.split(" ")[0] == "nop":
			i += 1
	
	data[j] = original

	if found:
		print(acc)
