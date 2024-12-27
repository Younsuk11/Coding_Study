#include <stdio.h>
#include <stdlib.h>



/*
1. Buffered I/O
- Enter를 누르기 까지 buffered
- 누르면 \n을 포함해서 전달된다.- 
- output역시 \n을 만나기 전까지 buffered

2. formatted I/O
printf("format string", values)
scanf("format string", &variable or pointer)
*/


int main(){
    FILE* file = fopen("data.txt", "r");
    if (file == NULL){
        printf("fopen error!\n");
        return 1;
    }

    char first_char = fgetc(file); // read and return a single character from a file
    /*
    char a  = fgetc(fileptr) : 읽고 반환하고, pointer는 넘어간다.
    fputc(a, fileptr); : character a 를 fileptr 가 가리키는 곳에 쓴다.
    fscanf(fileptr , "format string", variables);  : fileptr 가 가리키는 곳부터 format에 맞게 읽기
    fprintf(fileptr, "format string", variables); : fileptr 가 가리키는 곳에 쓰기.
    모두 오류가 나면 EOF를 반환한다.
    */

    int num;
    char word[20];
    int result = fscanf(file, " %d %s", &num, word); // read a file, where fileptr points
    printf("%c\n", first_char); // 4
    printf("%d\n", num); // 2
    printf("%s\n", word); //desert
    printf("%d\n", result); // 2

    return 0;



}