import sys

def get_value(tmp):
    if not tmp.replace("-", "").isdigit():
        tmp = int(registers[tmp])
    return int(tmp)

if __name__ == '__main__':

    instructions = sys.stdin.readlines()

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
            freq_of_last_sound = get_value(frequency)
        elif 'set' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] = get_value(value)
        elif 'add' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] += get_value(value)
        elif 'mul' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] *= get_value(value)
        elif 'mod' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]
            registers[register] %= get_value(value)
        elif 'rcv' in instruction:
            value = instruction.split(" ")[1]
            value = get_value(value)

            if value != 0:
                final = freq_of_last_sound
                print("recover {}".format(freq_of_last_sound))
                break

        elif 'jgz' in instruction:
            x_val = instruction.split(" ")[1]
            y_val = instruction.split(" ")[2]
            x_val = get_value(x_val)
            y_val = get_value(y_val)

            if x_val > 0:
                cnt += y_val
                continue

        cnt += 1
