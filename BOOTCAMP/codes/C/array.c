/*Array

constrast to lists in python
1. 오로지 한 데이터 타입만 가능
2. fixed size

//int arr[SIZE] = {3,1,4,6,5,9,2};

declaration
int grid[8];
1. 가장 첫번째 grid[0]는 가장 작은 주소로 할당 in run-time stack
*/

//example
#include <stdio.h>
#define NUM_STUDENTS 5 // fixed constant

int main(void){
    int midterm[NUM_STUDENTS];
    int final[NUM_STUDENTS];
    int total[NUM_STUDENTS];

    //input exam scores
    for(int i = 0; i <  NUM_STUDENTS; i++)
    {
        printf("input midterm score for student %d", i);
        scanf("%d", &midterm[i]);
        printf("input final score for student %d" ,i);
        scanf("%d", &final[i]); // 직접 받아서 각 array의 메모리에 할당
    }

    //calculate total scores
    for(int i =0; i<NUM_STUDENTS; i++)
    {
        total[i] = midterm[i] + final[i];

    }
    
    //output the total scores

    for(int i=0; i<NUM_STUDENTS; i++)
    {
        printf("Total score for Student %d is %d\n", i, total[i]);
    }

    return 0;
}



// Array - string (array of characters)
/*
char word[10]; Declaration

word[0] = 'w' ; word[1] = 'i'; 이런 식으로 한글자식 assign을 해야한다.
\0 : special character : null character(sentinel로, string의 끝을 알려주는 역할을 한다., 무조건 하나는 필요함)
따라서 word는 9글자까지밖에 저장을 못함.

printf("%s", word);


char work[10] = "winter"; 이렇게 직접 선언도 가능
'': one character
"": a string
\0이 자동적으로 맨 마지막에 할당 됨.*/