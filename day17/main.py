def spinlock_p1(steps, times):
    seq = ["0"]
    pos = 0
    for i in range(1, times):
        pos = (pos + steps) % len(seq)
        seq.insert(pos + 1, str(i))
        pos += 1
    return seq

def spinlock_p2(steps, times):
    pos = 0
    val = 0
    for i in range(1, times):
        pos = (pos + steps) % i
        pos += 1
        if pos == 1:
            val = i
    return val

if __name__ == '__main__':
    steps = 394
    times_p1 = 2018
    times_p2 = int(50e6) + 1
    seq = spinlock_p1(steps, times_p1)
    idx = seq.index("2017") + 1
    print("solution part1: " + seq[idx])
    print("solution part2: " + str(spinlock_p2(steps, times_p2)))
