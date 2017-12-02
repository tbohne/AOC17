import sys

if __name__ == '__main__':

    # Part 1
    input = sys.stdin.readlines()
    sum = 0
    for s in input:
        arr = list(map(int, s.strip().split()))
        diff = max(arr) - min(arr)
        sum += diff
    print(sum)
