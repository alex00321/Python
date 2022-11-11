#include <stdio.h>

int main()
{
    // printf("hello world!\n");
    // return 0;
    int w,x,y,z;
    int i = 3; int j = 4;
    {
        int i = 5;
        w = i + j;
    }
    x = i + j;
    {
        int j = 6;
        i = 7;
        y = i + j;
    }
    z = i + j;
    printf("w is %d,x is %d,y is %d,z is %d," , w, x, y, z);
}