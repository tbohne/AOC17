import sys

if __name__ == '__main__':

    input = sys.stdin.readlines()
    arr = []

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
            print(i[0].split()[0])
        not_in = True
