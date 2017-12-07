import sys

if __name__ == '__main__':

    input = sys.stdin.read()
    arr = list(map(int, input.split()))

    # Part 1
    solutions = []
    redistributions = 0

    finished = False
    val = 0

    while not finished:
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

        for (key, value) in solutions:
            if key == arr:
                print("already in there")
                finished = True
                val = value

        solutions.append((arr.copy(), redistributions))

    print("number of redistributions: ", redistributions)
    print("number of redistributions between: ", redistributions - val)
