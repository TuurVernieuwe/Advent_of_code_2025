with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day5/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

string_ranges = []
i = 0
while input_data[i] != '':
    string_ranges.append(input_data[i])
    i += 1

ranges = []
for cur_range in string_ranges:
    ll, ul = list(map(int, cur_range.split('-')))
    ranges.append((ll, ul))

ranges.sort()
merged = []
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end+1:
        cur_end = max(cur_end, end)
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end
merged.append((cur_start, cur_end))
    
res = sum(end - start + 1 for start, end in merged)
print(res)


