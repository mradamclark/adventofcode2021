#!/usr/bin/env python

class d08:
    def __init__(self):
        pass

    def solve(self, data):
        starts = [(3,1), (2,2), (2,1), (5,2), (1,1)]
        #starts = [(3,1)]
        
        c = []
        for s in starts:
            r= []
            x,y = 0,0
            while y < len(data):
                x = (s[0] + x) % len(data[y])
                y += s[1]
                if y <= len(data)-1 and data[y][x] == '#':
                    r.append((x,y))
            c.append(len(r))

        print(c)
        print(min(c))
        
      
if __name__ == '__main__':
    with open('../../Files/08.map.txt') as file:
            data = [line.strip() for line in file]
    solver = d08()
    solver.solve(data) 

    