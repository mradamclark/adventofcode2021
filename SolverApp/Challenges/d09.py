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
                    
    def solve_p2(self):
        pass         
       
    def score_cluster(self, points) -> int:
        lv = []
        for lp in points:
            v = self.grid[lp[1]][lp[0]]
            lv.append(v)
        
        lv = list(map(lambda x:x+1, lv))
        return sum(lv)
 
    def solve(self, data):
        self.readIntoGrid(data)
        
        self.solve_p1()
        print('p1 score: {}'.format(self.score_cluster(self.lowPoints)))
        
        self.solve_p2()

        
if __name__ == '__main__':
    with open('../../Files/09.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d09()
    solver.solve(data) 

    