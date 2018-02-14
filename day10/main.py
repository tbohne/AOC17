import sys
import copy
from operator import xor
from functools import reduce

def hash(lengths, int_list, idx, skip_size, round, number_of_rounds):
    for l in lengths:
        sub_list = []
        indices = []
        for i in range(idx, idx + l):
            indices.append(i % len(int_list))
            sub_list.append(int_list[i % len(int_list)])
        sub_list.reverse()

        cnt = 0
        for i in indices:
            int_list[i] = sub_list[cnt]
            cnt += 1

        idx = (idx + l + skip_size) % len(int_list)
        skip_size += 1

    round += 1
    if round == number_of_rounds:
        return int_list
    else:
        hash(lengths, int_list, idx, skip_size, round, number_of_rounds)
    return int_list

def dense_hash(ascii_input):

    seq = [17, 31, 73, 47, 23]
    ascii_input += seq

    skip_size = 0
    idx = 0
    round = 0

    int_list = []
    for i in range(0, 256):
        int_list.append(i)

    sparse_hash = hash(ascii_input, int_list, idx, skip_size, round, 64)

    dense_hash = []
    hash_cnt = 0
    tmp = []
    for i in sparse_hash:
        if hash_cnt == 15:
            tmp.append(int(i))
            dense_hash.append(reduce(xor, tmp))
            hash_cnt = 0
            tmp = []
        else:
            tmp.append(int(i))
            hash_cnt += 1

    hex_dense_hash = []
    for i in dense_hash:
        hex_dense_hash.append(format(i, '02x'))

    return hex_dense_hash


if __name__ == '__main__':
    inp = sys.stdin.read()
    input = copy.copy(inp)

    lengths = []
    input = input.split(',')
    for i in input:
        lengths.append(int(i.strip()))

    int_list = []
    for i in range(0, 256):
        int_list.append(i)

    skip_size = 0
    idx = 0
    round = 0

    sparse_hash = hash(lengths, int_list, idx, skip_size, round, 1)
    print("solution task1:", sparse_hash[0] * sparse_hash[1])

    ascii_input = []
    for i in inp.strip():
        ascii_input.append(ord(i))

    hex_dense_hash = dense_hash(ascii_input)
    print("solution part2:",''.join(str(e) for e in hex_dense_hash))
