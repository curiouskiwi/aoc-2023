// Advent of Code Day 6: Wait For It
// @curiouskiwi 6 Dec 2023

#include <stdio.h>
#include <math.h>

long calculate_wins(long time, long distance);

typedef struct game {
    long time;
    long distance;
} game;

int main(void){

    game games[] = {
        { redacted, redacted },
        { redacted, redacted },
        { redacted, redacted },
        { redacted, redacted },
        { redacted, redacted }
    };
    int p1 = 1;
    for (int i = 0; i < 4; i++) 
    {
        p1 *= calculate_wins(games[i].time, games[i].distance);
    }
    printf("Part 1: %d\n", p1);

    // Part two
    long p2 = calculate_wins(games[4].time, games[4].distance);
    printf("Part two: %li\n", p2);

    return 0;
}


long calculate_wins(long time, long distance) {
    long wins = 0;
    int had_win = 0;
    for (long i = 0; i < time-1; i++) {
        if ((time-i-1) * (i+1) > distance){
            had_win = 1;
            wins++;
        }
        else if (had_win)
            break;
    }
    return wins;
}
