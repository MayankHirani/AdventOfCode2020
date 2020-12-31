f = open("day22_data.txt")
data = [x.strip() for x in f.read().split("\n\n")]

player1 = [int(x) for x in data[0].split(":")[1].split("\n")[1:]][::-1]
player2 = [int(x) for x in data[1].split(":")[1].split("\n")[1:]][::-1]

while len(player1) > 0 and len(player2) > 0:
	if player1[-1] > player2[-1]:
		player1.insert(0, player1[-1]); player1.insert(0, player2[-1])
	else:
		player2.insert(0, player2[-1]); player2.insert(0, player1[-1])

	player1 = player1[:-1]
	player2 = player2[:-1]

answer = 0
for i, num in enumerate(player1):
	answer += num * (i + 1)

print("\nAnswer: " + str(answer))