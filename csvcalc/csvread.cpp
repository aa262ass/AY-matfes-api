#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <sstream>

using namespace std;
void v_print(vector<double> &v){
  int vl = v.size();
  for(int i = 0; i < vl; i++){
    cout << v[i] << " ";
  }
  cout << endl;
}
vector<double> str_split(string &str){
  vector<double> data;
  int sl = str.size();
  int first = 0;
  int i = 0;
  for(; i <= sl; i++){
    if(str[i] == ',' || str[i] == '\0'){
      if(first != 0){
        string buf = str.substr(first, i-first);
        buf.push_back('\0');
        stringstream ss;
        ss << buf;
        double tmp = 0.0;
        ss >> tmp;
        data.push_back(tmp);
      }
      first = i+1;
    }
  }
  v_print(data);
  return data;
}

int main(){
  ifstream ifs("data.csv");
  string str;
  while(ifs && getline(ifs, str)){
    cout << str << endl;
    str_split(str);
  }

  return 0;
}
