// python 의 class와 비슷하면서 좀 더 원시적인 형태, 단 method는 없음.

//여러가지 데이터 타입을 하나의 그룹으로 묶는 법

//Definition
struct studentType // 여기까지가 데이터 타입임.
{
    char name[10];
    int midterm;
    //...
};

//Declaration

struct studentType student A;
//Accessing
student.name = "inhoe"; // 

// 메모리 관점에서
// runtime stack에서는 뒤에 나오는 변수가 적은 메모리에 할당이 되는데, 전체 그룹이 마치
// array처럼 할당이 된다.(가장 작은 index가 가장 작은 주소값


/* 
typedef <type> <name> : 타입명을 커스텀 화

Typedef struct studentType Student; -> Student만 쓰면 됌.
*/


// array를 지원함
Student s[5]; // s[0] ~ s[4] all student type

Student s;
Student *sPtr = %s;
//Memeber access
// (*sPtr).midterm or sPtr -> midterm