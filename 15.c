// Advent of Code 2023: Day 15 Lens Library
// @curiouskiwi 15 Dec 2023

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef struct lens {
    char label[10];
    int focal;
    bool skip;
    struct lens *next;
} lens;

lens *boxes[256];

int part1hash;

int hash(char *label);
lens *find_lens(char *label, lens *box);
void handle_lens(lens *l);
lens *create_lens(char *x);
int calculate_total();
int number_of_lenses(lens *box);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./15 filename\n");
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    char buffer[23000];
    fgets(buffer, 23000, f);
    char *x = strtok(buffer, ",");
    lens *new = create_lens(x);
    handle_lens(new);
    while ((x = strtok(NULL, ",")))
    {
        new = create_lens(x);
        handle_lens(new);
    }
    fclose(f);

    printf("part one: %i\n", part1hash);
    printf("part two: %i\n", calculate_total());
    return 0;
}


// create the lenses
lens *create_lens(char *x)
{
    part1hash += hash(x);
    lens *l = malloc(sizeof(lens));
    if (l == NULL)
    {
        return NULL;
    }
    char label[10];
    int focal = 0;
    bool skip = false;
    for (int i = 0; i < strlen(x); i++)
    {
        if (isalpha(x[i]))
        {
            label[i] = x[i];
        }
        else if (x[i] == '-')
        {
            label[i] = '\0';
            skip = true;
        }
        else if (x[i] == '=')
        {
            label[i] = '\0';
            focal = x[i+1] - '0';
        }
    }
    strcpy(l->label, label);
    l->focal = focal;
    l->skip = skip;
    return l;
}


// hash the label
int hash(char *label)
{
    int h = 0;
    for (int i = 0; i < strlen(label); i++)
    {
        h = (label[i] + h * 17) % 256;
    }
    return h * 17 % 256;
}


// insert the box into the hash table
void handle_lens(lens *l)
{
    lens *box = boxes[hash(l->label)];
    lens *temp = find_lens(l->label, box);
    // if focal > 0, if the lens is in the hash table, update the focal length
    if (temp)
    {
        if (l->skip) // remove the lens from the box
        {
            temp->skip = true;
        } 
        // if the lens is in the box, update the focal length
        else
        {
            temp->focal = l->focal;
        }
    }
    // else if the lens is not in the box, add it to the box
    else if (l->skip == false)
    { 
        int h = hash(l->label);
        l->next = boxes[h];
        boxes[h] = l;
    }
    return;
}


lens *find_lens(char *label, lens *box)
{
    while (box)
    {
        if (strcmp(box->label, label) == 0 && box->skip == false)
        {
            return box;
        }
        box = box->next;
    }
    return NULL;
}


int calculate_total()
{
    int total = 0;
    for (int i = 0; i < 256; i++)
    {
        lens *box = boxes[i];
        int counter = number_of_lenses(box);
        while (box)
        {
            if (box->skip == false)
            {
                total += (i + 1)  * box->focal * counter--;
            }   
            box = box->next;
        }
    }
    return total;
}


int number_of_lenses(lens *box)
{
    int counter = 0;
    while (box)
    {
        if (box->skip == false)
        {
            counter++;
        }
        box = box->next;
    }
    return counter;
}
