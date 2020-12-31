f = open("day7_data.txt")
data = f.read().split("\n")[0:-1]

bags = {}
bag_set = set()
for bag in data:
	print()
	print(bag)

	contained_in = bag.split("bags contain")[0].strip();
	for x in bag.split(","):
		if x.split(" ")[-3] + " " + x.split(" ")[-2] in bags.keys():
			bags[x.split(" ")[-3] + " " + x.split(" ")[-2]].append(contained_in)
		else:
			bags[x.split(" ")[-3] + " " + x.split(" ")[-2]] = [contained_in]


def add_ancestors(color):
	if color in bags.keys():
		for contained_in in bags[color]:
			bag_set.add(contained_in)
			add_ancestors(contained_in)


add_ancestors("shiny gold")
print(len(bag_set))
