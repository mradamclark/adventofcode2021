#!/usr/bin/python

inputfile = 'puzzleInput.txt'

def count_ones(position, bin_data):
    ones = 0
    for s in bin_data:
        if s[position] == '1':
            ones += 1
    return ones
             
def get_common_bit(position, bin_data, most_common_result, least_common_result):
    ones = count_ones(position, bin_data)
    return most_common_result if ones >= (len(bin_data) - ones) else least_common_result     
    
def filter(most_common_result, least_common_result, bin_data, pos = 0):
    if len(bin_data) == 1:
        return bin_data.pop(0)
    else:
        new_bin_data = []
        bit = get_common_bit(pos, bin_data, most_common_result, least_common_result)
        for number in bin_data:
            if number[pos] == bit:
                new_bin_data.append(number)
        return filter(most_common_result, least_common_result, new_bin_data, pos + 1)

with open(inputfile) as file:
    bin_data = [line.strip() for line in file]

gamma_rating = [] 
epsilon_rating = [] 
      
for i in range(len(bin_data[0])):
    gamma_rating.append(get_common_bit(i, bin_data, '1', '0'))
    epsilon_rating.append(get_common_bit(i, bin_data, '0','1'))
    
oxy_rating = int(filter('1','0',bin_data),2)
co2_rating = int(filter('0','1', bin_data),2)
gamma_rating = int(''.join(gamma_rating),2)
epsilon_rating = int(''.join(epsilon_rating),2)

print('Power: ' + str(gamma_rating * epsilon_rating))
print("Life Support Rating: " + str(oxy_rating * co2_rating))