#!/usr/bin/env python

import re        

class d13:
        
    def foldPaper(self, coords, instrs):
        for instr in instrs:
            f = instr[1]
            tempcoords = []
            if instr[0] == 'y':
                for c in coords:
                    if (c[1] > f):
                        nc = (c[0], f-(c[1]-f))
                        if nc not in coords:
                            tempcoords.append(nc)
                    else:
                        tempcoords.append(c)
            else:
                for c in coords:
                    if (c[0] > f):
                        nc = (f-(c[0]-f), c[1])
                        if nc not in coords:
                            tempcoords.append(nc)
                    else:
                        tempcoords.append(c)
            coords = tempcoords
        return coords
       
    def loadCoordsAndInstructions(self, lines):
        pastCoords = False
        coords = []
        instrs = []
        p = 'fold along (x|y)=(\d+)'
        for l in lines:
            if len(l) == 0:
                pastCoords = True
                continue
            
            if not pastCoords:
                n = l.split(',')
                coords.append((int(n[0]), int(n[1])))
            else:
                cmd = re.findall(p,l)[0]
                instrs.append((cmd[0],int(cmd[1]))) 
        
        return coords, instrs
    
    def solve_p1(self, lines) -> int:
        coords, instrs = self.loadCoordsAndInstructions(lines)
        newcoords = self.foldPaper(coords, [instrs[0]])
        return(len(newcoords))
    
    def solve_p2(self, lines) -> int:
        coords, instrs = self.loadCoordsAndInstructions(lines)
        newcoords = self.foldPaper(coords, instrs)
        
        mx,my = 0,0
       
        for c in newcoords:
            mx = c[0] if c[0] > mx else mx
            my = c[1] if c[1] > my else my
        
        print(mx,my)
        
        paper = [[' ' for i in range(mx+1)] for j in range(my+1)]
    
        for c in newcoords:
            paper[c[1]][c[0]] = '#'
        
        for l in paper:
            print(''.join(l))
        
        return('see display')
  
    def solve(self, lines):
        print('p1 = {}'.format(self.solve_p1(lines)))
        print('p2 = {}'.format(self.solve_p2(lines)))

        
if __name__ == '__main__':
    with open('../../Files/13.input.txt') as file:
            lines = [line.strip() for line in file]
    solver = d13()
    solver.solve(lines)

    