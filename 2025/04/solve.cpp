#include "fileops.h"
#include "mathops.h"

int count;

int main()
{
    printf("Day 04 of Advent of Code!\n");

    File fd = File("04/input.txt");
    // fd.iterate_lines(parser);
    TwoDArray arr = fd.read_into_array();
    count = 0;
    arr.debug();
    int replaced = arr.count_cells_matching_surroundings('@', 0, 3, 'x');
    count += replaced;
    while (replaced > 0)
    {
        replaced = arr.count_cells_matching_surroundings('@', 0, 3, 'x');
        count += replaced;
    }

    // arr.num_surround_chrs(0, 2, '@');
    printf("Count:%d\n", count);
    // arr.debug();
}
