# Advent of Code Day 8: Haunted Wasteland
# @curiouskiwi  8 December 2023

import math

def main():
    with open('8.txt') as f:
        line = f.readline()
        directions = line.strip()
        blank = f.readline()
        path = {}
        while True:
            line = f.readline()
            if not line:
                break
            node, choices = line.split("=")
            node = node.strip()
            choices = choices.lstrip(' (').rstrip(')\n').split(', ')
            path[node] = choices

    # Part 1
    start=['AAA']
    print("Part 1:", followthemap(start, directions, path, 'ZZZ')[0])
    
    # Part 2
    starts = []
    for v in path.keys():
        if v.endswith('A'):
            starts.append(v)

    allsteps = followthemap(starts, directions, path, 'Z')
    # least common multiple of allsteps
    print("Part 2:", math.lcm(*allsteps))


def followthemap(nodes, directions, path, end):
    """Follows the map from start to end, returns number of steps"""

    dlen = len(directions)
    nextplace = []
    for node in nodes:
        nextplace.append(node) 
    allsteps = []
    # Run paths for every start node
    for n in range(len(nodes)):
        for i in range(dlen*1000):
            if directions[i%dlen] == 'L':
                nextplace[n] = path[nextplace[n]][0]
            elif directions[i%dlen] == 'R':
                nextplace[n] = path[nextplace[n]][1]
            if nextplace[n].endswith(end):
                allsteps.append(i+1)
                break
    return allsteps


if __name__ == '__main__':
    main()
