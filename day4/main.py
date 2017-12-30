import sys
import math

if __name__ == '__main__':

    input2 = sys.stdin.readlines()
    num_of_valid = 0

    # Part 1
    for s in input2:
        line = s.strip().split(' ')
        valid = True
        arr = []
        for i in line:
            if i not in arr:
                arr.append(i)
            else:
                valid = False
        if valid:
            num_of_valid += 1

    print(num_of_valid)

    # Part 2
    num_of_valid = 0
    for s in input2:
        line = s.strip().split(' ')
        valid = True
        arr = []
        for word in line:
            no_anagram = True
            for used_word in arr:
                cnt = 0
                for c in used_word:
                    if c in word:
                        cnt += 1
                if cnt == len(word) and len(word) == len(used_word):
                    no_anagram = False
            if no_anagram:
                arr.append(word)
            else:
                valid = False

        if valid:
            num_of_valid += 1
        arr = []

    print(num_of_valid)
