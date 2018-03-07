import sys
from collections import deque

def get_value(tmp, registers):
    if not tmp.replace("-", "").isdigit():
        tmp = int(registers[tmp])
    return int(tmp)

def snd(instruction, registers):
    frequency = instruction.split(" ")[1]
    return get_value(frequency, registers)

def set(instruction, registers):
    register = instruction.split(" ")[1]
    value = instruction.split(" ")[2]
    registers[register] = get_value(value, registers)

def add(instruction, registers):
    register = instruction.split(" ")[1]
    value = instruction.split(" ")[2]
    registers[register] += get_value(value, registers)

def mul(instruction, registers):
    register = instruction.split(" ")[1]
    value = instruction.split(" ")[2]
    registers[register] *= get_value(value, registers)

def mod(instruction, registers):
    register = instruction.split(" ")[1]
    value = instruction.split(" ")[2]
    registers[register] %= get_value(value, registers)

def rcv(instruction, registers):
    value = instruction.split(" ")[1]
    return get_value(value, registers)

def jgz(instruction, registers):
    x_val = instruction.split(" ")[1]
    y_val = instruction.split(" ")[2]
    x_val = get_value(x_val, registers)
    y_val = get_value(y_val, registers)

    return (x_val, y_val)

def part_one():
    freq_of_last_sound = 0
    cnt = 0

    while (cnt < len(instructions)):

        instruction = instructions[cnt].strip()

        if 'snd' in instruction:
            freq_of_last_sound = snd(instruction, registers)
        elif 'set' in instruction:
            set(instruction, registers)
        elif 'add' in instruction:
            add(instruction, registers)
        elif 'mul' in instruction:
            mul(instruction, registers)
        elif 'mod' in instruction:
            mod(instruction, registers)
        elif 'rcv' in instruction:
            value = rcv(instruction, registers)

            if value != 0:
                final = freq_of_last_sound
                print("solution part1: {}".format(freq_of_last_sound))
                break

        elif 'jgz' in instruction:
            x_val, y_val = jgz(instruction, registers)

            if x_val > 0:
                cnt += y_val
                continue

        cnt += 1

def part_two():

    queue_zero = deque([])
    queue_one = deque([])

    cnt = 0
    program_zero_active = True
    instruction_before = ""
    both_waiting = False
    program_zero_sending = 0
    program_one_sending = 0
    program_zero_start_idx = 0

    while (cnt < len(instructions)):

        instruction = instructions[cnt].strip()

        if instruction == instruction_before and both_waiting:
            print("deadlock caused by {}".format(instruction))
            print("solution part2: {}".format(program_one_sending))
            break

        both_waiting = False

        if instruction == instruction_before:
            both_waiting = True
        instruction_before = instruction

        if program_zero_active:
            registers = registers_program_zero
        else:
            registers = registers_program_one

        if 'snd' in instruction:
            frequency = snd(instruction, registers)

            if program_zero_active:
                program_zero_sending += 1
                queue_one.append(frequency)
            else:
                program_one_sending += 1
                queue_zero.append(frequency)

        elif 'set' in instruction:
            set(instruction, registers)
        elif 'add' in instruction:
            add(instruction, registers)
        elif 'mul' in instruction:
            mul(instruction, registers)
        elif 'mod' in instruction:
            mod(instruction, registers)
        elif 'rcv' in instruction:
            register = instruction.split(" ")[1]

            if program_zero_active:
                if len(queue_zero) == 0:
                    program_zero_active = False
                    cnt = program_zero_start_idx
                    continue
                else:
                    val = queue_zero[0]
                    queue_zero.popleft()
                    registers[register] = val
            else:
                if len(queue_one) == 0:
                    program_zero_active = True
                    program_zero_start_idx = cnt
                    continue
                else:
                    val = queue_one[0]
                    queue_one.popleft()
                    registers[register] = val

        elif 'jgz' in instruction:
            x_val, y_val = jgz(instruction, registers)

            if x_val > 0:
                cnt += y_val
                continue

        cnt += 1

if __name__ == '__main__':

    instructions = sys.stdin.readlines()

    registers = dict(
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
         "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
         "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

    registers_program_zero = registers.copy()
    registers_program_one = registers.copy()
    registers_program_one["p"] = 1

    part_one()
    part_two()
