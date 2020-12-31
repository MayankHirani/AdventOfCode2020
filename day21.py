import copy

with open('day21_data.txt') as f:
	data = [line.strip('\n') for line in f.readlines()]

# Set of all ingredients
ingredients = set()
for line in data:
	for ingredient in line.split("(")[0].strip().split(" "):
		ingredients.add(ingredient)

# Make a set of all the ingredients that FOR SURE contain an allergen
containsAllergen = set()
for i, food in enumerate(data):
	allergens = [x.strip(",").strip(")") for x in food.split("(")[1].split(" ")[1:]]
	for ingredient in food.split("(")[0].strip().split(" "):
		# For each allergen, check if this ingredient appears in every food
		# with that allergen, if so, add it to the ones that have
		for allergen in allergens:
			found = True
			for j, food2 in enumerate(data):
				allergens2 = [x.strip(",").strip(")") for x in food2.split("(")[1].split(" ")[1:]]
				if i != j and allergen in allergens2:
					if ingredient not in food2.split("(")[0].strip().split(" "):
						found = False
						break
			if found:
				containsAllergen.add(ingredient)

def countAppearences(ingredient):
	count = 0
	for food in data:
		if ingredient in food.split("(")[0].strip().split(" "):
			count += 1
	return count

answer = 0
for ingredient in ingredients:
	if ingredient not in containsAllergen:
		answer += countAppearences(ingredient)

print("\nAnswer: " + str(answer))