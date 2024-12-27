#include <iostream> 
#include <algorithm>
#include <string>
#include <vector>
#include <chrono>
#include <cctype>

using namespace std; 
using namespace std::chrono;


using namespace std; 

/*
24-1 computing 1 final 기출
*/


vector<int> computeWays(const std::string expression);

vector<int> computeWays(const std::string expression){

    vector<int> ans; 

    // if (expression.find("+") != string::npos &&expression.find("-") != string::npos&& expression.find("*") != string::npos){
    //     ans = {std::stoi(expression)};
    //     return ans;
    // }

    bool check = true;
    for(char c : expression){
        if(!std::isdigit(c)){
            check=false;
            break;
        }
    }
    if (check){
        ans = {std::stoi(expression)};
        return ans;
    }
    


    ans = {};
    for (int i = 0 ; i < expression.size(); ++i){
        char s =expression[i];
        if(s == '+' || s == '-' || s== '*'){
            vector<int> left = computeWays(expression.substr(0, i)); // expression[:i] i개 만큼만
            vector<int> right = computeWays(expression.substr(i+1, expression.size() - (i+1))); // expression[i+1:] i+1에서 N-(i+1)만큼만


            for(int l : left){
                for (int r : right){
                    if (s == '+'){
                        ans.push_back(l+r);
                    }
                    else if(s=='-'){
                        ans.push_back(l-r);
                    }
                    else{
                        ans.push_back(l*r);
                    }
                }
            } 
        }
    }

    return ans;   
}




void printVec(const vector<int> inputVec){

    int prev = -1E+9;

    for (auto i: inputVec){

        if (i == prev) continue; //중복 출력 안할려고.
        prev = i;

        std::cout << i << " ";
    }
}

  
// Driver program to test above functions 
int main(int argc, char * argv[]) 
{ 
    string expression = "2-1-1";
    // string expression = "2*3-4*5";
    vector<int> ans = computeWays(expression);

    sort(ans.begin(), ans.end());
    printVec(ans);

    return 0; 
} 