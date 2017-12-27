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

    already_visited = []
    visit('0', dict, already_visited)

    print("part1:", len(already_visited))
