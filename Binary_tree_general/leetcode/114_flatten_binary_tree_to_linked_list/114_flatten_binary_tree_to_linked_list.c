#include <stdio.h>
#include <stdlib.h>


typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}TreeNode;

TreeNode* prev = NULL;
void flatten(struct TreeNode* root) {
    

    if(root == NULL) return;

    flatten(root->right);
    flatten(root->left);

    root->right = prev;
    root->left = NULL;
    prev = root;
}