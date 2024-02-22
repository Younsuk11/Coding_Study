//array and pointer
// array이름 자체는 주소값이므로 pointer랑 비슷함.

//Example

int values[10]; // index랑 상관 없이, values는 &values[0]와 같은 것임. 즉 주소값임.
int *valPtr; // 0th element (integer를 가리키는 pointer)

//values = valPtr = &values[0]


// address of nth element = valPtr + n = values + n = &values[n]
// nth element : *(valPtr + n) = *(values + n) = values[n]

valPtr = values; // 각 주소가 할당된 이것도 address를 가지는 array가 된다.

//단, 이 이후, values를 다른 array로 reassign이 불가능 하다.(운명이 정해져있는 것임)
// Pointer는 그게 아니니, 좀 더 자유로움.


// array를 지칭하면 첫번째 값의 주소값이다!

//2d array
/* int values[rows][cols]*/
// 행 먼저 적은 주소 값으로 모두 할당 후, 열 element할당
// int image[640][480];
// image[n] : 1D array of 480 elements
// image = &image[0]와 같음.
// image + n : points to nth 1D element : &image[n]
// *(image +n) : points to the 0th element of image[n] : image[n][0] 의 address = image[n]
// (*(image +n) +m) :  : &image[n][m] 주소값.
// *((image+n) +m) : element of image[n][m]


// 주의할점.
/*
1. 모르는 값으로 선언하게 되면 안된다. -> 어느정도 예상치를 넣어줘야함.
2. size 범위를 넘어갔다고 해서 알지 못한다.(파이썬 처럼 out of range가 나오지 않음)*/

//int values[10];
//values[13] = 10; 이렇게 하면 모르는 부분의 값을 바꾸는 것이기에, 위험한 짓임.
// indexing으로 할때, 꼭 확인해야 함 0<= i < size