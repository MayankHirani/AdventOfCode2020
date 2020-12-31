with open('day4_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

passports = []
index = 0
while index < len(data):
	passport = ""
	for item in data[index:]:
		index += 1

		if (item != ""):
			passport += item + " "
		else:
			break
	passports.append(passport)


count = 0

for passport in passports:
	dict1 = {}
	for thing in passport.split(" "):
		if (thing != ""):
			dict1[thing.split(":")[0]] = thing.split(":")[1]
	if all(x in dict1.keys() for x in ["byr", "pid", "ecl", "hgt", "hcl", "iyr", "eyr"]):
		count += 1
		
	# elif ("cid" not in dict1.keys()) and (all(x in dict1.keys() for x in ["byr", "pid", "ecl", "hgt", "hcl", "pid", "eyr"])):
		# count += 1
	print(all(x in dict1.keys() for x in ["byr", "pid", "ecl", "hgt", "hcl", "pid", "eyr"]))

print(count)
