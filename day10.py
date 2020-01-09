from math import gcd
from collections import defaultdict, OrderedDict


sample = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".splitlines()

with open('day10_input.txt') as f:
    data = f.read().splitlines()

asteroid_list = []
class Asteroid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angles_blocked = defaultdict(list)

    def __repr__(self):
        return f"Asteroid at {self.x}, {self.y}."

    def get_angle(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        simplify = gcd(delta_x, delta_y)
        return (int(delta_y / simplify), int(delta_x / simplify))

    def check_visible(self):
        for aster in set(asteroid_list) - {self}:
            # print(f"Checking: {aster}")
            self.angles_blocked[self.get_angle(aster)].append(aster)

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def sort_lists(self):
        for angle in self.angles_blocked:
            self.angles_blocked[angle] = sorted(self.angles_blocked[angle],
            key = lambda target: self.distance(target))

    
    def order_angles(self):
        self.sort_lists()
        self.ordered = OrderedDict()

        for angle in sorted([
                ang for ang in self.angles_blocked
                if ang[0] >=0 and ang[1] > 0
            ], key= lambda x: convert_to_num(x)):
            self.ordered[angle] = self.angles_blocked[angle]
        
        for angle in sorted([
                ang for ang in self.angles_blocked
                if ang[0] <0 and ang[1] > 0
            ], key= lambda x: convert_to_num(x)):
            self.ordered[angle] = self.angles_blocked[angle]
        for angle in sorted([
                ang for ang in self.angles_blocked
                if ang[0] >=0 and ang[1] > 0
            ], key= lambda x: convert_to_num(x)):
            self.ordered[angle] = self.angles_blocked[angle]
        for angle in sorted([
                ang for ang in self.angles_blocked
                if ang[0] >=0 and ang[1] > 0
            ], key= lambda x: convert_to_num(x)):
            self.ordered[angle] = self.angles_blocked[angle]                                    

def get_asteroids(lst):
    for y in range(len(lst)):
        for x in range(len(lst[0])):
            if lst[y][x] == '#':
                asteroid_list.append(Asteroid(x, y))

def convert_to_num(ratio):
    try:
        return ratio[0] / ratio[1]
    except ZeroDivisionError:
        return ratio[0] / ratio[0]
        


get_asteroids(sample)

for asteroid in asteroid_list:
    asteroid.check_visible()
# 11, 13                  index[205]

monitor = asteroid_list[100]

print(monitor)
monitor.sort_lists()
# for angle in monitor.angles_blocked:
#     print(angle, [monitor.distance(a) for a in monitor.angles_blocked[angle]])

monitor.order_angles()

# print(max([len(ast.angles_blocked) for ast in asteroid_list]))

# print([i for i in range(len(asteroid_list))
# if len(asteroid_list[i].angles_blocked) == 210])


# max was 334
## located at 23, 20     


# print(asteroid_list[205].angles_blocked)