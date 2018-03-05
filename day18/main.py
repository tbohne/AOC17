import sys

if __name__ == '__main__':

    instructions = sys.stdin.readlines()

    registers = dict(
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
         "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
         "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

    freq_of_last_sound = 0
    cnt = 0
    final = ""

    while (cnt < len(instructions)):

        instruction = instructions[cnt].strip()

        if 'snd' in instruction:
            frequency = instruction.split(" ")[1]

            if not frequency.replace("-", "").isdigit():
                frequency = int(registers[frequency])

            freq_of_last_sound = int(frequency)
        elif 'set' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]

            if not value.replace("-", "").isdigit():
                value = int(registers[value])

            registers[register] = int(value)
        elif 'add' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]

            if not value.replace("-", "").isdigit():
                value = int(registers[value])

            registers[register] += int(value)
        elif 'mul' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]

            if not value.replace("-", "").isdigit():
                value = int(registers[value])

            registers[register] *= int(value)
        elif 'mod' in instruction:
            register = instruction.split(" ")[1]
            value = instruction.split(" ")[2]

            if not value.replace("-", "").isdigit():
                value = int(registers[value])

            registers[register] %= int(value)
        elif 'rcv' in instruction:
            value = instruction.split(" ")[1]

            if not value.replace("-", "").isdigit():
                values = int(registers[value])

            if value != 0:
                if final == "":
                    final = freq_of_last_sound
                    print("recover {}".format(freq_of_last_sound))

        elif 'jgz' in instruction:
            val1 = instruction.split(" ")[1]
            val2 = instruction.split(" ")[2]

            if not val1.replace("-", "").isdigit():
                val1 = int(registers[val1])
            if not val2.replace("-", "").isdigit():
                val2 = int(registers[val2])

            val1 = int(val1)
            val2 = int(val2)

            if val1 > 0:
                cnt += val2
                continue

        cnt += 1
