# Advent of Code Day 9: Mirage Maintenance
# @curiouskiwi 9 Dec 2023

import numpy as np

def main():

    p1, p2 = 0, 0
    with open('9.txt', 'r') as f:
        for line in f:
            seq = [int(x) for x in line.strip().split(' ')]
            p1 += solve(seq)
            # Part 2 can be solved simply by reversing the sequence
            seq.reverse()
            p2 += solve(seq)
    print(f"{p1=}")
    print(f"{p2=}")


def solve(seq):
    """solve the sequence"""
    ex = [seq]
    counter = 0
    while all(x == 0 for x in ex[-1]) == False:
        ex.append(np.diff(ex[-1]).tolist())
        counter += 1
    ex[counter].append(0)
    while len(ex[counter]) < len(seq):
        counter -= 1
        # append the sum of the last element in ex[counter] and the last element in ex[counter+1]
        ex[counter].append(ex[counter][-1] + ex[counter+1][-1])
    # return the calculated last new element in ex[0]
    return ex[0][-1] + ex[counter][-1]


if __name__ == '__main__':
    main()
