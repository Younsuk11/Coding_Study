#include <stdio.h>
#include <stdlib.h>

/*
[Practice] Reverse Linked List

Given numbers of linked list, reverse the list, and print it.

Sample 1)
./run 1 2 3 4 5
output : 5 4 3 2 1

Sample 2)
./run 10 20 30
output : 30 20 10
*/


/* Linked list node structure */
typedef struct nodeType LinkedNode;
struct nodeType{
    int val;
    LinkedNode *next;
};

/* Function to create a new node */
LinkedNode *createNode(int x){
    LinkedNode *newNode = (LinkedNode *)malloc(sizeof(LinkedNode));
    newNode->val = x;
    newNode->next = NULL;
    return newNode;
}

int main(int argc, char* argv[])
{  
    int length = argc - 1;

    /* Create a linked list from input integers */
    LinkedNode *head = NULL;
    LinkedNode *prev = NULL;
    LinkedNode *curr = NULL;

    for (int k = 1; k <= length; k++) {
        LinkedNode *temp = createNode(atoi(argv[k]));
        if (k > 1){
            prev->next = temp;
        }
        else {
            head = temp;
        }
        prev = temp;
    }

    /* Write your code here */	
    // Since printing starts at 'LinkedNode *head', it must point to the first node of the linked list.










    // DO NOT MODIFY BELOW!!!
    
    curr = head;
    while (curr){
        printf("%d ", curr->val);
        curr = curr->next;
    }

    return 0;
}
