#!/usr/bin/env python


class d09:
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

        
        ny = y-1 if y > 0 else 0
        n = self.grid[ny][x]
        
        sy = y+1 if y < self.rows-1 else y
        s = self.grid[sy][x]
        
        ex = x+1 if x < self.cols-1 else x
        e = self.grid[y][ex]
        
        wx = x-1 if x > 0 else 0
        w = self.grid[y][wx]

        if (v <= n and v <= s and v <= e and v <= w):
            return True
        else:
            return False
        
        
        
        
    def solve(self, data):
        self.readIntoGrid(data)
        
        for y in range(self.rows):
            for x in range(self.cols):
                if self.isLowPoint(x,y):
                    self.lowPoints.append((x,y))
        
        print(self.lowPoints)
        lv = []
        for lp in self.lowPoints:
            v = self.grid[lp[1]][lp[0]]
            if v < 9: lv.append(v)
        print(lv)
        
        lv = list(map(lambda x:x+1, lv))
        print(lv)
        print(sum(lv))
        
if __name__ == '__main__':
    with open('../../Files/09.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d09()
    solver.solve(data) 

    