with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day4/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

input_matrix = []
for input in input_data:
    input_matrix.append(list(input))

number_of_rows = len(input_matrix)
number_of_columns = len(input_matrix[0])
directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

new_matrix = input_matrix
res = 0
still_going = True
while still_going:
    still_going = False
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if input_matrix[row][column] == '@':
                number_of_neigbours = 0
                for direction in directions:
                    if (((row + direction[0]) >= 0) and ((row + direction[0]) < number_of_rows)):
                        if (((column + direction[1]) >= 0) and ((column + direction[1] < number_of_columns))):
                            if input_matrix[row + direction[0]][column + direction[1]] == '@':
                                number_of_neigbours += 1
                if number_of_neigbours < 4:
                    res += 1
                    new_matrix[row][column] = '.'
                    still_going = True
                else:
                    new_matrix[row][column] = '@'
            else:
                new_matrix[row][column] = '.'
    input_matrix = new_matrix

print(res)
