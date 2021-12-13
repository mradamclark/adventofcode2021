#!/usr/bin/env python

class Cave:
    def __init__(self, id):
        self.connections = {}
        self.Id = id
        self.start = id == 'start'
        self.end = id == 'end'
        self.small = id.islower()
        
    def addConnection(self, cave):
        self.connections[cave.Id] = cave
        
class CaveSystem:
    def __init__(self, lines):
        self.caves = {}
        self.pathCount = 0
        for l in lines:
            a, b = l.split('-')

            caveA = self.getCave(a)
            if (caveA == None):
                caveA = Cave(a)
                self.addCave(caveA)
            
            caveB = self.getCave(b)
            if (caveB == None):
                caveB = Cave(b)
                self.addCave(caveB)
            
            if (b not in ['start']):
                caveA.addConnection(caveB)
            
            if (a not in ['start'] and b not in ['end']):
                caveB.addConnection(caveA)
       
    def addCave(self, cave):
        self.caves[cave.Id] = cave
    
    def getCave(self, id) -> Cave:
        if id in self.caves.keys():
            return self.caves[id]
        
    def getAllPaths(self) -> int:
       
        return self.pathCount
    
    def findPaths(self, cave, end, visited, revisit = False):
        if cave == end:
            self.pathCount += 1
            return
        
        for k,n in cave.connections.items():
            if n.small and k in visited:
                if revisit: 
                    self.findPaths(n, end, {*visited, cave.Id}, False)
                else:
                    continue
            else:
                self.findPaths(n, end, {*visited, cave.Id}, revisit)
           
class d12:
        
    def solve_p1(self, lines) -> int:
        caves_p1 = CaveSystem(lines)
        visited = set()
        caves_p1.findPaths(caves_p1.getCave('start'), caves_p1.getCave('end'), visited)
        return(caves_p1.pathCount)
    
    def solve_p2(self, lines) -> int:
        caves = CaveSystem(lines)
        visited = set()
        caves.findPaths(caves.getCave('start'), caves.getCave('end'), visited, True)
        return(caves.pathCount)
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines)))
        print('p2 = {}'.format(self.solve_p2(lines)))

        
if __name__ == '__main__':
    print('test-simple')
    with open('../../Files/12.test-simple.txt') as file:
            lines = [line.strip() for line in file]
    solver = d12()
    solver.solve(lines)
        
    print('\ntest-med')
    with open('../../Files/12.test-med.txt') as file:
            lines = [line.strip() for line in file]
    solver = d12()
    solver.solve(lines)
    
    print('\ntest-large')
    with open('../../Files/12.test-large.txt') as file:
            lines = [line.strip() for line in file]
    solver = d12()
    solver.solve(lines)
    
    print('\ninput')
    with open('../../Files/12.input.txt') as file:
            lines = [line.strip() for line in file]
    solver = d12()
    solver.solve(lines) 

    