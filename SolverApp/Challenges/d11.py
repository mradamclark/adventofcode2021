#!/usr/bin/env python

FLASH_POINT = 9

class Octopus:
    def __init__(self, r, c, currentLevel):
        self.row, self.col = r,c
        self.currentLevel = currentLevel
        self.flashPoint = FLASH_POINT
    
    def step(self):
        self.currentLevel += 1
        if self.currentLevel > self.flashPoint:
            self.currentLevel = 0
          
    def flashed(self):
        return self.currentLevel == 0
    
    def __str__(self):
        return str('o({},{}):{}'.format(self.row, self.col, self.currentLevel))
    
    def __repr__(self):
        return str(self.currentLevel)
    
class OctopiGrid:
    def __init__(self, step, flashpoint, lines):
        self.setupGridByLines(flashpoint, lines)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.step = step
        self.flashCount = 0
        
    def setupGridByLines(self,flashpoint,lines):
        self.grid = list()
        r = 0
        for l in lines:
            c = 0
            self.grid.append([])
            for x in list(l):
                self.grid[r].append(Octopus(r, c, int(x)))
                c += 1
            r += 1
        
    def perfomStep(self):
        needsToSplash = []
        for row in self.grid:
            for o in row:
                o.step()
                if (o.flashed()):
                    needsToSplash.append(o)
       
        for o in needsToSplash:
            needsToSplash.extend(self.doSplash(o))
    
    def doSplash(self, o):
        needToFlash = []
        self.flashCount += 1
        #print('splash event ({},{}) = {}'.format(o.row, o.col, self.grid[o.row][o.col]))
        for r in range(o.row - 1, o.row + 2):
                for c in range(o.col - 1, o.col +2):
                    if (r >= 0 and r < self.rows) and (c >= 0 and c < self.cols) and not (r == o.row and c == o.col):
                            if not self.grid[r][c].flashed():
                                #print('\tsplashin: ({},{})'.format(r,c))
                                self.grid[r][c].step()
                                if self.grid[r][c].flashed():
                                    needToFlash.append(self.grid[r][c])
        return(needToFlash)
    
    def allFlash(self): 
        total = 0
        for r in self.grid:
            total += sum([o.currentLevel for o in r])
            
        return total
                                     
    
    def __str__(self):
        s = ''
        for r in self.grid:
            s += str(r) + '\n'
            
        s += 'FlashCount: ' + str(self.flashCount)
        return s        

class d11:
    def solve_p1(self, lines) -> int:
        octopiGrid = OctopiGrid(1, FLASH_POINT, lines)
        for i in range(0,100):        
            octopiGrid.perfomStep()
            
        return(octopiGrid.flashCount)
    
    def solve_p2(self, lines) -> int:
        octopiGrid = OctopiGrid(1, FLASH_POINT, lines)
        
        step = 0
        while octopiGrid.allFlash():
            step += 1
            octopiGrid.perfomStep()
            
        return(step)
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines)))
        print('')
        print('p2 = {}'.format(self.solve_p2(lines)))

        
if __name__ == '__main__':
    with open('../../Files/11.input.txt') as file:
            lines = [line.strip() for line in file]
    solver = d11()
    solver.solve(lines) 

    