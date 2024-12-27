#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <map>
#include <iostream>
#include <random>

using namespace std;

class KNN {
public:
    KNN(int k, string metric);
    void train(const vector<vector<double>>& X, const vector<int>& y);
    int infer(const vector<double>& x) const;
private:
    int k;
    string metric;
    vector<vector<double>> train_X;
    vector<int> train_y;

    double euclideanDistance(const vector<double>& a, const vector<double>& b) const;
    double cosineSimilarity(const vector<double>& a, const vector<double>& b) const;
};

KNN::KNN(int k, string metric) : k(k), metric(metric) {}

void KNN::train(const vector<vector<double>>& X, const vector<int>& y) {
    train_X = X; // 2차원 vector (150, 4)
    train_y = y; // 1차원 vector(150, )
}

// To implement
int KNN::infer(const vector<double>& x) const {

    //use sort function from algorithm library
    // tie-breaking : by randomly seleting one class among the tied classes
    //when there are the same number of instances for multiple classes

    //compute for each other....
    
    int N = this->train_X.size();
    double distance; // for each distance between train X and y
    vector<pair<double, int>> total;



    for (int i=0; i<N; ++i){
        if (this->metric =="E"){
            distance = euclideanDistance((this->train_X)[i], x); //작을 수록 가까운것.
        }
        else if (this->metric=="C"){
            distance = 1-cosineSimilarity((this->train_X)[i], x); // 클수록 가까운것.-> 작을 수록 가까운 것으로 바꿔야함.
        }
        total.push_back({distance, (this->train_y)[i]});
    }
    
   

    //sorting ascending order by distance
    sort(total.begin(), total.end());

    //select first K neighbors
    total.resize(this->k);



    //get frequency of labels : unordered_map을 쓴 이유 : 해시 테이블 기반 O(1) 연산 가능. map은 binary tree형태임.
    map<int, int> freq_labels;
    for (auto& t : total){
        freq_labels[t.second]++;
    }

    //maximum freq label
    vector<int>max_classes;
    int max_freq = 0;
    for (auto& pair : freq_labels){
        if(max_freq < pair.second){
            max_freq = pair.second;
        }
    }

    for (auto& pair: freq_labels){
        if (max_freq==pair.second){
            max_classes.push_back(pair.first);
        }
        else continue;
    }

    if (max_classes.size() == 1){
        return max_classes[0];
    }
    else{
        //random select(tie-breaking)
        random_device rd;
        mt19937 gen(rd());
        int size= max_classes.size();

        uniform_int_distribution<int> dist(0, size-1);
        int random_idx = dist(gen);
        return max_classes[random_idx];
    }

}

// Euclidean distance function(To implement)
double KNN::euclideanDistance(const vector<double>& a, const vector<double>& b) const {

    //using sqrt from cmath library
    double distance = 0;

    int n = a.size();
    for(int i =0; i<n ; ++i){
        distance += pow(a[i]- b[i], 2);
    }
    return sqrt(distance);

}

// Cosine similarity function(To implement)
double KNN::cosineSimilarity(const vector<double>& a, const vector<double>& b) const {

    //using inner_product form numeric library
    double dot = inner_product(a.begin(), a.end(), b.begin(), 0);

    double norm_a = 0;
    double norm_b = 0;

    norm_a = sqrt(inner_product(a.begin(), a.end(), a.begin(), 0));
    norm_b = sqrt(inner_product(b.begin(), b.end(), b.begin(), 0));

    return dot / (norm_a * norm_b);

}