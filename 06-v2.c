// Advent of Code Day 6 - Wait For It
// @curiouskiwi 6 Dec 2023
// quadratic formula version

#include <stdio.h>
#include <math.h>

long wins(long a, long b, long c);

typedef struct game {
    double time;
    double distance;
} game;

int main(void){

    game games[] = {
        {redacted, redacted},
        {redacted, redacted},
        {redacted, redacted},
        {redacted, redacted},
        {redacted, redacted}
    };
    // Part 1
    long part1 = 1;
    for (int i = 0; i < 4; i++)
        part1 *= wins(1, 2-games[i].time, games[i].distance-games[i].time-1);
    printf("Part one: %ld\n", part1);
    // Part 2
    long part2 = wins(1, 2-games[4].time, games[4].distance-games[4].time-1);
    printf("Part two: %ld\n", part2);
    return 0;
}

// use quadratic formula to calculate the number of wins
// int a = 1;
// long b = 2 - games[i].time;
// long c = games[i].distance - games[i].time - 1;
// long discriminant = b*b - 4*a*c;

long wins(long a, long b, long c) {
    long discriminant = b*b - 4*a*c;
    double j1 = (-b + sqrt(discriminant)) / (2*a);
    double j2 = (-b - sqrt(discriminant)) / (2*a);
    return floor(j1) - ceil(j2) + 1;
}
