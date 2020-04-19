#include <stdio.h>
#include <string.h>

#include <limits.h>

int main(int argc, char **argv)
{
    char test_str[35] = "456789098765,Read,0,456789,45678,N";
    char *tok = NULL;

    printf("original: %s\n", test_str);
    tok = strtok(test_str, ",");
    printf("after: %s\n", test_str);
    printf("%s -> %s\n", test_str, tok);
    tok = strtok(NULL, ",");
    printf("%s -> %s\n", test_str, tok);

    unsigned a = 0;
    a--;
    printf("%u\n", a);

    printf("UNIT_MAX = %u\n", UINT_MAX);
    printf("LONG_MAX = %li\n", LONG_MAX);
    printf("ULONG_MAX = %lu\n", ULONG_MAX);

    return 0;
}