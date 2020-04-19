#include <stdio.h>
#include <limits.h>

int main(int argc, char** argv) {
    short z = 5;
    int a = 10;
    long b = 20;
    long long c = 30000;
    short *ptr = &z;
    printf("%lu, %lu, %lu, %lu, %lu\n\n", sizeof(z), sizeof(a), sizeof(b), sizeof(c), sizeof(*ptr));
    printf("%d, %d\n", INT_MIN, INT_MAX);
    printf("%u, %u\n", 0, UINT_MAX);
    printf("%d, %d\n", SHRT_MIN, SHRT_MAX);
    printf("%u, %u\n", 0, USHRT_MAX);

    int arr[3];
    arr[0] = 45;
    arr[1] = 20;
    arr[2] = 67;

    int idx = 2;
    int val = arr[idx];
    int *ptr = arr;

    printf("%d\n", val);

    printf("%lu\n", sizeof(idx));
    printf("%lu\n", sizeof(ptr));

    return 0;
}
