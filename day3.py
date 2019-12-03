with open('day3_input.txt') as f:
    wires = f.readlines()

def manhattan_distance(point):
    x,y = point
    return (abs(x) + abs(y))


class Wire:

    def __init__(self, instructions):
        self.instructions = instructions.split(',')
        self.visited = set()
        self.steps_dict = {}
        self.x = 0
        self.y = 0
        self.steps_taken = 0

    def take_step(self, direction):
        self.steps_taken += 1
        if direction == 'R':
            self.x += 1
        elif direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        else:
            self.x -= 1

    def follow_path(self):
        for instruction in self.instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            for _ in range(distance):
                self.take_step(direction)
                if not (self.x, self.y) in self.visited:
                  self.visited.add((self.x, self.y))
                  self.steps_dict[(self.x, self.y)] = self.steps_taken

    def find_intersects(self, other):
        self.follow_path()
        other.follow_path()
        return self.visited & other.visited


def follow(wire):
    wire = wire.split(',')
    step_dict = {}
    visited = set()
    x, y = 0, 0
    steps_taken = 0
    for instruction in wire:

        direction, distance = instruction[0], int(instruction[1:])
        for d in range(distance):
            steps_taken += 1
            if direction == 'R':
                x += 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            else:
                x -= 1
            visited.add((x, y))
            steps_taken += 1
            step_dict[(x, y)] = steps_taken
    return visited

def closest_intersect(wire1, wire2):
    intersects = follow(wire1) & follow(wire2)
    print(intersects)
    return min([manhattan_distance(point) for point in intersects])

def part_one(wire1, wire2):
    w1 = Wire(wire1)
    w2 = Wire(wire2)
    intersects = w1.find_intersects(w2)
    return min([manhattan_distance(point) for point in intersects])

def part_two(wire1, wire2):
    w1 = Wire(wire1)
    w2 = Wire(wire2)
    intersects = w1.find_intersects(w2)
    return min([w1.steps_dict[spot] + w2.steps_dict[spot] for spot in intersects])


print(part_two(wires[0], wires[1]))