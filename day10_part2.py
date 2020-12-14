import copy

with open('day10_data.txt') as f:
	data = [int(line.strip('\n')) for line in f.readlines()]

data.sort()

data.insert(0, 0)

diff3 = 0
diff1 = 0

count = 1

def getToEnd(num, data):

	if num not in data:
		return 0
	if num == max(data):
		return 1

	return getToEnd(num + 1, data) + getToEnd(num + 2, data) \
			 + getToEnd(num + 3, data)

paths = {}
total = 0

class Tree:
	def __init__(self, num, data):
		global total
		global paths
		self.val = num
		self.count = 0
		if num not in data:
			self.val = -1
		elif num != max(data):
			if num in paths.keys():
				self.node1 = paths[num].node1
				self.node2 = paths[num].node2
				self.node3 = paths[num].node3
			else:
				self.node1 = Tree(num + 1, data)
				self.node2 = Tree(num + 2, data)
				self.node3 = Tree(num + 3, data)
				paths[num] = self
			self.count += self.node1.count + self.node2.count + self.node3.count
		else:
			self.count += 1


def countLeaves(tree, data):

	if tree.val == -1:
		return 0
	if tree.val == max(data):
		return 1
	return countLeaves(tree.node1, data) + countLeaves(tree.node2, data) + \
		   countLeaves(tree.node3, data)

tree = Tree(0, data)
print("Finished making tree")
print(tree.count)


	