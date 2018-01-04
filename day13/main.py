import sys

def calc_severity(depth_range):
    scanner_pos = dict()
    up = dict()
    for k in depth_range.keys():
        scanner_pos[k] = 0
        up[k] = True

    severity = 0
    for i in range(0, int(last) + 1):
        if str(i) in scanner_pos.keys() and scanner_pos[str(i)] == 0:
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
    print("solution part1:", severity)


def calc_delay(depth_range):

    severity = True
    delay = 0
    picosec = 0

    while severity == True:
        picosec = delay
        mypos = 0
        severity = False
        while mypos <= int(last):
            if str(mypos) in depth_range.keys():
                scanner = picosec % (2 * (depth_range[str(mypos)] - 1))
                if scanner == 0:
                    severity = True
            mypos += 1
            picosec += 1

        if severity:
            delay += 1

    print("solution part2:", delay)

if __name__ == '__main__':

    input = sys.stdin.read().strip().replace(' ', '')
    test = input.split('\n')
    depth_range = dict()
    for i in test:
        tmp = i.split(':')
        depth_range[tmp[0]] = int(tmp[1])
        last = tmp[0]

    calc_severity(depth_range)
    calc_delay(depth_range)
