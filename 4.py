# Advent of Code 2023 Day 4: Scratchcards
# @curiouskiwi 4 Dec 2023

with open("4.txt", "r") as f:
    lines = f.readlines()
cards = [1] * len(lines)
part_one, part_two = 0, 0
index = -1
for line in lines:
    index += 1
    # split the line into winning numbers and my numbers
    card, numbers = line.split("|")
    winning = card.split(":")[1].split()
    mine = numbers.split()
    # how many winning numbers do I have?
    matches = len(list(filter(mine.__contains__, winning)))
    # Part One - calculate the points value for this card
    if matches > 0:
        part_one += 1<<(matches-1) # 2^(matches-1)
    # Part Two - add points to all cards after this one
    for count in range(matches):
        cards[index+1+count] += cards[index]
    part_two += cards[index]

print(f"{part_one=}")
print(f"{part_two=}")
