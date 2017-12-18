import sys
import copy

def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst

if __name__ == '__main__':
    input = sys.stdin.read()

    lengths = []
    input = input.split(',')
    for i in input:
        lengths.append(int(i.strip()))

    int_list = []
    for i in range(0, 256):
        int_list.append(i)

    skip_size = 0
    idx = 0

    for l in lengths:
        # reverse_sublist(int_list, idx, l)
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

    print("solution task1:", int_list[0] * int_list[1])
