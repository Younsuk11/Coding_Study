#include <stdio.h>

int inGlobal;

int main()
{
    int inLocal = 5;
    int outLocalA;
    int outLocalB;

    inGlobal = 3;

    outLocalA = inLocal * inGlobal; //15
    outLocalB = inLocal & inGlobal; //논리 연산 -> 1(not True, False)

    printf("outLocalA = %d , outLocalB = %d\n", outLocalA, outLocalB);

    return 0;
}