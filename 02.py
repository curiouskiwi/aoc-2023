# Advent of Code Day 2: Cube Conundrum (https://adventofcode.com/2023/day/2)
# @curiouskiwi 2 Dec 2023

with open("2.txt", "r") as f:
    lines = f.readlines()

cube_totals = 0
power = 0
for game in lines:
    game = game.split(":")
    counter = int(game[0].split()[1])
    rounds = game[1].split(";")
    colors = {}
    for cubes in rounds:
        cubes = cubes.split(",")
        for cube in cubes:
            cube = cube.strip().split()
            result = {cube[1]: int(cube[0])}
            # update the game's maximum value for the color
            for color in result:
                colors[color] = max(colors.get(color, 0), result[color])

    # Part One
    if colors["red"] <= 12 and colors["green"] <= 13 and colors["blue"] <= 14:
        cube_totals += counter
    
    # Part Two
    power += colors["red"] * colors["green"] * colors["blue"]

print(f"part one: {cube_totals}")
print(f"part_two: {power}")
