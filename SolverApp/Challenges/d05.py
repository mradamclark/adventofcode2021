#!/usr/bin/python
import re

class grid:
    def __init__(self):
        self.rows, self.cols = (1000, 1000)
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        
    def place_vent(self, s, e): 
        x,y = self.order(s,e)
        path = '({},{}) -> ({},{})'.format(str(x[0]),str(x[1]),str(y[0]),str(y[1]))
        if (x[0] == y[0]):
            #print('vertical ' + path)
            for i in range(x[1],y[1]+1):
                self.grid[i][y[0]] += 1
        
        elif (x[1] == y[1]):
           # print('horizontal ' + path)
            for i in range(x[0],y[0]+1):
                self.grid[y[1]][i] += 1
    
    def order(self, s, e):
        if (s[0] == e[0]):
            if (s[1] > e[1]):
                return e,s
            else:
                return s,e
        else:
            if (s[0] > e[0]):
                return e,s
            else:
                return s,e
    
    def danger_count(self):
        i = 0
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if (self.grid[r][c] > 1):
                    i += 1
        return i
    
    def __str__(self):
        return '\n'.join([str(l) for l in self.grid]) + '\n'

        
class d05:
    def __init__(self):
        pass

    def solve(self, data):
        p = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')
        g = grid()
        for d in data:
            coords = p.findall(d)[0]
            if ((coords[0] == coords[2]) or (coords[1] == coords[3])):
                g.place_vent((int(coords[0]),int(coords[1])),(int(coords[2]),int(coords[3])))
                #print(g)
        
        print('danger count: ' + str(g.danger_count()))


if __name__ == '__main__':
    with open('../../Files/05.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d05()
    solver.solve(data) 

    