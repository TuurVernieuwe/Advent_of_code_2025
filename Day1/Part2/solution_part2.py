with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day1/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

current_digit = 50
counter = 0
was_not_zero = True
for input in input_data:
    for i in range(int(input[1:])):
        if input[0] == 'L':
            current_digit -= 1
        elif input[0] == 'R':
            current_digit += 1
        
        if current_digit < 0:
            current_digit += 100
        if current_digit > 99:
            current_digit -= 100

        if current_digit == 0:
            counter += 1    

print(counter)

