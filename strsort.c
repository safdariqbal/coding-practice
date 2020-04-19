#include <stdio.h>

char *strpartition(char *p, char *r) {
    char *i = p, *j = p - 1;
	char pivot = *r, tmp;
	while (i < r) {
		if (*i <= pivot) {
			j++;
			tmp = *j;
			*j = *i;
			*i = tmp;
		}
		i++;
	}
	j++;
	tmp = *j;
	*j = pivot;
	*r = tmp;
	return j;
}

void strput(char *p, char *r) {
    char *i = p;
    do {
        putc(*i, stdout);
        i++;
    } while (i != r+1);
    putc('\n', stdout);
}

void strsort(char *head, char *tail) {
	if (head >= tail) {
		return;
	}
	char *stack[64];
	int stack_idx = 0;
	char *p = head, *r = tail; 
	do {
        char *q = strpartition(p, r);
        strput(p, r);
		stack[stack_idx++] = r;
		r = q;
		if (p == r) {
			p += 1;
			r = stack[--stack_idx];
		}
	} while (stack_idx > -1);
}

int main(int argc, char *argv[]) {

    char str[] = "helloworld";
    char *end = str + 9;
    
    strsort(str, end);
    
    return 0;

}
