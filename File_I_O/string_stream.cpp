#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
std::string longest_word(std::string input_sentence){
    /*.
    sting line에서 가장 긴 단어 찾기
    */

    std::string answer;

    stringstream stream(input_sentence);
    std::string s;
    int max_l = 0;
    while (stream>>s){

        int temp = s.size(); // 공백을 기준으로 streaming, 단어 별로 분리가 가능하다.
        if (temp > max_l){
            max_l = temp;
            answer = s;
        }

    }
    return answer;

}


char most_frequent_char(std::string input_sentence){

    char answer;    

    std::map<char, int> map1;
    stringstream stream(input_sentence);
    std::string s;

    //char 개수 counting
    while(stream >> s){
        for (auto c : s){ // char
            if (map1.find(c) != map1.end()){
                map1[c] += 1;
            }
            else{
                map1[c] = 1;
            }

        }
    }
    // find most frequent
    int max_c = 0;
    for(std::pair<char, int> pair : map1){
        int cnt = pair.second;
        if (cnt> max_c){
            max_c  = cnt;
            answer = pair.first;

        }
    }
    // for (std::pair<char, int> pair : map1){
    //     cout<<pair.first<<" : " <<pair.second<<endl;
    // }

    return answer;

}





int main(int argc, char* argv[]){

    std::string line = "computing foundation for data science provides the foundational knowledge on cpp";

    std::cout << longest_word(line) << std::endl;
    std::cout << most_frequent_char(line) << std::endl;


    return 0;
    
}