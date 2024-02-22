//one character
//putchar : print 한 글자(아스키 코드로도 가능)
//getchar : 한글짜 얻기 -> return its ASCII value

// Buffered I/O
//Enter를 누르기 까지 buffered
// 누르면 \n을 포함해서 전달된다.
//output역시 \n을 만나기 전까지 buffered





// formatted I/O
/* 
printf("format string", values)
scanf("format string", &variable or pointer)
*/



//I/O from files
/* 
File pointer : *filePtr

filePtr = fopen("file name", "mode") :
mode : r, w, a, r+(reading and writing)*/

/* 
if (filePtr = NULL)
    printf("fopen erro!\n")*/


// char a = fgetc(filePtr);
//한 글자만 읽는다. 읽을 데이터가 없으면 EOF을 출력

//fputc(a, filePtr) : 한 글자 쓰기

//fscanf(filePtr, "format string", variables):  파일을 읽고, string을 varaible에 저장

//fprintf(filePtr, "format string", variables) : wrting 파일



//example
#include <stdio.h>

int main(void)
{
    FILE *infile;
    FILE *outfile;

    char str[50]; // 50글자의 string array

    infile = fopen("input.txt", "r");  //읽기
    outfile = fopen("output.txt", "w"); // 쓰기

    while(fscanf(infile,"%s", str)!=EOF) // white space일때까지 읽는다. (한 단어씩 읽고 전진)
    {
        fprintf(outfile, "%s ", str); // 쓰기
    }

    return 0;
}