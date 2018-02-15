import sys

if __name__ == '__main__':

    gen_a_start_val = 873
    gen_b_start_val = 583
    fac_a = 16807
    fac_b = 48271
    divisor = 2147483647

    prev_a = gen_a_start_val
    prev_b = gen_b_start_val
    matches = 0

    for i in range(int(40e6)):
        prev_a = prev_a * fac_a
        prev_b = prev_b * fac_b
        prev_a %= divisor
        prev_b %= divisor
        # reverses the binary strings and returns the first 16 chars (lowest 16 bits)
        lowest16_a = "{0:b}".format(prev_a)[::-1][:16]
        lowest16_b = "{0:b}".format(prev_b)[::-1][:16]

        if lowest16_a == lowest16_b:
            matches += 1

    print(matches)
