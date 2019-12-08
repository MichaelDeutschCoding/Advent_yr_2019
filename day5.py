
sample = "1002,4,3,4,33"
sample = "1101, 100, -1, 4, 0"
sample = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
sample = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
codes = [int(num) for num in sample.split(',')]


with open('day5_input.txt') as f:
    codes = [int(num) for num in f.read().split(',')]


def parse(instructions):
    opcode = instructions % 100
    mode_p1 = instructions //100 % 10
    mode_p2 =instructions //1000 % 10

    return opcode, mode_p1, mode_p2

def get_value(mode, param):
    # mode, param = zipped
    if mode == 1:
        return param
    if mode == 0:
        return codes[param]


def part_one():

    i = 0
    opcode = None
    
    while opcode !=99:
        opcode, mode_p1, mode_p2 = parse(codes[i])

        print(i, opcode, mode_p1, mode_p2, codes[i:i+4])

        if opcode == 1:
            codes[codes[i+3]] = get_value(mode_p1, codes[i+1]) + get_value(mode_p2, codes[i+2])
            i += 4

        elif opcode == 2:
            codes[codes[i+3]] = get_value(mode_p1, codes[i+1]) \
                            * get_value(mode_p2, codes[i+2])
            i += 4

        elif opcode == 3:
            codes[codes[i+1]] = 5 ##  Input
            i += 2

        elif opcode == 4:
            print(get_value(mode_p1, codes[i+1]))
            i += 2
        
        elif opcode == 5:
            if get_value(mode_p1, codes[i+1]):
                i = get_value(mode_p2, codes[i+2])
            else:
                i += 3

        elif opcode == 6:
            if not get_value(mode_p1, codes[i+1]):
                i = get_value(mode_p2, codes[i+2])
            else:
                i += 3

        elif opcode == 7:
            if get_value(mode_p1, codes[i+1]) < get_value(mode_p2, codes[i+2]):
                codes[codes[i+3]] = 1
            else:
                codes[codes[i+3]] = 0
            i += 4

        elif opcode == 8:
            if get_value(mode_p1, codes[i+1]) == get_value(mode_p2, codes[i+2]):
                codes[codes[i+3]] = 1
            else:
                codes[codes[i+3]] = 0
            i += 4

        elif opcode == 99:
            break

part_one()