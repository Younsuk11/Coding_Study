#include <stdio.h>
#include <stdbool.h>

int GlobalVar;

int main(void)
{
    int x = 1;
    int y;
    int z;

    printf("x is %d, y is %d, z is %d\n", x, y, z);
    //x is 1, y is 37404472, z is 1

    y = x++ ; // x = 2, y = 1
    printf("x is %d, y is %d, z is %d\n", x, y, z);

    z = ++y; // y = 2, x = 2
    printf("x is %d, y is %d, z is %d\n", x, y, z);

    return 0;
}

//output
/* x is 1, y is 1, z is 40566784
x is 2, y is 1, z is 40566784
x is 2, y is 2, z is 2*/


// x-> y evaluation이 되었기 때문에?