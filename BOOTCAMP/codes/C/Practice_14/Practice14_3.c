#include <stdio.h>
#include <stdlib.h>


// 재귀함수 : 피보나치 수열



int fibonacci(int n){
/* Please write your code below */	

	//base case
	if(n==1 || n==2)
	{
		return 1;
	}
	else//recursively 
	{

		return fibonacci(n-1) + fibonacci(n-2);
	}


	


/* Do not modify below */
}


/* Do not modify below */
int main(int argc, char* argv[]){
	/* 
	argc: Stores the number of program arguments. 
	argv[]: Array for storing program arguments. 
	The first value of argv[] is the name of program. 
	That is, if there is no argument, argc is 1 and argv[0] is the name of program. 
	*/

	// If the number of argument is not 2
	if (argc != 2){
		printf("Enter any natural number n\n");
		return 0;
	}

	// Store the first argument into the variable n
	int n = atoi(argv[1]);		

	// If n is smaller than 0
	if (n < 0){
		printf("No negative number is allowed\n");
		return 0;

	} else {
		// Variable for storing fibonacci value
		int f = 0;
		// Execute the fibonacci function and store the result into variable f
		f = fibonacci(n);
		// Print the answer 
		printf("%d\n",f);
		return 0;
	}
}

