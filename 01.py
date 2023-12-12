# AOC 2023 Day 1: Trebuchet?!
# @curiouskiwi 1 Dec 2023

def main():
    with open("1.txt", "r") as f:
        data = f.read().split("\n")

    one_total = 0
    two_total = 0
    for line in data:
        one_total += part1(line)
        two_total += part2(line)
    print("Part One:", one_total)
    print("Part Two:", two_total)


def part1(line):
    # remove all non-digits from line
    line = ''.join(filter(str.isdigit, line))
    try:
        return int(line[0]+line[-1])
    # if there are no digits in the line
    except IndexError:
        return 0


def part2(line):
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, 
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
            "7": 7, "8": 8, "9": 9}
    min_position = len(line)
    max_position = -1
    first = 0
    last = 0
    # check every possible number in the line
    for word,num in nums.items():
        # search from the beginning to find the first number
        left_idx = line.find(word)
        if left_idx != -1 and left_idx <= min_position:
            min_position = left_idx
            first = num
        # search from the end to find the last number
        right_idx = line.rfind(word)
        if right_idx > max_position:
            max_position = right_idx
            last = num
    return first * 10 + last


if __name__ == "__main__":
    main()
