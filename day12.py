import re

class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def __repr__(self):
        return f"Moon: {self.x}, {self.y}, {self.z}; vel = {self.x_vel}, {self.y_vel}, {self.z_vel}\n"

    def apply_gravity(self, other):
        if self.x < other.x:
            self.x_vel += 1
            other.x_vel -= 1
        elif self.x > other.x:
            self.x_vel -= 1
            other.x_vel += 1
        
        if self.y < other.y:
            self.y_vel += 1
            other.y_vel -= 1
        elif self.y > other.y:
            self.y_vel -= 1
            other.y_vel += 1

        if self.z < other.z:
            self.z_vel += 1
            other.z_vel -= 1
        elif self.z > other.z:
            self.z_vel -= 1
            other.z_vel += 1
        
    def adjust_position(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel

    def calc_energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)
        return potential * kinetic


def take_step(moons):
    for i in range(len(moons)):
        for j in range(i+1, len(moons)):
            moons[i].apply_gravity(moons[j])
    for moon in moons:
        moon.adjust_position()

def calc_total_energy(moons):
    return sum([moon.calc_energy() for moon in moons])


def parse_moon(string):
    nums = re.findall(r"=(-?\d{1,2})", string)
    return Moon(
        int(nums[0]),
        int(nums[1]),
        int(nums[2])
    )


def read_input(string):
    return [parse_moon(line) for line in string.splitlines()]


my_input = """<x=13, y=-13, z=-2>
<x=16, y=2, z=-15>
<x=7, y=-18, z=-12>
<x=-3, y=-8, z=-8>"""

example1 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


moons = read_input(my_input)
print(moons)
for _ in range(1000):
    take_step(moons)
print(moons)



print(calc_total_energy(moons))