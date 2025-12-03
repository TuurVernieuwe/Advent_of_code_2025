from functools import reduce

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



with open('C:/Users/tuur1/OneDrive/Bureaublad/Advent of code 2025/Advent_of_code_2025/Day2/Inputs/input.txt', 'r') as file:
    input_data = file.read().strip().split(',')


res = 0
for input in input_data:
    ll, ul = list(map(int, input.split('-')))
    
    for i in range(ll, ul+1):
        repeats = False
        s = str(i)
        for factor in factors(len(s)):
            if factor != len(s):
                chunks = [s[j:j+factor] for j in range(0, len(s), factor)]
                if all(chunk == chunks[0] for chunk in chunks):
                    repeats = True
        
        if repeats:
            res += i


print(res)

