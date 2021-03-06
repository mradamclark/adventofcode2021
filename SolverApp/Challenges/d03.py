#!/usr/bin/env python

ONE_BIT = '1'
ZERO_BIT = '0'

class d03:
    def __init__(self):
        pass

    def count_ones(self, position, bin_data):
        ones = 0
        for s in bin_data:
            if s[position] == ONE_BIT:
                ones += 1
        return ones
                
    def get_common_bit(self, position, bin_data, most_common_result, least_common_result):
        ones = self.count_ones(position, bin_data)
        return most_common_result if ones >= (len(bin_data) - ones) else least_common_result     
        
    def filter(self, most_common_result, least_common_result, bin_data, pos = 0):
        if len(bin_data) == 1:
            return bin_data.pop(0)
        else:
            bit = self.get_common_bit(pos, bin_data, most_common_result, least_common_result)
            new_bin_data = [num for num in bin_data if num[pos] == bit]
            return self.filter(most_common_result, least_common_result, new_bin_data, pos + 1)

    def solve(self, bin_data):

        gamma_rating = [] 
        epsilon_rating = [] 
            
        for i in range(len(bin_data[0])):
            gamma_rating.append(self.get_common_bit(i, bin_data, ONE_BIT, ZERO_BIT))
            epsilon_rating.append(self.get_common_bit(i, bin_data, ZERO_BIT, ONE_BIT))
            
        oxy_rating = int(self.filter(ONE_BIT, ZERO_BIT, bin_data),2)
        co2_rating = int(self.filter(ZERO_BIT, ONE_BIT, bin_data),2)
        gamma_rating = int(''.join(gamma_rating),2)
        epsilon_rating = int(''.join(epsilon_rating),2)

        print('P1 - Power: ' + str(gamma_rating * epsilon_rating))
        print('P2 - Life Support Rating: ' + str(oxy_rating * co2_rating))

if __name__ == '__main__':
    with open('../Files/03.input.txt') as file:
            bin_data = [line.strip() for line in file]
    solver = d03()
    solver.solve(bin_data)
    