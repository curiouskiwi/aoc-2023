# Advent of Code Day 10: Pipe Maze
# @curiouskiwi 10 Dec 2023

def main():
    grid = []
    with open('10.txt', 'r') as f:
         for line in f:
              x = line.strip().split()
              grid.append([c for c in x[0]])

    width = len(grid[0])
    height = len(grid)
    # create a 2d array to keep track of walls for part 2
    mapped = [[False]*width for _ in range(height)]
    
    print('Part1:', part1(grid,mapped,width,height))
    print('Part 2:', part2(grid,mapped))
    
    for r in range(height):
        for i in range(width):
            if mapped[r][i] is True:
                mapped[r][i] = '#'
            else:
                mapped[r][i] = grid[r][i]
    print('\n'.join([''.join([str(c) for c in row]) for row in mapped]))


def part1(grid, mapped, width, height):
    """find the max distance from start by following the entire path"""
    """then divide the steps by 2"""
    # find starting point
    for h in range(height):
        for w in range(width):
            if grid[h][w] == 'S':
                S = (h,w)
                break

    # start off from S. Mark that cell as part of the pipe for part 2
    mapped[S[0]][S[1]] = True
    dest, camefrom = start(grid,S,mapped)
    counter = 1
    # follow the only path available without going backwards
    while True:
        dest,camefrom = go(grid,dest,camefrom,mapped)
        counter += 1
        if dest == S:
            break

    # we are now back the beginning, so the path length is half the counter
    return counter//2


def start(grid, S, mapped):
    """find the second cell in the loop, keeping track of the direction we came from"""
    """it's a closed loop so we know we can only go 2 directions, so just pick the first one"""
    # check if we can go right
    if grid[S[0]][S[1]+1] in ['-', 'J', '7']:
        S = (S[0], S[1]+1)
        came_from = 'l'

    # check if we can go left
    elif grid[S[0]][S[1]-1] in ['-', 'L','F']:
        S = (S[0], S[1]-1)
        came_from = 'r'

    # check if we can go up
    elif grid[S[0]-1][S[1]] in ['|', '7', 'F']:
        S = (S[0]-1, S[1])
        came_from = 'd'

    # check if we can go down
    elif grid[S[0]+1][S[1]] in ['|', 'L', 'J']:
        S = (S[0]+1, S[1])
        came_from = 'u'

    return S, came_from


def go(grid, S, camefrom, mapped):
    """move to the next cell in the loop without going back"""
    """keeping track of the direction we came from for next time"""
    src = grid[S[0]][S[1]]
    back = S[0], S[1]
    # check if we can go right
    if camefrom != 'r' and src in ['-', 'L','F']:
        S = (S[0], S[1]+1)
        came_from = 'l'

    # check if we can go left
    elif camefrom != 'l' and src in ['-', 'J', '7']:
        S = (S[0], S[1]-1)
        came_from = 'r'

    # check if we can go up
    elif camefrom != 'u' and src in ['|','L', 'J' ]:
        S = (S[0]-1, S[1])
        came_from = 'd'

    # check if we can go down
    elif camefrom != 'd' and src in ['|', '7', 'F']:
        S = (S[0]+1, S[1])
        came_from = 'u'

    # mark the cell as part of the pipe so we can use that in part 2
    mapped[back[0]][back[1]] = True
    return S, came_from


def part2(grid, mapped):
    """count the number of cells with an odd number of crossings before it"""
    """if the crossing count is odd, that means the cell is inside the loop"""
    """ https://en.wikipedia.org/wiki/Point_in_polygon# (ray-casting algo)"""
    crossing, counter = 0, 0
    mark = ''
    for h in range(len(grid)):
        for w in range(len(grid[0])):
            cell=grid[h][w]
            if mapped[h][w] is True:
                # figure out if its a crossing
                if cell == '|': crossing += 1
                elif cell == 'L': mark = 'L' # only a crossing if followed by a 7
                elif cell == 'F': mark = 'F' # only a crossing if followed by a J 
                elif cell == '7' and mark == 'L': crossing += 1
                elif cell == 'J' and mark == 'F': crossing += 1
            else:
                if crossing % 2 !=0: counter += 1
        crossing = 0
        mark = ''
    return counter


if __name__ == '__main__':
    main()
