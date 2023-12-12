// Advent of Code 2023 Day 5: If You Give A Seed A Fertilizer
// @curiouskiwi 5 Dec 2023
// (brute force in part 2 ... consider rewriting)

#include <stdio.h>
#include <stdlib.h>

// sample data
#define SEEDS 4
#define SOILS 2
#define FERTILIZERS 3
#define WATERS 4
#define LIGHTS 2
#define TEMPERATURES 3
#define HUMIDITIES 2
#define LOCATIONS 2

long calc(long input, int num, long arr[][3]);

int main(void)
{
    // Sample Data
    long seeds[SEEDS] = {79,14,55,13};
    long seed_to_soil[SOILS][3] = {{50,98,2},{52,50,48}};
    long soil_to_fertilizer[FERTILIZERS][3] = {{0,15,37},{37,52,2},{39,0,15}};
    long fertilizer_to_water[WATERS][3] = {{49,53,8},{0,11,42},{42,0,7},{57,7,4}};
    long water_to_light[LIGHTS][3] = {{88,18,7},{18,25,70}};
    long light_to_temperature[TEMPERATURES][3] = {{45,77,23},{81,45,19},{68,64,13}};
    long temperature_to_humidity[HUMIDITIES][3] = {{0,69,1},{1,0,69}};
    long humidity_to_location[LOCATIONS][3] = {{60,56,37},{56,93,4}};
    
    // part 1    
    long min_location_so_far = 0;
    for (int i = 0; i < SEEDS; i ++) {
        long seed = seeds[i];
        long soil = calc(seed, SOILS, seed_to_soil);
        long fertilizer = calc(soil, FERTILIZERS, soil_to_fertilizer);
        long water = calc(fertilizer, WATERS, fertilizer_to_water);
        long light = calc(water, LIGHTS, water_to_light);
        long temperature = calc(light, TEMPERATURES, light_to_temperature);
        long humidity = calc(temperature, HUMIDITIES, temperature_to_humidity);
        long location = calc(humidity, LOCATIONS, humidity_to_location);

        // set first minimum to first seed's location
        if (i == 0) {
            min_location_so_far = location;
        } else {
            if (location < min_location_so_far) {
                min_location_so_far = location;
            }
        }
    }
    printf("part one: %ld\n", min_location_so_far);


    // part 2
    min_location_so_far = 0;
   // calculate the location for each seed, but only store the minimum location
    for (int i = 0; i < SEEDS; i +=2) {
        for (long j = seeds[i]; j < seeds[i] + seeds[i+1]; j++) {
            long seed = j;
            long soil = calc(seed, SOILS, seed_to_soil);
            long fertilizer = calc(soil, FERTILIZERS, soil_to_fertilizer);
            long water = calc(fertilizer, WATERS, fertilizer_to_water);
            long light = calc(water, LIGHTS, water_to_light);
            long temperature = calc(light, TEMPERATURES, light_to_temperature);
            long humidity = calc(temperature, HUMIDITIES, temperature_to_humidity);
            long location = calc(humidity, LOCATIONS, humidity_to_location);

            // set first minimum to first seed's location
            if (i == 0 && j == seeds[i]) {
                min_location_so_far = location;
            } else {
                if (location < min_location_so_far) {
                    min_location_so_far = location;
                }
            }
        }
    }
     
    printf("part two: %ld\n", min_location_so_far);
    return 0;
}


    long calc(long input, int num, long arr[][3])
    {
        // TODO
        long output = input;
        for (int i = 0; i < num; i++) {
            long start = arr[i][1];
            long end = arr[i][1] + arr[i][2];

            if (input >= start && input < end) {
                output = arr[i][0] + (input - start);
                break;
            }
        }
        // if no matches, return output as input
        return output; 
    }
