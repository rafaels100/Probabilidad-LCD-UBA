#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  vector<int> v = {0, 1, 2, 3};
  int i = 2;
  cout << (find(v.begin(), v.begin() + i, 2) != v.begin() + i) << endl;
  
  cout << *(v.end()-1) << endl;
}
