#!/usr/bin/env python

import re 
from functools import reduce      

class d14:

    def getCrisperSequences(self, lines) -> dict():
        p = '^([A-Z][A-Z]) -> ([A-Z])$'
        rules = {}
        
        for l in lines:
            m = re.findall(p,l)[0]
            rules[m[0]] = m[1]
        
        return rules
    
    def runCrisper(self, polymer, rules, steps) -> str:
        items = list(polymer)
        
        for s in range(steps):
            new_items = [items[0]]
            for i in range(1,len(items)):
                key = ''.join(items[i-1:i+1])
            #    print(key)
                if key in rules:
            #        print(f"{key} -> {rules.get(key)}")
                    new_items.append(rules.get(key))
                new_items.append(items[i])
            #    np = ''.join(new_items)
            #    print(f'inner - {s+1}({len(np)}):{np}')
            items = new_items
            #np = ''.join(items)
            #print(f'{s+1}({len(items)})')
        return(''.join(items))
        
    def getMinMaxFrequency(self, polymer):
        f = {}
        for c in list(polymer):
            f[c] = f[c] + 1 if c in f else 1
        
        min, max = 99999999,0
        for _,v in f.items():
            min = v if v < min else min
            max = v if v > max else max
        
        return min,max
        
    def solve_p1(self, lines) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        new_polymer = self.runCrisper(polymer, rules, 10) 
        least, most = self.getMinMaxFrequency(new_polymer)
        print(least,most)
        return(most-least)
    
    def solve_p2(self, lines) -> int:
        polymer = lines[0]
        sequences = self.getCrisperSequences(lines[2:])
        
        print(polymer)
        print(sequences)
        
  
        return(-1)
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines)))
        # print('p2 = {}'.format(self.solve_p2(lines)))

        
if __name__ == '__main__':
    with open('../../Files/14.test.txt') as file:
            lines = [line.strip() for line in file]
    solver = d14()
    solver.solve(lines)

    