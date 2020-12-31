f = open("day22_data.txt")
data = [x.strip() for x in f.read().split("\n\n")]

player1 = [int(x) for x in data[0].split(":")[1].split("\n")[1:]][::-1]
player2 = [int(x) for x in data[1].split(":")[1].split("\n")[1:]][::-1]


def play(player1, player2):
	previous = set()
	while len(player1) > 0 and len(player2) > 0:

		winner = -1
		if (str(player1), str(player2)) in previous:
			return [0, [player1, player2]]
		else:
			previous.add((str(player1), str(player2)))

		if len(player1[:-1]) >= player1[-1] and len(player2[:-1]) >= player2[-1]:
			winner = play(player1[len(player1[:-1]) - player1[-1]:-1], player2[len(player2[:-1]) - player2[-1]:-1])[0]
		elif player1[-1] > player2[-1]:
			winner = 0
		elif player2[-1] > player1[-1]:
			winner = 1

		if winner == 0:
			player1.insert(0, player1[-1]); player1.insert(0, player2[-1])
		elif winner == 1:
			player2.insert(0, player2[-1]); player2.insert(0, player1[-1])

		player1 = player1[:-1]
		player2 = player2[:-1]


	if len(player1) == 0:
		return [1, [player1, player2]]
	elif len(player2) == 0:
		return [0, [player1, player2]]

answer = 0
result = play(player1, player2)
if len(result[1][0]) == 0:
	for i, num in enumerate(result[1][1]):
		answer += num * (i + 1)
	print("\nAnswer: " + str(answer))
else:
	for i, num in enumerate(result[1][0]):
		answer += num * (i + 1)
	print("\nAnswer: " + str(answer))
