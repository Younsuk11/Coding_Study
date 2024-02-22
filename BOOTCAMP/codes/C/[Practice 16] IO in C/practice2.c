#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*
[Practice] Simple English Capitalization Rule

In English writing, each sentence must start with a capital letter, and all other alphabetic characters within the sentence should be lowercase. 
Your task is to write a program to enforce this rule by checking text in a .txt file.

Criteria:
- Each line (separated by '\n') in the given text file represents a separate sentence. 
- The first character of each line (if it's an alphabet) must be uppercase.
- All other alphabetic characters in the line must be lowercase.
- Characters that are not alphabets are not considered for errors.

Sample 1)
---------------input.txt---------------
If you please--draw me A sheep!
what!
Draw me a SheeP!
----------------------------------------
./run input.txt
Total error : 4 

Sample 2)
---------------input.txt---------------
0a000b
#$%
----------------------------------------
./run input.txt
Total error : 0

Hint 1) To check if a char is an alphabet, use isalpha(ch).
Hint 2) To check if a char is an uppercase alphabet, use isupper(ch).
*/


int main(int argc, char *argv[]){
    if(argc == 1 || argc > 3){ 
        printf("Invalid Command!\n"); 
        return -1;
    }

    FILE *file = fopen(argv[1], "r");

    /* Write your code here */







    return 0;
}