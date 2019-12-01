with open('day1_input.txt', 'r') as f:
    mods = [int(n) for n in f.read().split()]

def calc_fuel(mass):
    return mass // 3 -2

def fuel_two(mass):
    total = 0
    while True:
        added_fuel = calc_fuel(mass)
        if added_fuel >0:
            total += added_fuel
            mass = added_fuel
            continue
        return total

def part_one():
    return (sum([calc_fuel(mass) for mass in mods]))

def part_two():
    return sum([fuel_two(n) for n in mods])

# print(part_one())
print(part_two())