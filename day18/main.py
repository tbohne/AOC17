import sys
from collections import deque

def get_value(tmp, registers):
    if not tmp.replace("-", "").isdigit():
        tmp = int(registers[tmp])
    return int(tmp)

def part_one():

    registers = dict(
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
         "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
         "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

    freq_of_last_sound = 0
    cnt = 0

    while (cnt < len(instructions)):

        instruction = instructions[cnt].strip()

        if 'snd' in instruction:
            frequency = instruction.split(" ")[1]
            freq_of_last_sound = get_value(frequency, registers)
        elif 'set' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] = get_value(value, registers)
        elif 'add' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] += get_value(value, registers)
        elif 'mul' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] *= get_value(value, registers)
        elif 'mod' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] %= get_value(value, registers)
        elif 'rcv' in instruction:
            value = instruction.split(" ")[1]
            value = get_value(value, registers)

            if value != 0:
                final = freq_of_last_sound
                print("recover {}".format(freq_of_last_sound))
                break

        elif 'jgz' in instruction:
            x_val = instruction.split(" ")[1]
            y_val = instruction.split(" ")[2]
            x_val = get_value(x_val, registers)
            y_val = get_value(y_val, registers)

            if x_val > 0:
                cnt += y_val
                continue

        cnt += 1

if __name__ == '__main__':

    instructions = sys.stdin.readlines()
    # part_one()

    registers_program_a = dict(
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
         "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
         "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

    registers_program_b = dict(
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
         "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 1, "q": 0, "r": 0, "s": 0, "t": 0,
         "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

    queueA = deque([])
    queueB = deque([])

    cnt = 0

    program_a_active = True
    msg_before = ""
    deadlock = False
    sends_a = 0
    sends_b = 0
    a_started_from = 0

    while (cnt < len(instructions)):

        instruction = instructions[cnt].strip()

        if instruction == msg_before and deadlock:
            print("deadlock")
            print("A: " + str(sends_a))
            print("B: " + str(sends_b))
            print(instruction)
            break

        deadlock = False

        if instruction == msg_before:
            deadlock = True
        msg_before = instruction

        if program_a_active:
            registers = registers_program_a
        else:
            registers = registers_program_b

        if 'snd' in instruction:
            frequency = instruction.split(" ")[1]
            frequency = get_value(frequency, registers)

            if program_a_active:
                print("program a sends")
                sends_a += 1
                queueB.append(frequency)
            else:
                print("program b sends")
                sends_b += 1
                queueA.append(frequency)

        elif 'set' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] = get_value(value, registers)
        elif 'add' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] += get_value(value, registers)
        elif 'mul' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] *= get_value(value, registers)
        elif 'mod' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] %= get_value(value, registers)

        elif 'rcv' in instruction:

            register = instruction.split(" ")[1]

            if program_a_active:
                if len(queueA) == 0:
                    program_a_active = False
                    cnt = a_started_from
                    continue
                else:
                    print("program a rcv")
                    val = queueA[0]
                    queueA.popleft()
                    registers[register] = val
            else:
                if len(queueB) == 0:
                    program_a_active = True
                    a_started_from = cnt
                    continue
                else:
                    print("program b rcv")
                    val = queueB[0]
                    queueB.popleft()
                    registers[register] = val

        elif 'jgz' in instruction:
            x_val = instruction.split(" ")[1]
            y_val = instruction.split(" ")[2]
            x_val = get_value(x_val, registers)
            y_val = get_value(y_val, registers)

            if x_val > 0:
                cnt += y_val
                continue

        cnt += 1
