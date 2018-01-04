import sys

def calc_severity(depth_range, last):
    severity = 0
    for i in range(0, int(last) + 1):
        if str(i) in depth_range.keys():
            scanner = i % (2 * (depth_range[str(i)] - 1))
            if scanner == 0:
                severity += i * depth_range[str(i)]

    print("solution part1:", severity)

def calc_delay(depth_range, last):
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

    calc_severity(depth_range, last)
    calc_delay(depth_range, last)
