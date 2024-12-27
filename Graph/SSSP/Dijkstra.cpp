#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <climits>

using namespace std;


void flightRoute(const int n, const int m, const vector<vector<int>> & route_info);


void flightRoute(const int n, const int m, const vector<vector<int>> & route_info)
{

    //single source shortest path : Dijkstra algorithm
    /*
    n : number of cities
    m : number of flights
    route_info : {a,b,c}: 
    a : source 
    b : target
    a,b : 1~n
    c : price 
    */

    //map version : key = source / value : (target, cost)
    map<int, vector<pair<int, long long>>> graph_adj;
    for(const auto& root : route_info){
        graph_adj[root[0]].push_back({root[1], root[2]});
    }


    //Initialize single source : all vertex distance inf
    vector<long long>price(n+1, LLONG_MAX); // source -> 가는 price tracking
    price[1] = 0;
    vector<long long>route_count(n+1, 0); // for counting min-price-routes from source to each vertex
    route_count[1] = 1; 
    vector<int>flights(n+1, INT_MAX); // min num of flights in a min_price route from source to each vertex
    flights[1] = 0;
    vector<int>max_flights(n+1, 0); //// max num of flights in a min_price route from source to each vertex
    max_flights[1] = 0;
    
    /* /
    Dijkstra : O((V+E)logV)*/


    //pair<price, neighbor vertex> : price = from source
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> Q;//Q for vertices
    Q.push({0,1}); // source

    while (!Q.empty()){
        
        //extract-min(Q)
        auto u = Q.top().second;
        auto curr_price = Q.top().first;
        Q.pop();


        if (curr_price > price[u]){

            /*
            from source -> u로 가는 경로가 여러 개가 존재하면서 생기는 경우임.
            내가 지금 보는 경로로 가는 것이 다른 경로에 의해 이미 minimum으로 update가 된 경우면, 넘어가는 것.
            굳이 해당 u로 가는 최소가 아닌 경로는 보지 않겠다는 의미.
            */
            continue; 
        }
        //for each vertex v adjacent to u
        for (auto it = graph_adj[u].begin();it !=graph_adj[u].end();++it ){
            long long cost  = it->second; // u->v로의 cost
            int v =it->first;


            //relaxation 가능할 때
            if (curr_price + cost < price[v]){
                price[v] = curr_price + cost; // 현재까지의 price update (decrease-key에 해당되는 내용)
                Q.push({curr_price + cost, v}); // 넣으면 price오름 차순으로 정리 (근데 넣기만 함. update가 아님.)
                
                route_count[v] = route_count[u] % 2147483647;
                flights[v] = flights[u] +1;
                max_flights[v] = max_flights[u] + 1;
            }
            else if (curr_price + cost == price[v]){
                
                route_count[v]  = (route_count[v] + route_count[u]) % 2147483647;
                flights[v] = min(flights[v], flights[u] +1);
                max_flights[v] = max(max_flights[v], max_flights[u] +1);
            }
        }
    }


    std::cout<<price[n]<<" "<<route_count[n]<<" "<<flights[n]<<" "<<max_flights[n];
 
}




int main(){

    vector<vector<int>> my_route;
    my_route.push_back(vector<int>({1,4,5}));
    my_route.push_back(vector<int>({1,2,4}));
    my_route.push_back(vector<int>({2,4,5}));
    my_route.push_back(vector<int>({1,3,2}));
    my_route.push_back(vector<int>({3,4,3}));

    flightRoute(4, 5, my_route);

    return 0;
}