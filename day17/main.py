def spinlock(steps, times):
    seq = []
    seq.append("0")
    pos = 0
    for i in range(1, times):
        print(i)
        pos = (pos + steps) % len(seq)
        seq.insert(pos + 1, str(i))
        pos += 1
    return seq

if __name__ == '__main__':
    steps = 394
    times_p1 = 2018
    times_p2 = int(50e6)
    seq = spinlock(steps, times_p1)
    idx = seq.index("2017") + 1
    print("solution part1: " + seq[idx])

    seq = spinlock(steps, times_p2)
    idx = seq.index("0") + 1
    print("solution part2: " + seq[idx])
