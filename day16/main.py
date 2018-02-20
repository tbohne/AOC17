import sys

def swap_elements(program_seq, move):
    # converts string to list
    tmp_seq = list(program_seq)
    tmp = tmp_seq[int(move[0])]
    tmp_seq[int(move[0])] = tmp_seq[int(move[1])]
    tmp_seq[int(move[1])] = tmp
    # converts list back to string
    program_seq = ''.join(tmp_seq)
    return program_seq

if __name__ == '__main__':

    program_seq = 'abcdefghijklmnop'
    dance_moves = sys.stdin.read().strip().split(',')

    for move in dance_moves:
        move = move.replace(' ', '')
        # spin case
        if move[0] == 's':
            spin_size = int(move.replace('s', ''))
            # reverses the string
            rev_seq = program_seq[::-1]
            tmp_program = ''

            for i in range(spin_size):
                tmp_program += rev_seq[i]
            for i in range(len(program_seq) - spin_size):
                tmp_program += program_seq[i]

            program_seq = tmp_program

        # exchange case
        elif move[0] == 'x':
            move = move.replace('x', '')
            move = move.split('/')
            program_seq = swap_elements(program_seq, move)

        # partner case
        elif move[0] == 'p':
            indices = []
            move = move[1:]
            for c in move:
                if c in program_seq:
                    indices.append(program_seq.find(c))
            print(indices)
            program_seq = swap_elements(program_seq, indices)

    print(program_seq)
