with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day1/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

current_digit = 50
counter = 0
for input in input_data:
    if input[0] == 'L':
        current_digit -= int(input[1:])
    elif input[0] == 'R':
        current_digit += int(input[1:])
    
    while current_digit < 0:
        current_digit += 100
    while current_digit > 99:
        current_digit -= 100
    
    if current_digit == 0:
        counter += 1

print(counter)
