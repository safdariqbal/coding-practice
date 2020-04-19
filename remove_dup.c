#include <stdio.h>
#include <string.h>

void removeDup(char *str) {
    
    if (strlen(str) < 2) {
        return;
    }
    
    char *i = str + 1, *j, *tail = str + 1;
    
    while (*i) {
        j = str;
        while (j != tail) {
            if (*i == *j) {
                break; // duplicate found, breaking prevents j becoming == tail
            }
            j++;
        }
        if (j == tail) { // char at i is not a duplicate
            *tail = *i;
            tail++;
        }
        i++;
    }
    *tail = '\0';
    
}

int main(int argc, char *argv[]) {
    
    char *str = argv[1];
    removeDup(str);
    
    printf("%s\n", str);
    
    return 0;
}