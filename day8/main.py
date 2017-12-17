import sys

def calc_new_val(a1, a2, dec):
    if dec:
        return int(a1) -int(a2)
    else:
        return int(a1) + int(a2)

if __name__ == '__main__':
    input = sys.stdin.readlines()
    lines = []
    registers = dict()
    highest = 0

    for i in input:
        lines.append(i.strip().split(' '))

    # Initializes all registers
    for i in lines:
        register = i[0]
        registers[register] = 0

    for i in lines:
        register = i[0]
        dec = True if i[1] == 'dec' else False
        change_by = i[2]
        operand = int(registers[i[4]])
        value = int(i[6])
        operator = i[5]

        if operator == '<':
            if operand < value:
                registers[register] = calc_new_val(registers[register], change_by, dec)
        elif operator == '>':
            if operand > value:
                registers[register] = calc_new_val(registers[register], change_by, dec)
        elif operator == '<=':
            if operand <= value:
                registers[register] = calc_new_val(registers[register], change_by, dec)
        elif operator == '>=':
            if operand >= value:
                registers[register] = calc_new_val(registers[register], change_by, dec)
        elif operator == '==':
            if operand == value:
                registers[register] = calc_new_val(registers[register], change_by, dec)
        else:
            if operand != value:
                registers[register] = calc_new_val(registers[register], change_by, dec)

        if registers[register] > highest:
            highest = registers[register]

    print("solution part1:", max(registers.values()))
    print("solution part2: ", highest)
