import sys

if __name__ == '__main__':

    # Part 1
    input = sys.stdin.readlines()
    idx = 0
    steps = 0
    while idx >= 0 and idx < len(input):
        jumps = int(input[idx])
        input[idx] = int(input[idx]) + 1;
        idx += jumps
        steps += 1

    print(steps)
