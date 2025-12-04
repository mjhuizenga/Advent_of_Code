#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "mathops.h"

class File
{
public:
    File(const char *fname);
    ~File();

    void read_file();
    void iterate_lines(void (*func)(char *));
    void iterate_pattern(const char *pattern, void (*func)(char *));
    static void clean_line(char *line);
    TwoDArray read_into_array();
    int get_num_lines();
    int get_max_line_length();

private:
    FILE *fd;
    char **lines;

};