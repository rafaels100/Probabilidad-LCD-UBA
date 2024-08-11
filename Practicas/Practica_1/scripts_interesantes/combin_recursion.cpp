#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
/*
Tiro un dado de {1, 2, ..., N} caras unas n veces.
*/
int N = 4;
int n = 3;
vector<int> camino(n);
vector<vector<int>> S;
int contador = 0;
void rec_con_repo(int i){
  if (i < 0) {
    S.push_back(camino);
    return;
  }
  for (int k = 0; k < N; k++) {
    camino[i] = k;
    rec_con_repo(i-1);
  }
  return;
}


vector<int> U = {0, 1, 2, 3};
void rec_sin_repo(int i){
  if (i == n) {
    S.push_back(camino);
    return;
  }
  for (int elem : U) {
    if (! (find(camino.begin(), camino.begin() + i, elem) != camino.begin() + i)) {
      //cout << "Entro" << endl;
      camino[i] = elem;
      rec_sin_repo(i + 1);
    }
  }
  return;
}


int main(){
  rec_con_repo(n - 1);
  for (int i = 0; i < S.size(); i++) {
    for (int j = 0; j < S[i].size(); j++) {
      cout << S[i][j] << " ";
    }
    cout << endl;
  }
  cout << "Cardinal de S con reposicion es: " << S.size() << endl;
  
  S.clear();
  rec_sin_repo(0);
  for (int i = 0; i < S.size(); i++) {
    for (int j = 0; j < S[i].size(); j++) {
      cout << S[i][j] << " ";
    }
    cout << endl;
  }
  cout << "Cardinal de S sin reposicion es: " << S.size() << endl;
}
