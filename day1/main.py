import sys

if __name__ == '__main__':
    input = sys.stdin.readlines()

    str_list = list(input[0].strip())
    print(str_list)

    sum = 0

    if str_list[0] == str_list[len(str_list) - 1]:
        sum += int(str_list[0])

    for i in range(0, len(str_list) - 1):
        if str_list[i] == str_list[i + 1]:
            sum += int(str_list[i])

    print(sum)
