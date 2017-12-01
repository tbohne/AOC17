import sys

if __name__ == '__main__':
    input = sys.stdin.readlines()

    str_list = list(input[0].strip())
    print(str_list)

    sum = 0
    steps = int(len(str_list) / 2)

    for i in range(0, len(str_list)):
        if str_list[i] == str_list[(i + steps) % (len(str_list))]:
            sum += int(str_list[i])

    print(sum)
