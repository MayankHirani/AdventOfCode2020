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

# Remove the ones that do not contain any
for ingredient in ingredients:
	if ingredient not in containsAllergen:
		for i, food in enumerate(data):
			data[i] = food.replace(ingredient + " ", "")

# Make the set of all allergens
allergens = set()
for food in data:
	for allergen in [x.strip(",").strip(")") for x in food.split("(")[1].split(" ")[1:]]:
		allergens.add(allergen)

# Map what allergens each ingredient satisfies
ingredients = {}
for ingredient in containsAllergen:
	ingredients[ingredient] = []
	for allergen in allergens:
		inAll = True
		for food in data:
			if allergen in [x.strip(",").strip(")") for x in food.split("(")[1].split(" ")[1:]]:
				if ingredient not in food.split("(")[0].strip().split(" "):
					inAll = False
					break
		if inAll:
			ingredients[ingredient].append(allergen)

# Check that each ingredient is only attributed to one allergen
def check(ingredients):
	for i in ingredients.keys():
		if len(ingredients[i]) > 1:
			return False
	return True

# Filter it down so each ingredient only has one allergen
while not check(ingredients):
	for i in ingredients.keys():
		if len(ingredients[i]) == 1:
			for j in ingredients.keys():
				if i != j and ingredients[i][0] in ingredients[j]:
					ingredients[j].remove(ingredients[i][0])

# Rearrange so that its keys (allergen) : values (ingredient)
allergens = {}
for i in ingredients.keys():
	allergens[ingredients[i][0]] = i

# Get answer
answer = ""
a = list(allergens.keys())
a.sort()
for i, l in enumerate(a):
	answer += allergens[l]
	if i < len(a) - 1:
		answer += ","

print("\nAnswer: " + answer)