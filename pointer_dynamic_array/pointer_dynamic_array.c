#include<stdio.h>
#include<stdlib.h>



void Episode1(){

    /* 
    array and pointer
    1. static 1d array
    2. static multi-dim array
    3. dynamic 1d array
    4. dynamic multi-dim array

    ** cpp파일을 참고 할 것.
    */

   /*
   // array를 지칭하면 첫번째 값의 주소값이다!

    //2d array
     int values[rows][cols]
    // 행 먼저 적은 주소 값으로 모두 할당 후, 열 element할당
    // int image[640][480];
    // image[n] : 1D array of 480 elements
    // image = &image[0]와 같음.
    // image + n : points to nth 1D element : &image[n]
    // *(image +n) : points to the 0th element of image[n] : image[n][0] 의 address = image[n]
    // (*(image +n) +m) :  : &image[n][m] 주소값.
    // *(*(image+n) +m) : element of image[n][m]
    */

    int values[10]; // values는 == &values[0]
    int *valPtr = values;
    printf("%p\n", values);
    printf("%p\n", &values[0]);
}


void Episode2(){
    // string array(array of characters)

    char word[10]; //9개의 글자와 마지막 \0이 들어갈 수 있는 fixed size array
    word[0] = 'w';
    word[1] = 'i';

    /*
    '': one character
    "": a string
    */

   char string[10] = "winter";
   for (int i = 0; i<10; ++i){
        printf("%c", string[i]);
   } // winter
   printf("\n");
   printf("%s\n", string); // winter


}

////////////////////////////////////////////////////////////////////////////////////////////////////
/*
call by pointer
- 참고로 call by reference는 C에서는 지원하지 않음.
*/

void swap(int firstVal, int secondVal);
void newSwap(int *firstVal, int *secondVal); // 이제는 pointer가 가리키는 메모리 공간을 직접 다룰 것임.

void Episode3()
{
    int valA = 7;
    int valB = 5;

    printf("Before Swap : valA = %d, valB = %d\n", valA, valB); // Before Swap : valA = 7, valB = 5

    swap(valA, valB);  // 내부에서 바뀌지만 메모리 직접 접근이 아니기에, 바뀌지 않음. 

    printf(" After Swap : valA = %d, valB = %d\n", valA, valB);
    // After Swap : valA = 7, valB = 5

    newSwap(&valA, &valB);
    printf(" After Swap : valA = %d, valB = %d\n", valA, valB);
    // After Swap : valA = 5, valB = 7


}

void swap(int firstVal, int secondVal)
{
    int tempVal;
    tempVal = firstVal;
    firstVal = secondVal;
    secondVal = tempVal;

    printf("In Swap : firstVal = %d, secondVal = %d\n", firstVal, secondVal);
    //In Swap : firstVal = 5, secondVal = 7
}

void newSwap(int* firstVal, int* secondVal)
{
    int tempVal;
    tempVal = *firstVal;
    *firstVal = *secondVal;
    *secondVal = tempVal;

    printf("In Swap : firstVal = %d, secondVal = %d\n", *firstVal, *secondVal);
    //In Swap : firstVal = 5, secondVal = 7
}



////////////////////////////////////////////////////////////////////////////////////////////////////
/*
<output>
Before Reverse: a = 1234, b = 67890
After Reverse: a = 4321, b = 9876
After Swap: a = 9876, b = 4321
*/
void reverse_dig(int* value);


void reverse_dig(int* value){
    /*
    10씩 나눠서 결과도 업데이트하고, 나온 나머지를 ans에 10을 곱해서 더한다.
    temp에서는 나누고 나머지 빼고(즉 몫만)
    */
    int temp = *value; // 임시 저장
    int ans = 0;
    int re;

    while(temp>0){
        re = temp%10;
        ans = ans*10 + re;
        temp/=10;
    }

    *value = ans;
}

void Episode4(){
    int a = 1234;
    int b = 67890;

    printf("Before Reverse: a = %d, b = %d\n", a, b);
    reverse_dig(&a);
    reverse_dig(&b);
    printf("After Reverse: a = %d, b = %d\n", a, b);
    newSwap(&a, &b);
    printf("After Swap: a = %d, b = %d\n", a, b);


}

////////////////////////////////////////////////////////////////////////////////////////////////////

/* 
시험 문제  :array right rotation
Sample 1) 
./rotate_array [arrays] [rotation number]
./rotate_array 4 2 8 8 3 
2 8 8 4  
 
Sample 2) 
./rotate_array 6 3 1 6 
6 3 1
*/

void Episode5(int argc, char *argv[]){
    int size = argc-2; // Size of array
    int arr[size];
    for(int i=0;i<size;i++){
        arr[i] = atoi(argv[i+1]);
    }
    int result[size]; // array you have to fill it
    int rotate = atoi(argv[size+1]); // number of rotation  

    /* Write your code here */ 

    int real_rotate = rotate % size;
    for (int i = 0; i<size; i++){
        int j  =i-real_rotate;
        if (j<0){
            j +=size;
        }
        result[i] = arr[j];
    }


    // DO NOT MODIFY BELOW!!!
    for (int i=0; i<size; i++) {
        printf("%d ", result[i]);
    }


}

////////////////////////////////////////////////////////////////////////////////////////////////////

/*
dynamic allocation in heap

array vs linked list

array는 : 메모리 사이즈가 미리 할당되어야함. 메모리 주소는 기억할 필요가 없음(바로 다음)
-> run time stack에 저장함.


Stack
// grows upward : 주소값이 줄어듬., 컴파일러가 자동적으로 함.(알아서 추가 및 삭제)

local varaible
faster and no fragmentation


linked list : 동적으로 사이즈 증가 가능.pointer 관련한 별도의 메모리가 필요.
-> HEAP에 저장함.

아래로 내려감
manually 해야함. 메모리 추각 및 삭제
global varaible access
slower and fragmented(빈공간이 생김.)

메모리 할당을 위한 코드가 필요함 . Heap, malloc
할당 결과를 항상봐야함. NULL이면 할당이 안된것임
*/

void Episode6(){

    int* intptr;
    intptr = (int*)malloc(sizeof(int));
    /*
    (datatype*)malloc(sizeof(datatype))
    */

    free(intptr);
}

/// double pointer : 주소의 주소를 말하는 격임.
void Episode7(){
    int num = 123;
    int* ptr  = &num; // address of num
    int** dptr = &ptr; // dptr : address of ptr
    /*
    (int*)* dptr이라고 생각하면 편함. int를 담는 pointer를 담는 메모리를 가리키는 포인터
    */
    int* ptr2; //pointer ptr2 선언


    printf("%p %p\n", ptr, *dptr); // 둘다 같은 값을 나타냄.
    printf("%d %d\n", num, **dptr); // 둘다 같은 값을 나타냄. 123 123 
    
    ptr2 = *dptr; //address of num = ptr

    *ptr=456; // num의 값이 바뀜.
    printf("%d %d\n",num, **dptr); // 456, 123
    
}

int main(int argc, char *argv[]){

    Episode1();
    Episode2();
    Episode3();
    Episode4();
    Episode5(argc, argv);
    Episode6();
    Episode7();


    return 0;
}