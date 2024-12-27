#include <stdio.h>
#include <stdlib.h>


/*
singly list node
each node is stack
*/


typedef struct Stack {
  int top;
  int* data;
  int capacity;
} Stack;

typedef struct ListNode {
  struct ListNode *next;
  struct Stack *stack;

} ListNode;


Stack* create_stack(int capacity){
  Stack* stack = (Stack*)malloc(sizeof(Stack));
  if(stack == NULL){
    printf("Memory allocation failed for stack.\n");
    exit(EXIT_FAILURE);
  }

  stack -> top = -1;
  stack->capacity = capacity;
  stack->data = (int*)malloc(sizeof(int)*capacity);
  if(stack->data == NULL){

    //nothing in data
    printf("Memory allocation failed for stack.\n");
    free(stack);
    exit(EXIT_FAILURE);
  }
  return stack;
}


ListNode* create_list_node(int stack_capacity){
  ListNode* node = (ListNode*)malloc(sizeof(ListNode));
  if(node == NULL){
    printf("Memory allocation failed for stack.\n");
    exit(EXIT_FAILURE);
  }

  node->stack = create_stack(stack_capacity);
  node->next = NULL;
  return node;
}





int list_size(ListNode *head) {

  /*
  count non-empty node
  */
  ListNode* currnode = head;
  int size = 0;
  
  while(currnode !=NULL){ // currnode : next to last node
    if ((currnode->stack)->top >=0){
      size++;
    }
    currnode = currnode->next;
  }
  
  return size;
}

void push_los(ListNode *head, int val) {
  /*
  push at last node stack
  */


  ListNode* currnode = head;

  // move to last node
  while(currnode ->next != NULL){
    currnode  = currnode -> next;
  }

  Stack* stack = currnode->stack;

  //if not full
  if(stack->top < stack->capacity -1){
    stack->data[++(stack->top)] = val;
  }

  //if full
  else{
    //new node
    ListNode* new_node = create_list_node(stack->capacity); // 새로만들기.
    new_node->stack->data[++(new_node->stack->top)] = val; // top index 늘리고, data에 추가하기. (늘리고 추가하기)
    currnode->next = new_node; // 이어붙이기.
    }
}

int pop_los(ListNode *head) {
  /*
  pop from last node stack
  */


  if (head == NULL){
    //nothing
    return 0;
  }


  //뺐을 때, 해당 노드가 비을 수 있기 때문에 그렇게 되면 그 노드 제거하기 : previous 추적 필요
  ListNode* prevnode = NULL;
  ListNode* currnode = head;

  //move to last node
  while(currnode->next != NULL){
    prevnode = currnode;
    currnode = currnode->next;
  }

  Stack* stack = currnode->stack;

  //checking stack is empty or not
  if(stack->top >= 0){
    int val = stack->data[(stack->top)--]; // 빼고 줄이기. (요론 디테일)
    // 비었다면 제거하기
    if(stack->top ==-1 && prevnode !=NULL){
      free(stack->data);
      free(stack);

      prevnode->next = NULL;
      free(currnode);
    }
    return val;

  }
  else{
    //stack is empty
    return -1;
  }
}


int main(){


  ListNode *head = create_list_node(3);
  if (head == NULL){
    printf("error");
  }


  printf("List size (non-empty stacks): %d\n", list_size(head)); // 0개 노드

  push_los(head, 10);
  push_los(head, 20);
  push_los(head, 30);
  push_los(head, 40); // 새로운 노드에 푸시됨

  printf("List size (non-empty stacks): %d\n", list_size(head)); // 2개 노드


  printf("Popped value: %d\n", pop_los(head));
  printf("Popped value: %d\n", pop_los(head));
  printf("Popped value: %d\n", pop_los(head));
  printf("Popped value: %d\n", pop_los(head));
  
  printf("List size (non-empty stacks): %d\n", list_size(head));


  //free memory
  ListNode* curr = head;
  while(curr != NULL){
    ListNode* temp = curr;
    curr =curr -> next;

    free(temp->stack->data);
    free(temp->stack);
    free(temp);
  }
  return -1;
}
