#include "fileops.h"

File::File(const char* fname)
{
    fd = fopen(fname, "r+");
    if (!fd)
        perror("fopen");
}

File::~File()
{
    fclose(fd);
}

void File::read_file()
{
    char line[256] = {0};
    while (fgets(line, sizeof(line), fd) != NULL)
        printf("line: %s", line);
}

void File::iterate_lines(void (*func)(char *))
{
    char line[256] = {0};
    while (fgets(line, sizeof(line), fd) != NULL)
        func(line);

    fseek(fd, 0, SEEK_SET);
}

void File::iterate_pattern(const char *pattern, void (*func)(char *))
{
    char line[2046] = {0};
    char *ptr, *token;
    while (fgets(line, sizeof(line), fd) != NULL)
    {
        for (ptr = line; ; ptr = NULL)
        {
            token = strtok(ptr, pattern);
            if (token == NULL)
                break;
            printf("Searching [%s]\n", token);
            func(token);
        }
    }

    fseek(fd, 0, SEEK_SET);
}

void File::clean_line(char *line)
{
    line[strcspn(line, "\n\0")] = '\0';;
}

TwoDArray File::read_into_array()
{
    int x, y, i=0;
    x = get_num_lines();
    y = get_max_line_length();
    TwoDArray arr = TwoDArray(x, y);
    char *line = (char *)calloc(y + 2, sizeof(char));
    while (fgets(line, y + 2, fd) != NULL)
    {
        clean_line(line);
        arr.insert_row(i, line);
        i++;
    }

    fseek(fd, 0, SEEK_SET);
    free(line);
    return arr;
}

int File::get_num_lines()
{
    int num_lines = 1;
    char cur = fgetc(fd);
    while (cur != EOF)
    {
        if (cur == '\n')
            num_lines++;
        
        cur = fgetc(fd);
    }
    
    fseek(fd, 0, SEEK_SET);
    return num_lines;
}

int File::get_max_line_length()
{
    int max_len = 0;
    int cur_len = 0;
    char cur = fgetc(fd);
    while (cur != EOF)
    {
        if (cur != '\n')
            cur_len++;
        else
            cur_len = 0;
        
        if (cur_len > max_len)
            max_len = cur_len;

        cur = fgetc(fd);
    }
    
    fseek(fd, 0, SEEK_SET);
    return max_len;
}