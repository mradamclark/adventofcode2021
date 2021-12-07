
import statistics

def solve_p1(positions):
    m = statistics.median(positions)
    fuel_usage = list(map(lambda x:int(abs(x-m)), positions))
    print(sum(fuel_usage))

def solve_p2(positions):
    f = lambda n: n * (n + 1) / 2
    usedfuel = int(min([sum([f(abs(t - p)) for p in positions]) for t in range(max(positions))]))
    print(usedfuel)


class d07:
    def __init__(self):
        pass

    def solve(self, data):
        positions = list(map(lambda x:int(x.strip()), data[0].split(',')))
        solve_p1(positions)
        solve_p2(positions)
       

if __name__ == '__main__':
    with open('../../Files/07.input.txt') as file:
            data = [line.strip() for line in file]
    solver = d07()
    solver.solve(data) 

    