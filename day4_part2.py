import string
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

		byr = dict1["byr"]
		iyr = dict1["iyr"]
		pid = dict1["pid"]
		ecl = dict1["ecl"]
		hgt = dict1["hgt"]
		hcl = dict1["hcl"]
		eyr = dict1["eyr"]

		if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002 \
			and len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020 \
			and len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030 \
			and (hgt.find("cm") > 0 or hgt.find("in") > 0) \
			and hcl[0] == "#" and len(hcl[1:]) == 6 \
			and ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] \
			and pid.isnumeric() and len(pid) == 9:
			good = True

			for char in hcl[1:]:
				if (char not in [str(i) for i in range(10)]) and (char not in string.ascii_lowercase[0:6]):
					good = False

			
			if hgt.find("cm") < 0 and hgt.find("in") < 0:
				good = False
			elif hgt.find("cm") > 0:
				if not((int(hgt[0:hgt.find("c")])) >= 150 and int(hgt[0:hgt.find("c")]) <= 193):
					
					good = False
			elif hgt.find("in") > 0:
				if not((int(hgt[0:hgt.find("i")])) >= 59 and (int(hgt[0:hgt.find("i")])) <= 76):
					good = False
			
			if good:
				count += 1



print(count)