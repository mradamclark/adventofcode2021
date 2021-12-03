#!/usr/bin/python

inputfile = 'puzzleInput.txt'

def get_most_common_bit(position, bin_data, default_if_even):
    total = len(bin_data)
    ones = 0
    for s in bin_data:
        if s[position] == '1':
            ones += 1
    zeros = total - ones
    if (ones > zeros):
        return '1'
    elif ones < zeros:
        return '0'
    else:
        return default_if_even
    
def get_least_common_bit(position, bin_data, default_if_even):
    total = len(bin_data)
    ones = 0
    for s in bin_data:
        if s[position] == '1':
            ones += 1
    zeros = total - ones
    if (ones < zeros):
        return '1'
    elif ones > zeros:
        return '0'
    else:
        return default_if_even
        
    
def filter(getbit, default_if_even, bin_data, pos = 0):
    if len(bin_data) == 1:
        return bin_data.pop(0)
    else:
        new_bin_data = []
        bit = getbit(pos, bin_data, default_if_even)
        for number in bin_data:
            if number[pos] == bit:
                new_bin_data.append(number)
        return filter(getbit, default_if_even, new_bin_data, pos + 1)

with open(inputfile) as file:
    bin_data = [line.strip() for line in file]

# totals = [0] * len(bin_data[0])
# for line in bin_data:
#     s = list(line)
#     for i in range(len(s)):
#         totals[i] += int(s[i])

# for count in totals:
#     if count < (len(bin_data) - count):
#         gamma_rate += "0"
#         epsilon_rate += "1"
#     else:
#         gamma_rate += "1"
#         epsilon_rate += "0"

gamma_rating = [] 
epsilon_rating = [] 
      
for i in range(len(bin_data[0])):
    gamma_rating.append(get_most_common_bit(i, bin_data, '1'))
    epsilon_rating.append(get_least_common_bit(i, bin_data, '0'))
    
oxy_rating = int(filter(get_most_common_bit, '1', bin_data),2)
co2_rating = int(filter(get_least_common_bit, '0', bin_data),2)

gamma_rating = int(''.join(gamma_rating),2)
epsilon_rating = int(''.join(epsilon_rating),2)
print('Power: ' + str(gamma_rating * epsilon_rating))
print("Life Support Rating: " + str(oxy_rating * co2_rating))