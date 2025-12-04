#include <stdio.h>
#include "fileops.h"

void count(char *line);

int cur_ind;
int zero_hits;

int main()
{
  char fname[] = "01/input.txt";
  File fd = File(fname);
  cur_ind = 50;
  zero_hits = 0;
  fd.iterate_lines(count);
  printf("Found index of %d\n", cur_ind);
  printf("Found zero_hits of %d\n", zero_hits);
}

void count(char *line)
{
  char direction = line[0];
  int distance = 0;
  int prev = 0;
  switch(direction)
  {
    case 'L':
      sscanf(line,"L%d", &distance);
      printf("Left-%d\n", distance);

      prev = cur_ind;
      cur_ind -= distance % 100;
      zero_hits += distance / 100;
      if (cur_ind < 0)
      {
        cur_ind = 100 + cur_ind;
        if (prev != 0)
          zero_hits += 1;
      }
        
      if (cur_ind == 0)
        zero_hits += 1;

      break;
    case 'R':
      sscanf(line,"R%d", &distance);
      printf("Right-%d\n", distance);

      cur_ind += distance % 100;
      zero_hits += distance / 100;
      if (cur_ind > 99)
      {
        cur_ind = cur_ind - 100;
        zero_hits += 1;
      }

      break;
    default:
      printf("Weird line: %s\n", line);
      break;
  }

  printf("cur_ind=%d, zero_hits:%d\n", cur_ind, zero_hits);
}
