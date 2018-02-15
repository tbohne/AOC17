import sys
from operator import xor
from functools import reduce
import binascii

import importlib.util
spec = importlib.util.spec_from_file_location("day10.main", "../day10/main.py")
day10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day10)

def hex_to_binary(hex):
    return bin(int(hex, 16))[2:]

if __name__ == '__main__':

    hash_inputs = []
    example_string = 'flqrgnkx'
    input_string = 'uugsqrei'

    for i in range(0, 128):
        curr_row_hash = example_string + "-" + str(i)
        hash_inputs.append(curr_row_hash)

    grid = ''
    for i in hash_inputs:
        ascii_input = [ord(x) for x in i]
        hex_dense_hash = day10.dense_hash(ascii_input)
        hex_dense_hash_str = ''.join(str(e) for e in hex_dense_hash)

        binary = hex_to_binary(hex_dense_hash_str)

        for c in binary:
            if c == '1':
                grid += '#'
            else:
                grid += '.'

    pos = 0
    for i in grid:
        if pos % 128 == 0 and pos != 0:
            print()
        sys.stdout.write(i)
        pos += 1
    print()


    print("used squares: " + str(grid.count('#')))

    tabulist = []
    regions = 0

    for row in range(0, 128):
        for col in range(0, 128):
            if 128 * row + col <= len(grid) - 1 and grid[128 * row + col] == '#':

                tabulist.append(row * 128 + col)

                if (row - 1) * 128 + col >= 0 and (row - 1) * 128 + col <= len(grid) - 1 and (row - 1) * 128 + col in tabulist:
                    continue
                # can't be part of the tabulist because it is yet to come
                # elif (row + 1) * 128 + col >= 0 and (row + 1) * 128 + col <= len(grid) - 1 and (row + 1) * 128 + col in tabulist:
                #     continue
                elif row * 128 + col - 1 >= 0 and row * 128 + col - 1 <= len(grid) - 1 and row * 128 + col - 1 in tabulist:
                    continue
                # can't be part of the tabulist because it is yet to come
                # elif row * 128 + col + 1 >= 0 and row * 128 + col + 1 <= len(grid) - 1 and row * 128 + col + 1 in tabulist:
                #     continue

                regions += 1

    print(regions)
