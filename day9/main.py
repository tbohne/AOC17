import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    print(input.strip())

    final_score = 0
    tmp_score = 0
    garbage_mode = False
    skip_next = False

    for c in input:
        if garbage_mode != True:
            if c == '{':
                tmp_score += 1
                final_score += tmp_score
            if c == '}':
                tmp_score -= 1
            if c == '<':
                garbage_mode = True
        else:
            if skip_next == True:
                skip_next = False
            elif c == '!':
                skip_next = True
            elif c == '>':
                garbage_mode = False
            else:
                skip_next = False

    print(final_score)
