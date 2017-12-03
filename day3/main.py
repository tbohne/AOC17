import sys
import math

if __name__ == '__main__':

    input = 265149

    # Part 1
    i = 1
    while (i * i < input):
        i * i
        i += 2
    square = i * i
    print("The smallest odd square the input fits into: ", square)

    pos_on_spiral_arm = 0
    tmp_square = square
    # The spiral always has 4 arms
    spiral_arm = 1
    while (tmp_square != input):
        tmp_square -= 1
        pos_on_spiral_arm += 1
        if pos_on_spiral_arm == i - 1:
            spiral_arm += 1
            pos_on_spiral_arm = 0

    edge_of_arm = square - (spiral_arm - 1) * (i - 1)
    mid_of_arm = edge_of_arm - math.floor((i) / 2)

    # Position in the sequence of odd squares.
    mid_distance_to_center = math.ceil(i / 2) - 1

    # Steps from the curr pos to the arm's mid.
    steps = 0
    if mid_of_arm < input:
        while mid_of_arm < input:
            mid_of_arm += 1
            steps += 1
    if mid_of_arm > input:
        while mid_of_arm > input:
            mid_of_arm -= 1
            steps += 1

    sol = mid_distance_to_center + steps
    print(sol)

    # Part2
    https://oeis.org/A141481
