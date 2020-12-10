f = open("day8_data.txt")
data = f.read().split("\n")[0:-1]

been_to = []
acc = 0
i = 0
while i not in been_to:
	instruction = data[i]
	been_to.append(i)
	if instruction.split(" ")[0] == "acc":
		acc += int(instruction.split(" ")[1])
		i += 1
	elif instruction.split(" ")[0] == "jmp":
		i += int(instruction.split(" ")[1])
	elif instruction.split(" ")[0] == "nop":
		i += 1

print(acc)