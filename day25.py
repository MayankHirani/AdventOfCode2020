
a = 14012298
b = 74241

def findLoopSize(num):
	loops = 0
	val = 1
	while val != num:
		loops += 1
		val *= 7
		val %= 20201227
		# print(val)
	return loops

def transform(num, loops):
	val = 1
	for x in range(loops):
		val *= num
		val %= 20201227
	return val

# print(findLoopSize(14012298))
print(transform(a, findLoopSize(b)))