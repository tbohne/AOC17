import sys

def part1(gen_a, gen_b):
    prev_a = gen_a
    prev_b = gen_b
    matches = 0

    for _ in range(int(40e6)):
        prev_a = prev_a * fac_a
        prev_b = prev_b * fac_b
        prev_a %= divisor
        prev_b %= divisor
        # reverses the binary strings and returns the first 16 chars (lowest 16 bits)
        lowest16_a = "{0:b}".format(prev_a)[::-1][:16]
        lowest16_b = "{0:b}".format(prev_b)[::-1][:16]

        if lowest16_a == lowest16_b:
            matches += 1

    return matches

def part2(gen_a, gen_b):
    prev_a = gen_a
    prev_b = gen_b
    matches = 0

    a_values = []
    b_values = []

    cnt_a = 0
    cnt_b = 0

    while cnt_a < int(5e6) or cnt_b < int(5e6):

        prev_a = prev_a * fac_a
        prev_b = prev_b * fac_b
        prev_a %= divisor
        prev_b %= divisor

        if prev_a % 4 == 0 and cnt_a < 5e6:
            lowest16_a = "{0:b}".format(prev_a)[::-1][:16]
            a_values.append(lowest16_a)
            cnt_a += 1

        if prev_b % 8 == 0 and cnt_b < 5e6:
            lowest16_b = "{0:b}".format(prev_b)[::-1][:16]
            b_values.append(lowest16_b)
            cnt_b += 1

    for i in range(len(a_values)):
        if a_values[i] == b_values[i]:
            matches += 1

    return matches


if __name__ == '__main__':

    gen_a_start_val = 873
    gen_b_start_val = 583
    fac_a = 16807
    fac_b = 48271
    divisor = 2147483647

    gen_a_test = 65
    gen_b_test = 8921

    print("solution part1: " + str(part1(gen_a_start_val, gen_b_start_val)))
    print("solution part2: " + str(part2(gen_a_start_val, gen_b_start_val)))
