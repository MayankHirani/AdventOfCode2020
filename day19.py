with open('day19_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

r = data[0:data.index('')]
messages = data[data.index('') + 1:]

# Make a dictionary of the rules
rules = {}
for rule in r:
	rules[int(rule.split(":")[0])] = rule[rule.find(":") + 2:]

validMessages = []

# i is the index you are currently making the rules from
def findValidMessages(rules, rule):

	m = []

	# Base Case
	if rule.find('"') >= 0:
		return [rule.split('"')[1]]

	# 2 Possibility one
	elif rule.find('|') >= 0:
		# 4 values
		if len(rule.split(" ")) > 3:
			use = {1: 0, 2: 1, 3: 3, 4:4}
			for i in [1, 3]:
				for poss1 in findValidMessages(rules, rules[int(rule.split(" ")[use[i]])]):
					for poss2 in findValidMessages(rules, rules[int(rule.split(" ")[use[i + 1]])]):
						m.append(poss1 + poss2)
		# 2 values
		else:
			for poss1 in findValidMessages(rules, rules[int(rule.split(" ")[0])]):
				m.append(poss1)
			for poss2 in findValidMessages(rules, rules[int(rule.split(" ")[2])]):
				m.append(poss2)

	# Add 1, 2, or 3 things together
	else:
		for poss1 in findValidMessages(rules, rules[int(rule.split(" ")[0])]):
			if len(rule.split(" ")) == 1:
				m.append(poss1)
			elif len(rule.split(" ")) == 2:
				for poss2 in findValidMessages(rules, rules[int(rule.split(" ")[1])]):
					m.append(poss1 + poss2)
			elif len(rule.split(" ")) >= 3:
				for poss2 in findValidMessages(rules, rules[int(rule.split(" ")[1])]):
					for poss3 in findValidMessages(rules, rules[int(rule.split(" ")[2])]):
						m.append(poss1 + poss2 + poss3)

	return m

m = set(findValidMessages(rules, rules[0]))

answer = 0
for message in messages:
	if message in m:
		answer += 1

# print(m)
print("\nAnswer: " + str(answer))