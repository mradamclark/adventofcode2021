#!/usr/bin/python

inputfile = 'puzzleInput.txt'

gamma_rate = ""
epsilon_rate = ""

def get_power_consumption(g,e):
    return g * e

with open(inputfile) as file:
    bin_data = [line.strip() for line in file]

totals = [0] * len(bin_data[0])
for line in bin_data:
    s = list(line)
    for i in range(len(s)):
        totals[i] += int(s[i])

for count in totals:
    if count < (len(bin_data) - count):
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
        
print(int(gamma_rate,2))
print(int(epsilon_rate,2))

print('Answer: ')
print(get_power_consumption(int(gamma_rate,2), int(epsilon_rate,2)))