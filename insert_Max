#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> sol(int num, int k){
    int tmp = num;
    int digits;
    vector<int> vec;
    if(tmp < 0){
        tmp = -tmp;
    }
    while(tmp>0){
        digits = tmp%10;
        vec.push_back(digits);
        tmp = tmp/10;
    }
    reverse(vec.begin(),vec.end());

    if(num>0){
        for(unsigned int i=0; i<=vec.size();i++){
            if(vec[i]<k || i==vec.size()){
                vec.insert(vec.begin()+i,k);
                break;
            }
        }
    }

    else{
        for(unsigned int i=0; i<=vec.size(); i++){
            if(vec[i]>k || i==vec.size()){
                vec.insert(vec.begin()+i,k);
                break;
            }
        }
    }
    return vec;
} 

int main()
{
    vector <int> myvector;
    myvector = sol(-446,5);
    cout << "Hello world!" << endl;
    for(unsigned int i=0; i<myvector.size();i++){
        cout<<myvector[i];
    }
    cout <<endl<< "Hello world!" << endl;
    return 0;
}
