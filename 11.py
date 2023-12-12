# Advent of Code Day 11: Cosmic Expansion
# @curiouskiwi 11 Dec 2023

import itertools


def main():
    grid = []
    with open('11.txt', 'r') as f:
        for line in f:
            x = line.strip().split()
            grid.append([c for c in x[0]])

    width = len(grid[0])
    height = len(grid)

    # any row or col that doesn't have a galaxy needs to be expanded 
    newrows = [r for r in range(height) if '#' not in grid[r]]
    newcols = [c for c in range(width) if '#' not in [grid[r][c] for r in range(height)]]

    # Solve for part 1 and part 2
    galaxies, count = map_galaxies(grid, height, width, newrows, newcols, 1)
    print("Part 1:", calculate_distances(galaxies, count))
    galaxies, count = map_galaxies(grid, height, width, newrows, newcols, 2)
    print("Part 2:", calculate_distances(galaxies, count))


# determine the adjustment to row,col for each galaxy based on these added rows/cols
# find number of values in sorted list that are less than or equal to a given value
#https://stackoverflow.com/a/10543316
def count_lower(sorted_list, value):
    return sum (i <= value for i in sorted_list)


def map_galaxies(grid, height, width, newrows, newcols, part):
    """map the galaxies to the new grid"""
    # using the new rows and cols, calculate the coords of each galaxy
    # for each galaxy, add the number of new rows/cols that are less than the row/col of the galaxy
    # for part 1, add 1 new row/col, for part 2 add 999999 new rows/cols
    part_multiplier = 1 if part == 1 else 999999
    count = 1;
    galaxies = {}
    for r in range(height):
        for c in range(width):
            if grid[r][c] == '#':
                x = r + (count_lower(newrows,r) * part_multiplier)
                y = c + (count_lower(newcols,c) * part_multiplier)
                galaxies[count]=(x,y)
                count += 1
    return galaxies, count


def calculate_distances(galaxies, count):
    """ calculate the sum of all the distances """
    galaxy_pairs = list(itertools.combinations(range(1, count), 2))
    # for each galaxy pair, find the shortest path between them,using the dictionary
    # of galaxy coordinates (sum of horizontal and vertical distance)
    sum = 0
    for pair in galaxy_pairs:
        x, y = pair[0], pair[1]
        sum += abs(galaxies[x][0] - galaxies[y][0]) + abs(galaxies[x][1] - galaxies[y][1])
    return sum


if __name__ == '__main__':
    main()
