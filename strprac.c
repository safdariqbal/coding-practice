#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    
    printf("%d\n", argc);
    
    if (argc < 2) {
        printf("not enough arguments\n");
        exit(-1);
    }
    
    char *str = argv[1];
    char *c = str;
    while (*c) {
        printf("%d ", *c);
        c++;
    }
    printf("\n");
    
    int n = 10;
    printf("%d\n", n++);
    printf("%d\n", n);
    printf("%d\n", ++n);
    printf("%d\n", n);
    
    return 0;
}