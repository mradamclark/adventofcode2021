#!/usr/bin/env python

import re 
from time import time 
from collections import Counter    

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
    
    splitPairs = lambda s:[s[i-1:i+1] for i in range(1,len(s))]
    def polymerize(template, rules, steps):
        pair_freq = Counter(d14.splitPairs(template))
        char_freq = Counter(template)
        
        for _ in range(steps):
            step_freq = Counter()
            for p, f in pair_freq.items():
                if p in rules:
                    step_freq[p[0] + rules[p]] += f
                    step_freq[rules[p] + p[1]] += f
                    char_freq[rules[p]] += f
            pair_freq = step_freq

        return max(char_freq.values()), min(char_freq.values())
    
    @timer_func
    def solve_p1(self, lines) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        most, least = d14.polymerize(polymer, rules, 10)
        return most - least
        
    @timer_func
    def solve_p2(self, lines) -> int:
        polymer = lines[0]
        rules = self.getCrisperSequences(lines[2:])
        most, least = d14.polymerize(polymer, rules, 40)
        return most - least
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines)))
        print('p2 = {}'.format(self.solve_p2(lines)))
        
if __name__ == '__main__':
    with open('../../Files/14.test.txt') as file:
            lines = [line.strip() for line in file]
    solver = d14()
    solver.solve(lines)

    