import sys

if __name__ == '__main__':

    input = sys.stdin.read()
    arr = list(map(int, input.split()))

    # Part 1
    solutions = []
    redistributions = 0

    while True:
        print(arr)
        max_num = max(arr)
        print("max num: ", max_num)
        idx = arr.index(max_num)
        print("idx: ", idx)

        arr[idx] -= max_num

        offset = 1
        while max_num > 0:
            arr[(idx + offset) % len(arr)] += 1
            offset += 1
            max_num -= 1

        redistributions += 1

        if arr in solutions:
            print("already in there")
            break

        solutions.append(arr.copy())

    print("number of redistributions: ", redistributions)
