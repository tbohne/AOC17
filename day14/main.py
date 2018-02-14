import sys
from operator import xor
from functools import reduce
import binascii

import importlib.util
spec = importlib.util.spec_from_file_location("day10.main", "../day10/main.py")
day10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day10)

if __name__ == '__main__':

    hash_inputs = []
    input_string = 'uugsqrei'

    for i in range(0, 128):
        curr_row_hash = input_string + "-" + str(i)
        hash_inputs.append(curr_row_hash)

    grid = ''
    for i in hash_inputs:

        ascii_input = [ord(x) for x in i]
        hex_dense_hash = day10.dense_hash(ascii_input)
        hex_dense_hash_str = ''.join(str(e) for e in hex_dense_hash)

        scale = 16
        num_of_bits = 4
        binary = bin(int(hex_dense_hash_str, scale))[2:].zfill(num_of_bits)

        for c in binary:
            if c == '1':
                grid += '#'
            else:
                grid += '.'

    print("used squares: " + str(grid.count('#')))
