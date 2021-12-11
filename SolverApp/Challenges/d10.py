#!/usr/bin/env python
import math

P1 = { ')':3, ']':57, '}':1197, '>':25137 }
P2 = { ')':1, ']':2, '}':3, '>':4 }
OPEN = ['(','[','{','<']
CLOSE = [')',']','}','>']

class d10:
  
    def solve_p1(self, data) -> int:
       
        scores = []
        for d in data:
            syntax = []
           # print(d)
            for c in list(d):
               # print(c)
                if c in OPEN:
                    syntax.append(c)
                   # print(syntax)
                else:
                    i = CLOSE.index(c)
                    e = OPEN[i]
                    p = syntax.pop()
                   # print(i,e,p)
                    if e != p:
                        scores.append(P1[c])
                        break
           # print('---')
        #print(scores)
        return(sum(scores))
    
    def solve_p2(self, data) -> int:
        scores = []
        for d in data:
            syntax = []
            # print(d)
            for c in list(d):
                # print(c)
                if c in OPEN:
                    syntax.append(c)
                    # print(syntax)
                else:
                    i = CLOSE.index(c)
                    e = OPEN[i]
                    p = syntax.pop()
                   # print(i,e,p)
                    if e != p:
                        syntax = []
                        break
            if (len(syntax) > 0):
                score = 0
                for c in reversed(syntax):
                    closing = CLOSE[OPEN.index(c)]
                    score = score * 5 + P2[closing]
                scores.append(score)       
            
        scores = sorted(scores)
        return scores[int(len(scores)/2)]
  
    def solve(self, data):
        print('p1 = {}'.format(self.solve_p1(data)))
        print('')
        print('p2 = {}'.format(self.solve_p2(data)))

        
if __name__ == '__main__':
    with open('../../Files/10.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d10()
    solver.solve(data) 

    