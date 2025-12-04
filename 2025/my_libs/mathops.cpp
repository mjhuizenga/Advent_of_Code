#include "mathops.h"

long power(long num, int exponent)
{
    long tmp = 1;
    for (int i = 0; i < exponent; i++)
        tmp *= num;
    return tmp;
}

TwoDArray::TwoDArray(int x, int y) : x(x), y(y)
{
    if (x < 0 || y < 0)
    {
        perror("Invalid args to TwoDArray Constructor");
        return;
    }
    else if (x == 0 || y == 0 )
    {
        arr = NULL;
        return;
    }

    arr = (char **)calloc(x, sizeof(char*));
    for(int i = 0; i < x; i++)
        arr[i] = (char *)calloc(y, sizeof(char));
}

TwoDArray::~TwoDArray()
{
    if (arr != NULL)
    {
        for(int i = 0; i < x; i++)
        {
            if (arr[i] != NULL)
                free(arr[i]);
        }

        free(arr);
    }
}

void TwoDArray::insert_row(int index, char *row)
{
    if (index < x && index >= 0)
        memcpy(arr[index], row, MIN(strlen(row) * sizeof(char), y));
    else
        perror("index out of bounds for insert_row");
}

void TwoDArray::debug()
{
    for (int i = 0; i < x; i++)
    {
        printf("[%s]\n", arr[i]);
    }
}

int TwoDArray::num_surround_chrs(int ix, int iy, char needle)
{
    if (ix >= x || ix < 0 || iy >= y || iy < 0)
    {
        perror("num_surround_chars out of bounds");
        return 0;
    }

    int count = 0;
    if (ix > 0)
    {
        if (arr[ix - 1][iy] == needle)
        {
            // printf("[-1][0]\n");
            count++;
        }

        if (iy > 0)
        {
            if (arr[ix - 1][iy - 1] == needle)
            {
                // printf("[-1][-1]\n");
                count++;
            }
        }

        if (iy < (y - 1))
        {
            if (arr[ix - 1][iy + 1] == needle)
            {
                // printf("[-1][+1]\n");
                count++;
            }
        }
    }
    
    if (ix < (x - 1))
    {
        if (arr[ix + 1][iy] == needle)
        {
            // printf("[+1][0]\n");
            count++;
        }

        if (iy > 0)
        {
            if (arr[ix + 1][iy - 1] == needle)
            {
                // printf("[+1][-1]\n");
                count++;
            }
        }

        if (iy < (y - 1))
        {
            if (arr[ix + 1][iy + 1] == needle)
            {
                // printf("[+1][+1]\n");
                count++;
            }
        }
    }

    if (iy > 0)
    {
        if (arr[ix][iy - 1] == needle)
        {
            // printf("[0][-1]\n");
            count++;
        }
    }

    if (iy < (y - 1))
    {
        if (arr[ix][iy + 1] == needle)
        {
            // printf("[0][+1]\n");
            count++;
        }
    }

    return count;
}

void TwoDArray::iterate_cells(void (*func)(int ix, int iy, char cell))
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            func(i, j, arr[i][j]);
        }
    }
}

int TwoDArray::count_cells_matching_surroundings(char needle, int lower, int higher, char replacement)
{
    int cur = 0;
    int count = 0;
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if (arr[i][j] == needle)
            {
                cur = num_surround_chrs(i, j, needle);
                if (cur >= lower && cur <= higher)
                {
                    arr[i][j] = replacement;
                    count++;
                }
            }
        }
    }

    return count;
}