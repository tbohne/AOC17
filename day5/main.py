import sys

if __name__ == '__main__':

    # Part 1
    input = sys.stdin.readlines()
    nums = list(int(i.strip()) for i in input)
    tmp_nums = nums.copy()

    idx = 0
    steps = 0
    while idx >= 0 and idx < len(tmp_nums):
        offset = tmp_nums[idx]
        tmp_nums[idx] = offset + 1
        idx += offset
        steps += 1

    print(steps)

    # Part 2
    idx = 0
    steps = 0
    tmp_nums = nums.copy()
    while idx >= 0 and idx < len(tmp_nums):
        offset = tmp_nums[idx]
        if offset >= 3:
            tmp_nums[idx] = offset - 1
        else:
            tmp_nums[idx] = offset + 1
        idx += offset
        steps += 1

    print(steps)
