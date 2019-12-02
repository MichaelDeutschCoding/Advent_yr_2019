codes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]

def op1(i):
    val1 = codes[codes[i+1]]
    val2 = codes[codes[i+2]]
    codes[codes[i+3]] = val1 + val2

def op2(i):
    val1 = codes[codes[i+1]]
    val2 = codes[codes[i+2]]
    codes[codes[i+3]] = val1 * val2

def walk():
    for i in range(0, len(codes), 4):
        if codes[i] == 99:
            return codes[0]
        if codes[i] == 1:
            op1(i)
        elif codes[i] == 2:
            op2(i)
        else:
            raise ValueError


# print(walk())

for noun in range(100):
    for verb in range(100):
        memory = [val for val in codes]
        memory[1] = noun
        memory[2] = verb
        for i in range(0, len(memory), 4):
            op = memory[i]
            lhs_loc, rhs_loc, dest_loc = memory[i + 1], memory[i + 2], memory[i + 3]
            if op == 1:
                memory[dest_loc] = memory[lhs_loc] + memory[rhs_loc]
            elif op == 2:
                memory[dest_loc] = memory[lhs_loc] * memory[rhs_loc]
            else:
                assert (op == 99)
                break
        if memory[0] == 19690720:
            print('noun:', noun, 'verb:', verb)
            print('100 * noun + verb:', 100 * noun + verb)