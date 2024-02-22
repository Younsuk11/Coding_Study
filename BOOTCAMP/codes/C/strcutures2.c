// Array version grading -> Structure version

#include <stdio.h>

#define STUDENT_NUMS 5

struct studentType{
    char name[50];
    int ID;
    int midterm;
    int final;
    int total;

};
typedef struct studentType Student;

void calculateTotal(Student *s);


int main(void)
{

    //define array of student
    Student s[STUDENT_NUMS];

    //receive inputs
    for(int i =0; i < STUDENT_NUMS; i++)
    {
        printf("input for student #%d", i);
        printf("\t name : ");
        scanfe("%s", s[i].name);
        printf("\t ID : ");
        scanfe("%s", s[i].ID);
        printf("\t midterm : ");
        scanfe("%s", s[i].midterm);

        printf("\t final : ");
        scanfe("%s", s[i].final);


    }


    //calculate total
    for (int i = 0; i<STUDENT_NUMS; i++)
    {
        calculateTotal(&s[i]); //pointer address input
    }

    //print each total score
    for (int i = 0; i<STUDENT_NUMS; i++)
    {
        printf("total score for student #%d(%s) is %d\n", i, s[i].name, s[i].total);
    }


    return 0;
}

// Define caculate Total
void calculateTotal(Student *s) // value가 아닌 student type의 s를 가리키는 pointer 임.
{
    s->total = s->midterm + s->final;
}
