#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0] if length >= 1 else []

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2] if len(sequence) > 1 else 1)

    print(sequence)

    '''
    def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        sequence = [0, 1]

        for i in range(2, length):
            sequence.append(sequence[i - 1] + sequence[i - 2])

        print(sequence)
    '''


