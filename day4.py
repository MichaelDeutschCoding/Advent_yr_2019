my_range = range(158126, 624575)

def part_one(num):
    num = str(num)
    doubled = False
    for i in range(1,6):
        if num[i] == num[i-1]:
            doubled = True
        if num[i] < num[i-1]:
            return False
    return doubled

def part_two(num):
    num = str(num)
    doubled = False
    for i in range(1,6):
        if num[i] < num[i-1]:
            return False
        if num[i] == num[i-1]:
            
            if i >= 2:
                if num[i-2] == num[i]:
                    continue

            if i <= 4:
                if num[i+1] == num[i]:
                    continue
            doubled = True

    return doubled


print('Part 1:', sum([part_one(num) for num in my_range]))
print('Part 2:', sum([part_two(num) for num in my_range]))