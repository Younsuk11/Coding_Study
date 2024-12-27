#include<iostream>
#include<vector>
#include<queue>

using namespace std;    


class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        
        // default : max_heap
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq; //min heap {sum , i, j}

        int n  = nums1.size();
        int I;
        if (n>=k) {I = k;}
        else{I = n;}

        for (int i = 0 ; i<I ; i++){

            pq.push({nums1[i] + nums2[0], {i, 0}});
            cout<<nums1[i]<<endl;

        }

        vector<vector<int>> res;
        while(!pq.empty() && res.size()<k){

            auto top = pq.top();
            int s = top.first;
            int i = top.second.first;
            int j = top.second.second;
            pq.pop();

            vector<int>temp{nums1[i], nums2[j]};
            res.push_back(temp);

            //추가
            if (j+1 < nums2.size()){
                pq.push({nums1[i] + nums2[j+1], {i, j+1}});
            }
        }
        return res;
    }
};