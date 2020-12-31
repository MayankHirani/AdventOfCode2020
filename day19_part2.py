import itertools

with open('day19_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

r = data[0:data.index('')]
messages = data[data.index('') + 1:]

# Adjust the rules for part 2
r.insert(r.index("8: 42"), "8: 42 | 42 8")
r.remove("8: 42")
r.insert(r.index("11: 42 31"), "11: 42 31 | 42 11 31")
r.remove("11: 42 31")

# Make a dictionary of the rules
rules = {}
for rule in r:
	rules[int(rule.split(":")[0])] = rule[rule.find(":") + 2:]

print("8: " + rules[8])
print("11: " + rules[11])
print("42: " + rules[42])
print("31: " + rules[31])

validMessages = []

# i is the index you are currently making the rules from
def findValidMessages(rules, rule):

	# if rule not in ['"a"', '"b"']:
		# print(rule)

	m = []

	# Base Case
	if rule.find('"') >= 0:
		return [rule.split('"')[1]]

	# 2 Possibility one
	elif rule.find('|') >= 0:
		# 6 values (occurs at 11: 42 31 | 42 11 31)
		# if len(rule.split(" ")) == 6:
		# 	for x in range(1, 6):
		# 		part1 = itertools.product(set(findValidMessages(rules, rules[42])), repeat=x)
		# 		part2 = itertools.product(set(findValidMessages(rules, rules[31])), repeat=x)
		# 		for comb1 in part1:
		# 			for comb2 in part2:
		# 				string = ""
		# 				for t in comb1:
		# 					string += t
		# 				for t in comb2:
		# 					string += t
		# 				m.append(string)
		# 		m = set(m); m = list(m)
		# 		print(x, len(m))
		# 4 values
		if len(rule.split(" ")) == 5:
			use = {1: 0, 2: 1, 3: 3, 4:4}
			for i in [1, 3]:
				for poss1 in set(findValidMessages(rules, rules[int(rule.split(" ")[use[i]])])):
					for poss2 in set(findValidMessages(rules, rules[int(rule.split(" ")[use[i + 1]])])):
						m.append(poss1 + poss2)
		# 5 values (occurs at 8: 42 | 42 8)
		# elif len(rule.split(" ")) == 4:
		# 	for x in range(1, 2):
		# 		for comb in itertools.product(set(findValidMessages(rules, rules[42])), repeat=x):
		# 			string = ""
		# 			for poss in comb:
		# 				string += poss
		# 			m.append(string)
		# 		m = set(m); m = list(m)
		# 		print(x, len(m))
		# 2 values
		else:
			for poss1 in set(findValidMessages(rules, rules[int(rule.split(" ")[0])])):
				m.append(poss1)
			for poss2 in set(findValidMessages(rules, rules[int(rule.split(" ")[2])])):
				m.append(poss2)

	# Add 1, 2, or 3 things together
	else:
		for poss1 in set(findValidMessages(rules, rules[int(rule.split(" ")[0])])):
			if len(rule.split(" ")) == 1:
				m.append(poss1)
			elif len(rule.split(" ")) == 2:
				for poss2 in set(findValidMessages(rules, rules[int(rule.split(" ")[1])])):
					m.append(poss1 + poss2)
			elif len(rule.split(" ")) >= 3:
				for poss2 in set(findValidMessages(rules, rules[int(rule.split(" ")[1])], repitions)):
					for poss3 in set(findValidMessages(rules, rules[int(rule.split(" ")[2])], repitions)):
						m.append(poss1 + poss2 + poss3)

	return m

# ruleEight = set(findValidMessages(rules, rules[8]))
# ruleEleven = set(findValidMessages(rules, rules[11]))

poss42 = set(findValidMessages(rules, rules[42]))
poss31 = set(findValidMessages(rules, rules[31]))

answer = 0
for m, message in enumerate(messages):
	print()
	print(message)
	if message[0:8] not in poss42:
		print("Immediatley didnt work")
		continue

	messageWorks = True
	reached31 = False

	num42 = 0
	num31 = 0
	for i in range(0, len(message) - 7, 8):
		segment = message[i:i+8]
		print(segment)
		if segment in poss42 and not reached31:
			num42 += 1
			print("in 42")
			continue
		elif segment in poss31:
			num31 += 1
			print("in 31")
			reached31 = True
			continue
		else:
			print("in none")
			messageWorks = False
			break
	if messageWorks and reached31 and num42 > num31:
		print("Message Worked")
		answer += 1


	# print()
	# print(m, len(messages))
	# print("Match with: " + message)
	# for eight in ruleEight:
	# 	if message[0:len(eight)] == eight:
	# 		for eleven in ruleEleven:
	# 			if message == eight + eleven:
	# 				answer += 1
	# 				break
	# print("Current Answer: " + str(answer))

print("\nAnswer: " + str(answer))