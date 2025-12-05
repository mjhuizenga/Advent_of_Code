#pragma once

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

long power(long num, int exponent);

/*
   yyyyyy
   012345
x0[@ @ @ ]
x1[ @ @ @]
x2[@ @ @ ]
*/

class TwoDArray
{
public:
    TwoDArray(int x, int y);
    TwoDArray();
    ~TwoDArray();

    void insert_row(int index, char *row);
    void debug();
    int num_surround_chrs(int ix, int iy, char needle);
    void iterate_cells(void (*func)(int ix, int iy, char cell));
    int count_cells_matching_surroundings(char needle, int lower, int higher, char replacement);

private:
    int x, y;
    char **arr;

};

class LongRange
{
public:
    LongRange(long start, long end);
    bool contains(long needle);

    long start, end;
};