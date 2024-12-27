#include <iostream>
#include <stack>
#include <vector>
using namespace std;

/*
24-1 Computing1 기말 시험 내용
*/
class TreeNode {
    public:
        int data;
        string color;
        TreeNode* left, *right, *parent;

        TreeNode(int data) : data(data) {
            parent = left = right = nullptr;
            color = "RED";
        }
    };

class BST {
    protected:
        TreeNode* root;
    public:
        BST() : root(nullptr) {}

        // (a) Implement the insert function
        virtual void insert(int data) { 

            TreeNode* z = new TreeNode(data);
            TreeNode* x = root;
            TreeNode* y = nullptr;
            while(x!=nullptr){
                y = x;
                if (data < x->data){
                    x = x->left;
                
                }
                else{
                    x = x->right;
                }
            }
            z->parent = y;
            if(y == nullptr){
                root = z;
            }
            else if(data < y->data){
                y->left = z;

            }
            else{
                y->right = z;
            }
            z->left = nullptr;
            z->right = nullptr;

        

        }

        void search(int num) {
            TreeNode* current = root;
            int height = 0;
            while (current != nullptr) {
                if (num == current->data){
                    cout << height;
                    return;
                }
                else if (num < current->data){
                    current = current->left;
                    height++;
                }
                else{
                    current = current->right;
                    height++;
                }
            }
            cout << "Not exist";
        }

        virtual void RBCounter(){};
    };

class RBTree : public BST { // class inheritance
    public:
        RBTree():BST(){}

        // (b) Implement the insert function
        void insert(int data) {

            TreeNode* z = new TreeNode(data);
            TreeNode* x = root;
            TreeNode* y = nullptr;
            while(x!=nullptr){
                y = x;
                if (data < x->data){
                    x = x->left;
                
                }
                else{
                    x = x->right;
                }
            }
            z->parent = y;
            if(y == nullptr){
                root = z;
            }
            else if(data < y->data){
                y->left = z;

            }
            else{
                y->right = z;
            }
            z->left = nullptr;
            z->right = nullptr;
            z->color = "RED";
            fixViolation(z);
           
            cout<<"RBT insert : "<<data<<endl;

        }

        // (c) Implement the RBCounter function
        void RBCounter(){
            //tree traversal하면서 count
            
            
            

        }

    private:
        void rotateLeft(TreeNode* &root, TreeNode* &pt) {
            TreeNode* pt_right = pt->right;

            pt->right = pt_right->left;

            if (pt->right != nullptr)
                pt->right->parent = pt;

            pt_right->parent = pt->parent;

            if (pt->parent == nullptr)
                root = pt_right;
            else if (pt == pt->parent->left)
                pt->parent->left = pt_right;
            else
                pt->parent->right = pt_right;

            pt_right->left = pt;
            pt->parent = pt_right;
        }

        void rotateRight(TreeNode* &root, TreeNode* &pt) {
            TreeNode* pt_left = pt->left;

            pt->left = pt_left->right;

            if (pt->left != nullptr)
                pt->left->parent = pt;

            pt_left->parent = pt->parent;

            if (pt->parent == nullptr)
                root = pt_left;
            else if (pt == pt->parent->left)
                pt->parent->left = pt_left;
            else
                pt->parent->right = pt_left;

            pt_left->right = pt;
            pt->parent = pt_left;
        }

        void fixViolation(TreeNode* &pt) {
       
            TreeNode* parent_pt = nullptr;
            TreeNode* grand_parent_pt = nullptr;

            while ((pt != root) && (pt->color != "BLACK") && (pt->parent->color == "RED")) {

                parent_pt = pt->parent;
                grand_parent_pt = pt->parent->parent;

                if (parent_pt == grand_parent_pt->left) {
                    TreeNode* uncle_pt = grand_parent_pt->right;

                    if (uncle_pt != nullptr && uncle_pt->color == "RED") {
                        grand_parent_pt->color = "RED";
                        parent_pt->color = "BLACK";
                        uncle_pt->color = "BLACK";
                        pt = grand_parent_pt;
                    } else {
                        if (pt == parent_pt->right) {
                            rotateLeft(root, parent_pt);
                            pt = parent_pt;
                            parent_pt = pt->parent;
                        }

                        rotateRight(root, grand_parent_pt);
                        swap(parent_pt->color, grand_parent_pt->color);
                        pt = parent_pt;
                    }
                } else {
                    TreeNode* uncle_pt = grand_parent_pt->left;

                    if (uncle_pt != nullptr && uncle_pt->color == "RED") {
                        grand_parent_pt->color = "RED";
                        parent_pt->color = "BLACK";
                        uncle_pt->color = "BLACK";
                        pt = grand_parent_pt;
                    } else {
                        if (pt == parent_pt->left) {
                            rotateRight(root, parent_pt);
                            pt = parent_pt;
                            parent_pt = pt->parent;
                        }

                        rotateLeft(root, grand_parent_pt);
                        swap(parent_pt->color, grand_parent_pt->color);
                        pt = parent_pt;
                    }
                }
            }
            root->color = "BLACK";
        }
    };






int main() {
    BST* tree = new BST;
    vector<int> node_value = {10,20,30,15,25,5,1};
    for(auto i:node_value){
        tree->insert(i);
    }
    tree->search(25); // 3



    BST* rbtree = new RBTree;
    for(auto i:node_value){
        rbtree->insert(i);
    }
    rbtree->search(25); // 2

    rbtree->RBCounter();
    return 0;
}