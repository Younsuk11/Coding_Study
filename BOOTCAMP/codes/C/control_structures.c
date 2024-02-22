// if, if-else : clarify using parentheses(괄호)
// block이 더 중요한 것. indentation 은 의미 없음.
// switch, case : same as if -else but include break, switch(default case)
/*
switch(keypress)
{
    case 1:
    //do statement
    break;
}*/


// without break, all the remaining codes in the switch statement will be excuted

//iteartions
// while statement

#include <stdio.h>
int main(void)
{
    int x = 0; // initial

    while(x <10)
    {
        printf("%d", x);
        x +=1;
    }
}

//do while statement; action performed first and the condition is tested
/* 
do{
    <loop body>
    
}while(<test>)*/


int main(void)
{
    int x =0;
    do{
        printf("%d",x);
        x+=1;
    }while(x <10);
}

//for statement
/*
For (initialization; test; update)
{
    <loop body>
}*/

int main(void)
{
    int x;
    for (x = 0; x<10 ; x++) // or int x= 0;(declaration)
    {
        printf("%d", x);
    }
}
//nested loops possible!
//break; : exit a loop or a switch statement right away
//continue; causes only the current iteration to end


