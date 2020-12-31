
data = [15,12,0,14,3,1]

nums = {}

lastSpoken = 0
for turn in range(1, 2021):

	if turn <= len(data):
		if turn > 1:
			nums[lastSpoken] = [turn - 1]
		lastSpoken = data[turn - 1]
			
	else:
		if lastSpoken not in nums.keys():
			nums[lastSpoken] = [turn - 1]
			lastSpoken = 0
		elif len(nums[lastSpoken]) == 1:
			
			nums[lastSpoken].append(turn - 1)
			lastSpoken = nums[lastSpoken][-1] - nums[lastSpoken][-2]
			
		else:
			nums[lastSpoken].append(turn - 1)
			lastSpoken = nums[lastSpoken][-1] - nums[lastSpoken][-2]
			


print(lastSpoken)
