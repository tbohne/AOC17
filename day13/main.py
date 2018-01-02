import sys

if __name__ == '__main__':

    input = sys.stdin.read().strip().replace(' ', '')
    test = input.split('\n')
    depth_range = dict()
    for i in test:
        tmp = i.split(':')
        depth_range[tmp[0]] = int(tmp[1])
        last = tmp[0]

    scanner_pos = dict()
    up = dict()
    for k in depth_range.keys():
        scanner_pos[k] = 0
        up[k] = True

    # print(scanner_pos)

    severity = 0

    for i in range(0, int(last) + 1):

        # print("picosec and also my pos:", i)
        # print("scanner_pos:", scanner_pos)
        if str(i) in scanner_pos.keys() and scanner_pos[str(i)] == 0:
            # print("collision:", i, depth_range[str(i)])
            severity += i * depth_range[str(i)]

        for k in scanner_pos.keys():
            if up[k]:
                scanner_pos[k] += 1
                if scanner_pos[k] == depth_range[k] - 1:
                    up[k] = False
            else:
                scanner_pos[k] -= 1
                if scanner_pos[k] == 0:
                    up[k] = True

        # print(scanner_pos)
    print("severity:", severity)
