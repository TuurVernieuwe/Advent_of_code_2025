with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day2/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split(',')


res = 0
for input in input_data:
    ll, ul = list(map(int, input.split('-')))
    
    for i in range(ll, ul+1):
        stri = str(i)
        mid = len(stri) // 2
        if (stri[:mid] == stri[mid:]):
            res += i

print(res)

