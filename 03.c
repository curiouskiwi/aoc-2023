// Advent of Code Day 3: Gear Ratios
// @curiouskiwi 3 Dec 2023

#include <stdio.h>
#include <ctype.h>

typedef struct enginepart {
    int num;
    int marker; 
} enginepart;

#define SIZE 140

void print_markers(int dim, int grid[dim][dim]);
void print_grid(int dim, char grid[dim][dim]);

int main(void)
{
    // Create grid and fill with dots including an extra row/column around entire thing
    // to avoid boundary problems when checking surrounding cells
    char grid[SIZE+2][SIZE+2];
    for (int i = 0; i < SIZE+2; i++) {
        for (int j = 0; j < SIZE+2; j++) {
            grid[i][j] = '.';
        }
    }
    // now replace the dots with the file data
    FILE *f = fopen("3.txt", "r");
    for (int i = 0; i < SIZE; i++) {
        fscanf(f, "%s", &grid[i+1][1]);
        // replace the nul terminator with a dot
        grid[i+1][SIZE+1] = '.';
    }
    fclose(f);

    // Create a grid of markers to indicate it's an engine part and which gear it belongs to
    int markers[SIZE+2][SIZE+2];
    int starcount = 0;
    
    for (int i = 1; i <= SIZE; i++) {
        for (int j = 1; j <= SIZE; j++) {
            int found_star = 0;
            if (ispunct(grid[i][j]) && grid[i][j] != '.') {
                // special handling for part 2
                if (grid[i][j] == '*') {
                    found_star = 1;
                    starcount++;
                } 
            // mark surrounding
                for (int k = i-1; k <= i+1; k++) {
                    for (int l = j-1; l <= j+1; l++) {
                        if (found_star) markers[k][l] = starcount;
                        else markers[k][l] = 999;
                    }
                }
            }
        }
    }

    // now find all the numbers
    // array to hold all the valid part_numbers found with their associated marker
    enginepart n[2000] = {0};

    int marker = 0, ctr = 0;
    int num = 0, found = 0;
    // loop through the grid looking for digits
    for (int i = 0; i < SIZE+1; i++) {
        for (int j = 0; j < SIZE+1; j++) {
            // calculate the number and set found if on a marker
            if (isdigit(grid[i][j])) {
                num = num * 10 + grid[i][j] - '0';
                // if the digit is the first one found on a marker, store the marker
                if ((markers[i][j] > 0) & !found) {
                    marker = markers[i][j];
                    found = 1;
                }
            }
            // if we have a valid part number, store it in the array
            else if (found) {
                n[ctr].num = num;
                n[ctr].marker = marker;
                ctr++;
                num = 0;
                found = 0;
            }
            // otherwise reset to look for the next number
            else {
                num = 0;
            }
        }
    }

    // sort the array by enginepart.marker to find the pairs (the gears)
    for (int i = 0; i < ctr+1; i++) {
        for (int j = i+1; j < ctr+1; j++) {
            if (n[i].marker > n[j].marker) {
                enginepart temp = n[i];
                n[i] = n[j];
                n[j] = temp;
            }
        }
    }
    // add up all the numbers
    int part_one = 0;
    int part_two = 0;
    for (int i = 0; i < ctr+1; i++) {
        // for part 1 just add up all the numbers
        part_one += n[i].num;
        // for part 2, if the 2 parts are on the same gear, multiply them and add to total
        if (n[i].marker == n[i+1].marker && n[i+1].marker != 999) {
            part_two += n[i].num * n[i+1].num;
        }
    }
    printf("part 1: %i\n", part_one);
    printf("part 2: %i\n", part_two);
}


void print_markers(int dim, int grid[dim][dim]) {
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            printf("%03i ", grid[i][j]);
        }
        printf("\n");
    }
}

void print_grid(int dim, char grid[dim][dim]) {
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            printf("%c ", grid[i][j]);
        }
        printf("\n");
    }
}
