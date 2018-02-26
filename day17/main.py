if __name__ == '__main__':

    seq = []
    seq.append("0")
    steps = 394
    pos = 0

    print(seq)

    for i in range(1, 2018):
        pos = (pos + steps) % len(seq)
        seq.insert(pos + 1, str(i))
        pos += 1
        print(seq)
