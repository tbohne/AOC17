import sys

if __name__ == '__main__':

    # Part 1
    input = sys.stdin.readlines()
    sum = 0
    for s in input:
        arr = list(map(int, s.strip().split()))
        diff = max(arr) - min(arr)
        sum += diff
    print("solution part1: ", sum)

    # Part2
    sum = 0
    for s in input:
        arr = list(map(int, s.strip().split()))
        for i in arr:
            for j in arr:
                if i != j and i % j == 0:
                    sum += int(i / j)
    print("solution part2: ", sum)
