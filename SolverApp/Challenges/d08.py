#!/usr/bin/env python

class d08:
    def __init__(self):
        pass

    def solve_p1(self, signals):
        digit_counter = [0] * 10
        for s in signals:
            digits = s[1].split()
            for d in digits:
                match len(d):
                    case 2:
                        digit_counter[1] += 1
                        continue
                    case 4:
                        digit_counter[4] += 1
                        continue
                    case 3:
                        digit_counter[7] += 1
                        continue
                    case 7:
                        digit_counter[8] += 1
                        continue
        
        for i in range(0, len(digit_counter)):
            print('{} : {}'.format(i, digit_counter[i]))
            
        print(sum(digit_counter))   
        

    def solve(self, data):
        signals = [s.split('|') for s in data]
        self.solve_p1(signals)
       

if __name__ == '__main__':
    with open('../../Files/08.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d08()
    solver.solve(data) 

    