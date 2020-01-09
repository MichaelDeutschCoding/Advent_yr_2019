from collections import defaultdict

sample = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"


# with open('day9_input.txt') as f:
#     codes = [int(num) for num in f.read().split(',')]


codes = defaultdict(int)
for i, n in enumerate(sample.split(',')):
    codes[i] = int(n)


def parse(instructions):
    opcode = instructions % 100
    mode_p1 = instructions //100 % 10
    mode_p2 = instructions //1000 % 10
    mode_p3 = instructions //10000 % 10

    return opcode, mode_p1, mode_p2, mode_p3






def part_one():

    rel_base = 0
    i = 0

    def get_value(mode, param):
        # mode, param = zipped
        if mode == 1:
            return param
        if mode == 2:
            return codes[param+rel_base]
        if mode == 0:
            return codes[param]


    opcode = None
    
    while opcode !=99:

        opcode, mode_p1, mode_p2, mode_write_to = parse(codes[i])

        print(i, opcode, mode_p1, mode_p2, mode_write_to)

        write_to = i+3 if mode_write_to == 0 else i+3+rel_base

        if opcode == 1:
            codes[write_to] = get_value(mode_p1, codes[i+1]) + get_value(mode_p2, codes[i+2])
            i += 4

        elif opcode == 2:
            codes[write_to] = get_value(mode_p1, codes[i+1]) \
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
                codes[write_to] = 1
            else:
                codes[write_to] = 0
            i += 4

        elif opcode == 8:
            if get_value(mode_p1, codes[i+1]) == get_value(mode_p2, codes[i+2]):
                codes[write_to] = 1
            else:
                codes[write_to] = 0
            i += 4

        elif opcode == 9:
            rel_base += get_value(mode_p1, codes[i+1])
            i += 2

        elif opcode == 99:
            break

part_one()