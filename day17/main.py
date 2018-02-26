def spinlock(steps, times):
    seq = []
    seq.append("0")
    pos = 0
    for i in range(1, times):
        pos = (pos + steps) % len(seq)
        seq.insert(pos + 1, str(i))
        pos += 1
    return seq

if __name__ == '__main__':
    steps = 394
    times = 2018
    seq = spinlock(steps, times)
    idx = seq.index("2017") + 1
    print("solution part1: " + seq[idx])
