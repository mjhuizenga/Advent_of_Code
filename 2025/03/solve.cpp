#include "fileops.h"
#include "mathops.h"

void get_joltage(char *line);
int i_highest(char *str1, int len, long mult);

long count;

int main()
{
    File fd = File("03/input.txt");
    count = 0;
    fd.iterate_lines(get_joltage);
    printf("Count:%ld\n", count);
}

void get_joltage(char *line)
{
    line[strcspn(line, "\n\0")] = '\0';
    char *next_range = line;

    for (int i = 12; i > 0; i--)
    {
        next_range = next_range + i_highest(next_range, strlen(next_range) - i + 1, power(10, i-1)) + 1;
    }
}

int i_highest(char *str1, int len, long mult)
{
    char *ptr = str1;
    int highest = 0;
    int current = 0;
    int index = 0;
    for(int i = 0; i < len; i++)
    {
        current = (int)(ptr[i] - '0');
        if (current > highest)
        {
            highest = current;
            index = i;
        }
    }
    printf("Looking at [%s], found %d\n", str1, highest);
    count += highest * mult;
    return index;
}