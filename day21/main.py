import sys

def print_pattern(size, pattern):
    print("the current pattern:")
    cnt = 0
    for i in pattern:
        if cnt == size:
            cnt = 0
            print()
        sys.stdout.write(i)
        cnt += 1
    print()

def print_break_stuff(amount, pattern, size):
    # print("split into " + str(int(amount)) + " grid")
    # print(pattern)
    print("break stuff")
    splits = int(int(amount) / 2)

    tmp_pattern = ""

    cnt = 0
    hori_cnt = 0
    for i in pattern:
        if cnt == size:
            if hori_cnt == 1:
                tmp_pattern += "\n"
                print()
                for _ in range(0, size + 1):
                    tmp_pattern += "-"
                    sys.stdout.write("-")
                hori_cnt = 0
            else:
                hori_cnt += 1
            tmp_pattern += "\n"
            print()
            cnt = 0
        sys.stdout.write(i)
        tmp_pattern += i
        if cnt == splits - 1 and splits != 0:
            sys.stdout.write('|')
            tmp_pattern += "|"
        cnt += 1

    print()
    tmp_pattern += "\n"
    return tmp_pattern

def check_rules(pattern, size):

    for rule in rules:

        old, new = rule.split("=>")
        old = old.strip().replace("/", "")

        new_size = len(new.strip().split("/"[0]))
        new = new.strip().replace("/", "")

        if old == pattern or old == pattern[::-1]:
            return (new, new_size)

    return (pattern, size)

def extract_one_grid(tmp_pattern):
    print(tmp_pattern)
    grid = ""
    col = 0
    row = 0
    while 1:
        if tmp_pattern[row * col + col] == '|':
            row += 1
            col += 1
        elif tmp_pattern[row * col + col] == '-' or tmp_pattern[row * col + col] == "":
            break
        else:
            grid += tmp_pattern[row * col + col]
            col += 1

    return grid


if __name__ == '__main__':

    rules = sys.stdin.readlines()

    # for rule in rules:
    #     print(rule)

    start_pattern = ".#...####"
    size = 3
    print_pattern(size, start_pattern)

    for i in range(0, 2):
        # If the size is evenly divisible by 2, break the pixels up into 2x2 squares,
        # and convert each 2x2 square into a 3x3 square by following the corresponding
        # enhancement rule.
        if size % 2 == 0:

            amount_of_two_by_two_squares = (size * size) / (2 * 2)
            tmp = print_break_stuff(amount_of_two_by_two_squares, start_pattern, size)
            tmp_grid = extract_one_grid(tmp)
            print("TMP")
            print(tmp_grid)
            start_pattern, size = check_rules(start_pattern, size)

        # Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares,
        # and convert each 3x3 square into a 4x4 square by following the corresponding
        # enhancement rule.
        elif size % 3 == 0:

            amount_of_two_by_two_squares = (size * size) / (3 * 3)
            tmp = print_break_stuff(amount_of_two_by_two_squares, start_pattern, size)
            tmp_grid = extract_one_grid(tmp)
            print("TMP")
            print(tmp_grid)
            start_pattern, size = check_rules(start_pattern, size)

        print_pattern(size, start_pattern)
