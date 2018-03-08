import sys

def find_start(start_row):
    for i in range(0, len(start_row)):
        if start_row[i] == '|':
            return i

if __name__ == '__main__':

    input = sys.stdin.readlines()
    grid = []

    for row in input:
        grid.append(row)

    start_idx = find_start(grid[0])
    print(start_idx)
    row = 0
    col = start_idx
    y_pos = 0
    x_pos = start_idx
    direction = 'd'
    res = ""

    while True:
        print("dir: " + direction + " pos : " + str(y_pos) + " - " + str(x_pos))
        if direction == 'd':
            if y_pos + 1 >= len(grid) or x_pos >= len(grid[y_pos + 1]) or grid[y_pos + 1][x_pos].strip() == "":
                if x_pos - 1 >= 0 and grid[y_pos][x_pos - 1].strip() != "":
                    print(grid[y_pos][x_pos - 1])
                    direction = 'l'
                    continue
                else:
                    direction = 'r'
                    continue
            else:
                y_pos += 1
        elif direction == 'u':
            if y_pos - 1 < 0 or x_pos >= len(grid[y_pos - 1]) or grid[y_pos - 1][x_pos].strip() == "":
                if x_pos - 1 >= 0 and grid[y_pos][x_pos - 1].strip() != "":
                    direction = 'l'
                    continue
                else:
                    direction = 'r'
                    continue
            else:
                y_pos -= 1
        elif direction == 'l':
            if x_pos - 1 < 0 or grid[y_pos][x_pos - 1].strip() == "":
                if y_pos - 1 >= 0 and x_pos < len(grid[y_pos - 1]) and grid[y_pos - 1][x_pos].strip() != "":
                    direction = 'u'
                    continue
                else:
                    direction = 'd'
                    continue
            else:
                x_pos -= 1
        elif direction == 'r':
            if x_pos + 1 >= len(grid[y_pos]) or grid[y_pos][x_pos + 1].strip() == "":
                if y_pos - 1 >= 0 and x_pos < len(grid[y_pos - 1]) and grid[y_pos - 1][x_pos].strip() != "":
                    direction = 'u'
                    continue
                else:
                    direction = 'd'
                    continue
            else:
                x_pos += 1

        if grid[y_pos][x_pos] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if grid[y_pos][x_pos] in res:
                print(res)
                break

            print("add: " + grid[y_pos][x_pos])
            res += grid[y_pos][x_pos]

        elif grid[y_pos][x_pos] == '+':

            if y_pos - 1 >= 0 and x_pos < len(grid[y_pos - 1]) and grid[y_pos - 1][x_pos].strip() != "" and direction != 'd':
                direction = 'u'
            elif y_pos + 1 < len(grid) and x_pos < len(grid[y_pos + 1]) and grid[y_pos + 1][x_pos].strip() != "" and direction != 'u':
                direction == 'd'
            elif x_pos + 1 < len(grid[y_pos]) and grid[y_pos][x_pos + 1].strip() != "" and direction != 'l':
                direction == 'r'
            elif x_pos - 1 > 0 and grid[y_pos][x_pos - 1].strip() != "" and direction != 'r':
                direction  == 'l'
