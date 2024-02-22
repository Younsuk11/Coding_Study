// array vs linked list

//array는 : 메모리 사이즈가 미리 할당되어야함. 메모리 주소는 기억할 필요가 없음(바로 다음)
// -> run time stack에 저장함.
// Stack
// grows upward : 주소값이 줄어듬., 컴파일러가 자동적으로 함.(알아서 추가 및 삭제)
/*
local varaible
faster and no fragmentation*/


//linked list : 동적으로 사이즈 증가 가능.pointer 관련한 별도의 메모리가 필요.
/// -> HEAP에 저장함.
/*/
아래로 내려감
manually 해야함. 메모리 추각 및 삭제
global varaible access
slower and fragmented(빈공간이 생김.)*/



// 메모리 할당을 위한 코드가 필요함 . Heap, malloc
// 할당 결과를 항상봐야함. NULL이면 할당이 안된것임
#include <stdlib.h>

int *intPtr;
intPtr =(int*)malloc(sizeof(int)); // 앞부분에 return 받을 데이터 타입도 정해줘야함.(type cast)
free(intPtr); // 메모리 삭제

Student  = *sPtr;
sPtr = (Student *)malloc(STUDENT_NUMs*sizeof(Student))
free(sPtr); // 메모리 deallocation

