with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day3/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

res = 0
tmp = 0
for input in input_data:
    number_list = list(input)
    print(number_list)
    twelve_max = max(number_list[:len(number_list)-11])
    twelve_max_idx = idx = number_list.index(twelve_max)
    newlist = number_list[twelve_max_idx+1:]
    print(twelve_max)
    print(newlist)

    eleven_max = max(newlist[:len(newlist)-10])
    eleven_max_idx = idx = newlist.index(eleven_max)
    newlist = newlist[eleven_max_idx+1:]
    print(eleven_max)
    print(newlist)

    ten_max = max(newlist[:len(newlist)-9])
    ten_max_idx = idx = newlist.index(ten_max)
    newlist = newlist[ten_max_idx+1:]
    print(ten_max)
    print(newlist)

    nine_max = max(newlist[:len(newlist)-8])
    nine_max_idx = idx = newlist.index(nine_max)
    newlist = newlist[nine_max_idx+1:]
    print(nine_max)
    print(newlist)

    eight_max = max(newlist[:len(newlist)-7])
    eight_max_idx = idx = newlist.index(eight_max)
    newlist = newlist[eight_max_idx+1:]
    print(eight_max)
    print(newlist)

    seven_max = max(newlist[:len(newlist)-6])
    seven_max_idx = idx = newlist.index(seven_max)
    newlist = newlist[seven_max_idx+1:]
    print(seven_max)
    print(newlist)

    six_max = max(newlist[:len(newlist)-5])
    six_max_idx = idx = newlist.index(six_max)
    newlist = newlist[six_max_idx+1:]
    print(six_max)
    print(newlist)

    five_max = max(newlist[:len(newlist)-4])
    five_max_idx = idx = newlist.index(five_max)
    newlist = newlist[five_max_idx+1:]
    print(five_max)
    print(newlist)

    four_max = max(newlist[:len(newlist)-3])
    four_max_idx = idx = newlist.index(four_max)
    newlist = newlist[four_max_idx+1:]
    print(four_max)
    print(newlist)

    three_max = max(newlist[:len(newlist)-2])
    three_max_idx = idx = newlist.index(three_max)
    newlist = newlist[three_max_idx+1:]
    print(three_max)
    print(newlist)

    two_max = max(newlist[:len(newlist)-1])
    two_max_idx = idx = newlist.index(two_max)
    newlist = newlist[two_max_idx+1:]
    print(two_max)
    print(newlist)

    ones_max = max(newlist)
    print(ones_max)

    res += int(twelve_max)*100000000000 + int(eleven_max)*10000000000 + int(ten_max)*1000000000 + int(nine_max)*100000000 + int(eight_max)*10000000 + int(seven_max)*1000000 + int(six_max)*100000 + int(five_max)*10000 + int(four_max)*1000 + int(three_max)*100 + int(two_max)*10 + int(ones_max)

print(res)

