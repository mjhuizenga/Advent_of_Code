#include "fileops.h"
#include "mathops.h"
#include "linkedlist.h"

void parser(char *line);
void count_ranges();
bool sort_ascending();

LinkedList fresh_ranges;
long count;

// 35111979995710 is too low
// 35824021552703 is too low
// 325882625213520 is too low
// 325400476911257
int main()
{
    printf("Day 05 of Advent of Code 2025!\n");

    count = 0;
    File fd = File("05/input.txt");

    fd.iterate_lines(parser);

    count_ranges();

    printf("Count:%ld\n", count);
}

void parser(char *line)
{
    if (line[0] == '\n')
    {
        printf("--------------\n");
    }
    else if (strchr(line, '-') != NULL)
    {
        // remember the range
        long start, end;
        sscanf(line, "%ld-%ld\n", &start, &end);
        printf("%ld-%ld\n", start, end);
        fresh_ranges.push(new LongRange(start, end));
    }
}

void count_ranges()
{
    long i = 0;
    while (!sort_ascending())
    {
        printf("Pass through: %ld\n", i);
        i++;
    }

    Node *ptr = fresh_ranges.head;
    long tracker = 0;
    while (ptr != NULL)
    {
        LongRange *cur_range = (LongRange *)ptr->value;
        long tmp = count;
        // 520945760876904 is interesting
        if (tracker >= cur_range->start && tracker < cur_range->end)
        {
            count += cur_range->end - tracker;
            tracker = cur_range->end;
        }
        else if (tracker < cur_range->start)
        {
            count += cur_range->end - cur_range->start + 1;
            tracker = cur_range->end;
        }
        printf("%ld-%ld : %ld : %ld\n", cur_range->start, cur_range->end, tracker, count - tmp);
        ptr = ptr->next;
    }
}

bool sort_ascending()
{
    bool sorted = true;
    Node *ptr = fresh_ranges.head;
    while (ptr != NULL && ptr->next != NULL)
    {
        long first = ((LongRange *)(ptr->value))->start;
        long second = ((LongRange *)(ptr->next->value))->start;
        if (second < first)
        {
            // swap them
            fresh_ranges.swap_with_next(ptr);
            sorted = false;
        }

        ptr = ptr->next;
    }

    return sorted;
}