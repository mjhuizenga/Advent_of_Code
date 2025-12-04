#include "fileops.h"
#include "mathops.h"

void add_range(char *line);
bool is_invalid(long combo);
long power(long num, int exponent);
bool matching_combos(long combo, long pattern, long p_ten);

long count;

int main()
{
    File fd = File("02/input.txt");
    count = 0;
    fd.iterate_pattern(",", add_range);
    printf("Count:%ld\n", count);
}

void add_range(char *line)
{
    long left, right;
    sscanf(line, "%ld-%ld", &left, &right);
    // count_invalids(left, right);
    for (long i = left; i <= right; i++)
    {
        if (is_invalid(i))
        {
            count += i;
            printf("%ld, count=%ld\n", i, count);
        }
        
        if (i % 100000000 == 0)
            printf("i=%ld\n", i);
    }
}
// 1616710917 too low
// 1223028718 too low
// 37314786486

bool is_invalid(long combo)
{
    if (combo < 0)
    {
        perror("negative combo");
        return false;
    }

    int digits = snprintf(NULL, 0, "%ld", combo);
    long pattern = 0;
    int p_ten = 0;

    for (int i = 1; i < digits; i++)
    {
        if (digits % i == 0)
        {
            p_ten = power(10, i);
            pattern = combo % p_ten;
            if (matching_combos(combo, pattern, p_ten))
            {
                return true;
            }
        }
    }

    return false;
}

bool matching_combos(long combo, long pattern, long p_ten)
{
    if (combo == 0)
    {
        return true;
    }

    if (combo % p_ten == pattern)
    {
        return matching_combos(combo / p_ten, pattern, p_ten);
    }
    else
    {
        return false;
    }
}
