import sys

def visit(i, dict, already_visited):

    if i in already_visited:
        return
    already_visited.append(i)

    for j in dict[i]:
        visit(j, dict, already_visited)

if __name__ == '__main__':

    input = sys.stdin.readlines()
    dict = dict()

    for i in input:
        tuple = i.strip().split('<->')
        tmp_list = []
        for j in tuple[1].split(','):
                tmp_list.append(j.strip())
        dict[tuple[0].strip()] = tmp_list

    # Part1
    already_visited = []
    visit('0', dict, already_visited)
    print("part1:", len(already_visited))

    # Part2
    already_visited = []
    groups = 0
    for i in dict.keys():
        if i not in already_visited:
            visit(i, dict, already_visited)
            groups += 1
    print("part2:", groups)
