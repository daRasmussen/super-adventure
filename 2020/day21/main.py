with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

foods = []
for food in data:
    x = food.index('contains')
    ingredients = food[:x-1].split()
    allergens = food[x+9:-1].split(', ')
    foods.append((ingredients, allergens))

solved = {}
unsolved = {}
for i in range(len(foods)):
    if len(foods[i][1]) == 1:
        current = foods[i][1][0]

        indicies = []
        if current not in solved:
            for j in range(len(foods)):
                if current in foods[j][1] and i != j:
                    indicies.append(j)
            possible_ingredients = foods[i][0]
            for k in indicies:
                combined_ingredients = []
                I = foods[k][0]
                for f in I:
                    if f in possible_ingredients:
                        combined_ingredients.append(f)
                possible_ingredients = combined_ingredients.copy()

            if len(possible_ingredients) == 1:
                solved[current] = possible_ingredients[0]
            else:
                unsolved[current] = possible_ingredients

while len(unsolved) > 0:
    still_unsolved = {}
    for key in unsolved.keys():
        possible_ingredients = []
        for value in unsolved[key]:
            if value not in solved.values():
                possible_ingredients.append(value)
        if len(possible_ingredients) == 1:
            solved[key] = possible_ingredients[0]
        else:
            still_unsolved[key] = possible_ingredients
    unsolved = still_unsolved
count = 0
for ingredients, allergens in foods:
    for i in ingredients:
        if i not in solved.values():
            count += 1
print(count)
