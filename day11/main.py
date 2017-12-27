import sys
import math

if __name__ == '__main__':

    input = sys.stdin.read().split(',')

    # https://www.redblobgames.com/grids/hexagons/

    coords = [0, 0, 0]
    furthest = 0

    for i in input:
        dir = i.strip()

        if dir == 'n':
            coords[1] += 1
            coords[2] -= 1
        elif dir == 's':
            coords[1] -= 1
            coords[2] += 1
        elif dir == 'ne':
            coords[0] += 1
            coords[2] -= 1
        elif dir == 'nw':
            coords[0] -= 1
            coords[1] += 1
        elif dir == 'se':
            coords[0] += 1
            coords[1] -= 1
        elif dir == 'sw':
            coords[0] -= 1
            coords[2] += 1

        curr = max(abs(coords[0]), abs(coords[1]), abs(coords[2]))

        if curr > furthest:
            furthest = curr

    print("part1:",max(abs(coords[0]), abs(coords[1]), abs(coords[2])))
    print("part2:", furthest)
