f = open("day7_data.txt")
data = f.read().split("\n")[0:-1]

bags = {}

for bag in data:
	print()
	print(bag)

	contains = bag.split("bags contain")[0].strip();
	if bag.find("no other") > 0:
		continue
	for x in bag.split(","):
		for i in range(int(x.split(" ")[-4])):

			if contains in bags.keys():
				bags[contains].append(x.split(" ")[-3] + " " + x.split(" ")[-2])
			else:
				bags[contains] = [x.split(" ")[-3] + " " + x.split(" ")[-2]]




total = 0
def count_children(color):
	global total
	if color in bags.keys():
		for child_bag in bags[color]:
			total += 1
			count_children(child_bag)


count_children("shiny gold")
print(total)