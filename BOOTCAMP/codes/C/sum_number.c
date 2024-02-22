// Sum of the Number

// In this problem, you have to implement the simple summation program. 
// This program has to be capable of adding all given numbers and print the result.
// Regardless how many integers are given, your program should calculate the sum of numbers.

// For input, the sequence of integers will be inserted. And output is the summation of the integer sequence. 

// Example 1:
// Input: 3 5 4 10 23
// Output: 45
// Explanation: Sum of all given number is 45
// To run:
// Compile: gcc sum_number.c -o sum_number
// Run: ./sum_number 3 5 4 10 23

// Example 2:
// Input: 6 5 8
// Output: 19
// Explanation: Sum of all given number is 19
// To run:
// Compile: gcc sum_number.c -o sum_number
// Run: ./sum_number 6 5 8

#include<stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int length = argc - 1;
    int score[length];
    for(int i=0;i<length;i++){
        score[i] = atoi(argv[i+1]); // 문자열 to 정수형
    }
    int sum = 0;
    /* Write your code here */
    for (int i =0; i < length; i++)
    {
        sum += score[i];
    }
    
    // DO NOT MODIFY BELOW!!!
    printf("%d",sum);
}