#!/usr/bin/env python

import re 
from time import time     

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

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
    

    splitPairs = lambda s:[s[i-1:i+1] for i in range(1,len(s))]

    def runCrisper2(self, polymer, rules, steps):
        fq = {}
        for c in polymer:
            fq[c] = fq[c] + 1 if c in fq else 1
            
        pairs = d14.splitPairs(polymer)
        for p in pairs: 
                self.process(p,rules, steps, fq)
        return(fq)
    
    def process(self, polymer, rules, steps, fq):
        # print(f"calling with: {polymer} on {steps}")
        if steps == 0:
            return fq
        else:
            # print(f'polymer: {polymer}')
            k = rules.get(polymer) or ''
            fq[k] = fq[k] + 1 if k in fq else 1
            np = polymer[0] + k + polymer[1]
            pairs = d14.splitPairs(np)
            for p in pairs:
                self.process(p,rules, steps-1, fq)
             
    def getMinMaxFrequency(self, polymer):
        f = {}
        for c in list(polymer):
            f[c] = f[c] + 1 if c in f else 1
        
        print(f)
        min, max = 99999999,0
        for _,v in f.items():
            min = v if v < min else min
            max = v if v > max else max
        
        return min,max
      
    @timer_func  
    def solve_p1(self, lines, steps) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        new_polymer = self.runCrisper(polymer, rules, steps) 
        least, most = self.getMinMaxFrequency(new_polymer)
        #print(least,most)
        return(most-least)
       
    @timer_func
    def solve_p1v2(self, lines, steps) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        f = self.runCrisper2(polymer, rules, steps)
        print(f"freq: {f}")
        min, max = 99999999,0
        for _,v in f.items():
            min = v if v < min else min
            max = v if v > max else max

        return(max-min)
        
    @timer_func
    def solve_p2(self, lines) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        new_polymer = self.runCrisper(polymer, rules, 40) 
        least, most = self.getMinMaxFrequency(new_polymer)
        print(least,most)
        return(most-least)
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines, 20)))
        print('p1v2 = {}'.format(self.solve_p1v2(lines, 20)))
        # print('p2 = {}'.format(self.solve_p2(lines)))
        
if __name__ == '__main__':
    with open('../../Files/14.test.txt') as file:
            lines = [line.strip() for line in file]
    solver = d14()
    solver.solve(lines)

    