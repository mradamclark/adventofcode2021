#!/usr/bin/env python


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
        known = {2:1,4:4,3:7,7:8}
        converted_sum = 0
        
        for d in data:
            signals = [''.join(sorted(p)) for p in d[0].split()]
            digits =  [''.join(sorted(p)) for p in d[1].split()]
            
            rm = {}
            m = {}
            for s in signals:
                if len(s) in known:
                    n = known[len(s)]
                    rm[n] = set(s)
                    m[s] = n
            
            print(signals)       
            for s in signals:
                p = set(s)
                if len(s) == 6: # 0,6,9 are the only numbers that have 6 segments
                    if rm[4] & p == rm[4]: 
                        m[s] = 9
                    elif rm[1] & p == rm[1]:
                        m[s] = 0
                    else:
                        m[s] = 6
                if len(s) == 5: # 2,3,5 are the only numbers with 5 segments
                    if rm[1] & p == rm[1]:
                        m[s] = 3
                    elif rm[4] | p == rm[8]:
                        m[s] = 2
                    else:
                        m[s] = 5
                        
            print(m)
            converted_sum += int(''.join([str(m[d]) for d in digits]))
        print(converted_sum)               

    def solve(self, data):
        signals = [s.split('|') for s in data]
        self.solve_p1(signals)
        self.solve_p2(signals)
       

if __name__ == '__main__':
    with open('../../Files/08.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d08()
    solver.solve(data) 

    