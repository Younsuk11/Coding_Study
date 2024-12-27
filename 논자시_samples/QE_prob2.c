#include <stdio.h>

typedef struct Number {
  int val;
} Number;

void set_number(Number *n, int val) {
  n->val  = val;
}

int get_number(Number *n) {
  return (*n).val;
}

void add(Number *n1, Number *n2, Number *n3) {
  int new_val = n1->val + n2->val;
  n3->val = new_val;
}