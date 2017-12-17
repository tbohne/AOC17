import sys
from collections import *
import itertools

stuff = []

# Part 1
def solve_part1(arr):
    sol1 = ""
    for i in input:
        if "->" in i:
            x = i.strip().split("->")
            arr.append(x)

    not_in = True
    for i in arr:
        for j in arr:
            if i != j:
                if i[0].split()[0] in j[1]:
                    not_in = False
        if not_in:
            sol_with_num = i[0]
            sol1 = i[0].split()[0]
            print("solution part1: ", sol1)
        not_in = True
    return sol_with_num

# Part2
class Node:
    def __init__(self, name, weight):
        self.name = name
        self.children = []
        self.weight = weight

    def add_child(self, child):
        self.children.append(child)

    def get_weight(self):
        sum = self.weight
        for i in self.get_children_weights():
            sum += i
        return sum

    def get_children_weight(self):
        if (len(self.children) != 0):
            children_weights = []
            for child in self.children:
                children_weights.append(child.get_weight())
            return get_children_weights
        else:
            return [0]

def solve_part2(root, arr, node_dict, first_root, layer, test_vals):

    global stuff

    print("REC", root)
    sum_for_root = 0

    tmp_vals = []

    for i in arr:
        if i[0] == root:
            next_level = i[1].split(',')
            for j in next_level:
                for k in arr:
                    if j.strip() in k[0]:
                        solve_part2(k[0], arr, node_dict, first_root, layer + 1, test_vals)
            # print("rec done", root)
            # sum = 0
            for l in next_level:
                if root not in first_root:
                    tmp = node_dict[l.strip()].replace('(', '').replace(')', '')
                    # print("l: ", l, " --> ", tmp)
                    sum_for_root += int(tmp)
                    tmp_vals.append(int(tmp))
                    solve_part2(l + ' ' + node_dict[l.strip()], arr, node_dict, first_root, layer + 1, test_vals)
                    # sum += int(node_dict[l.strip()].replace('(', '').replace(')', ''))
            # if root not in first_root:
                # print(sum + int(node_dict[root.split()[0]].replace('(', '').replace(')', '')))
    sum_for_root += int(node_dict[root.split()[0]].replace('(', '').replace(')', ''))
    tmp_vals.append(int(node_dict[root.split()[0]].replace('(', '').replace(')', '')))
    # print("SUM FOR REC: ", sum_for_root)
    layer = 0
    if len(tmp_vals) > 1:
        print("END REC: ", root, "weight: ", sum(tmp_vals))
        del tmp_vals[-1]
        stuff += tmp_vals
        # print(stuff)

    if root in important:
        # print("RESET", root)
        stuff = []

if __name__ == '__main__':

    input = sys.stdin.readlines()
    arr = []
    sol_with_num = solve_part1(arr)

    # Part 2
    # We will have to build up the tree

    root_with_num = sol_with_num
    first_root = root_with_num
    print(first_root)
    # print("root: ", root_with_num)

    node_dict = dict()

    for i in input:
        x = i.split()
        node_dict[x[0]] = x[1]

    layer = 0

    important = ""
    for i in arr:
        important += i[0]

    test_vals = []

    current = root_with_num
    solve_part2(root_with_num, arr, node_dict, first_root, layer, test_vals)
