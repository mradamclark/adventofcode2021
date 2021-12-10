#!/usr/bin/env python
import math

class d09:
    VISITIED = -1
    PEAK = 9
    
    def __init__(self):
        self.grid = []
        self.lowPoints = []
        self.rows = 0
        self.cols = 0
        pass

    def readIntoGrid(self, data):
        self.grid = [list(map(int,list(w))) for w in data]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
    def isLowPoint(self,x,y):
        v = self.grid[y][x]

        n = self.grid[y-1][x] if y > 0 else 9
        s = self.grid[y+1][x] if y < self.rows-1 else 9
        e = self.grid[y][x+1] if x < self.cols-1 else 9
        w = self.grid[y][x-1] if x > 0 else 9

        if (v < n and v < s and v < e and v < w):
            return True
        else:
            return False
       
    def solve_p1(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.isLowPoint(x,y):
                    self.lowPoints.append((x,y)) 
        print('p1 score: {}'.format(self.lowPointScore(self.lowPoints))) 
                    
    def solve_p2(self):
        basins = []
        for lp in self.lowPoints:
            basin = []
            basin.append(lp)
            basin.append(self.findBasin(lp))
            basins.append(basin)
            
        largests = self.getLargestThree(basins, 3)
        
        for b in largests: 
            print('Basin: {}({}): {}'.format(b[0],len(b[1]),b[1]))
        
        print('p2 score: {}\n'.format(math.prod([len(l[1]) for l in largests])))
     
    def getLargestThree(self, basins, n):
        f,s,t = basins[0], basins[0], basins[0]
        
        for b in basins:
            lenb = len(b[1])
            if lenb > len(f[1]):
                t = s
                s = f
                f = b
            elif lenb > len(s[1]):
                t = s
                s = b
            elif lenb > len(t[1]):
                t = b
        
        return [f,s,t]

       
    def findBasin(self, p):
        c = [p]
        #print(c)
        self.grid[p[1]][p[0]] = -1
        for n in self.getUnvisitedNeighbours(p):
            c.extend(self.findBasin(n))
            #print(c)
        return c
     
    def getUnvisitedNeighbours(self, lp):
        r = lp[1]
        c = lp[0]
        edge = [d09.PEAK,d09.VISITIED]
    
        #print('on {}, checking {}'.format(lp, (c,r-1)))        
        if r - 1 >= 0 and self.grid[r-1][c] not in edge:
            yield (c,r-1)
            
        #print('on {}, checking {}'.format(lp, (c+1,r)))        
        if c + 1 < self.cols and self.grid[r][c+1] not in edge:
            yield (c+1,r)
        
        #print('on {}, checking {}'.format(lp, (c,r+1)))
        if r + 1 < self.rows and self.grid[r+1][c] not in edge:
            yield (c,r+1)
            
        #print('on {}, checking {}'.format(lp, (c-1,r)))
        if c - 1 >= 0 and self.grid[r][c-1] not in edge:
            yield (c-1,r)
            
       
    def lowPointScore(self, points) -> int:
        lv = []
        for lp in points:
            v = self.grid[lp[1]][lp[0]]
            lv.append(v)
        
        lv = list(map(lambda x:x+1, lv))
        return sum(lv)
 
    def solve(self, data):
        self.readIntoGrid(data)
        
        self.solve_p1()
        print('')
        self.solve_p2()

        
if __name__ == '__main__':
    with open('../../Files/09.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d09()
    solver.solve(data) 

    