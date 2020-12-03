with open('day2_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]
	
count = 0
for password in data:
	a = int(password.split("-")[0])
	b = int(password.split("-")[1].split(" ")[0])
	pw = password.split(" ")[2]
	letter = password.split(" ")[1].strip(":")

	if (pw[a - 1] == letter) ^ (pw[b-1] == letter):
		count += 1
print(count)