#!/usr/bin/python

class d06:
    def __init__(self):
        pass

    def solve(self, data):
        print(data)
        fish = list(map(lambda x:int(x.strip()), data[0].split(',')))
  
        days = 80
        for n in range(days):
            newfish = []
            for f in range(len(fish)):
                if fish[f] == 0:
                    newfish.append(8)
                    fish[f] = 6
                else:
                    fish[f] -= 1
            fish += newfish
            print('{}: {}'.format(n, len(fish)))
        
        print(len(fish))
        

if __name__ == '__main__':
    with open('../../Files/06.test.txt') as file:
            data = [line.strip() for line in file]
    solver = d06()
    solver.solve(data) 

    