with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day5/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

ranges = []
available_ingredients = []
blank_reached = False
for input in input_data:
    if input == '':
        blank_reached = True
        continue
    if not blank_reached:
        ranges.append(input)
    else:
        available_ingredients.append(input)

res = 0
for ingredient in available_ingredients:
    ingredient_spoiled = True
    for cur_range in ranges:
        ll, ul = list(map(int, cur_range.split('-')))
        if int(ingredient) in range(ll, ul+1):
            ingredient_spoiled = False
    if not ingredient_spoiled:
        res += 1

print(res)

