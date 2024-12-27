#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double loss(const std::vector<std::vector<double>>& X, const std::vector<double>& y, const std::vector<double>& w) {
    int m = X.size();  // Number of samples
    double total_cost = 0.0;
    for (int i = 0; i < m; ++i) {
        double prediction = 0.0;
        for (int j = 0; j < X[i].size(); ++j) {
            prediction += w[j] * X[i][j];
        }
        double error = prediction - y[i];
        total_cost += error * error;
    }
    return total_cost / (2 * m);
}

// (To implement) - This function should return the weights of linear model as a vector
std::vector<double> gradientDescent(const std::vector<std::vector<double>>& X, const std::vector<double>& y, std::vector<double>& w, double alpha, int num_iters) {

    //X : 2차원 vector (N, d)
    // y: 1차원 vector (N, 1)
    //w : 이전 iteration weight
    //alpha : learning rate
    //num_iterations


    //mse loss gradient : dL/dw  = -2/n x(y-wx) : -2/n X^T(y- XW)

    int N = X.size();// number of samples
    int d = X[0].size();


    for (int iter = 0; iter<num_iters; ++iter){
        vector<double> temp; // (N, 1)
        double xw;
        double s;
        vector<double>gradients(d, 0.0);


        //gradient computation
        for (int i = 0; i< N; ++i){
            xw = 0;
            for (int j = 0; j< d; ++j){
                xw += X[i][j] * w[j];
            }
            temp.push_back(y[i] - xw);
        }

        for (int j = 0; j<d; ++j){
            s = 0;
            for (int i = 0; i< N; ++i){
                s += X[i][j]*temp[i];
            }
            gradients[j] = (-2.0/N*s);
        }


        //parameter step
        for (int j =0 ; j<d; ++j){
            w[j] -= alpha*gradients[j];
        }
    }
    return w;
}