import sys

if __name__ == '__main__':

    input = sys.stdin.read().strip()

    # Part 1
    sum = 0
    last = input[-1]

    for i in input:
        if i == last:
            sum += int(i)
        last = i

    print("solution task1: ", sum)

    # Part 2
    sum = 0
    steps = int(len(input) / 2)

    for i, j in enumerate(input):
        if j == input[(i + steps) % len(input)]:
            sum += int(j)

    print("solution task2: ", sum)
