f = open("day16_data.txt")
data = f.read().split("\n\n")[0:]

fields = data[0].split("\n")
nearby = data[2].split("\n")[1:-1]

def checkNum(num):
	for field in fields:
		ranges = field.split(":")[1].split(" ")[1:]
		if (num >= int(ranges[0].split("-")[0]) and num <= int(ranges[0].split("-")[1])) \
		 or (num >= int(ranges[2].split("-")[0]) and num <= int(ranges[2].split("-")[1])):
		 return 0
	return num

count = 0
answer = 0
for ticket in nearby:
	for num in ticket.split(","):
		answer += checkNum(int(num))
		if checkNum(int(num)) != 0:
			count += 1

print(answer)
print(count)