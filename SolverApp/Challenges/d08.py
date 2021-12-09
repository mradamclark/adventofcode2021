#!/usr/bin/env python

digit_map = ['abcefg', 'cf', 'acdeg','acdfg','bcdf','abdfg','abdfge','acf','abcdefg','acbdfg']
known = {2:1,4:4,3:7,7:8}

class d08:
    def __init__(self):
        pass

    def solve_p1(self, signals):
        total = 0
        for s in signals:
            digits = s[1].split()
            for d in digits:
                if (len(d) in [2,3,4,7]):
                    total += 1
        print(total)
    
    def solve_p2(self, data):
       
        for d in data:
            signals = [''.join(sorted(p)) for p in d[0].split()]
            digits =  [''.join(sorted(p)) for p in d[1].split()]
            print(signals, digits)
                    

    def solve(self, data):
        signals = [s.split('|') for s in data]
        self.solve_p1(signals)
        self.solve_p2(signals)
       

if __name__ == '__main__':
    with open('../../Files/08.test-simple.txt') as file:
            data = [line.strip() for line in file]
    solver = d08()
    solver.solve(data) 

    