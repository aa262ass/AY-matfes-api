#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv){
  if(argc != 3){
    cerr << "input file names" << endl;
    return 1;
  }
  ifstream ifs1, ifs2;
  ofstream ofs;
  try{
    ifs1.open(argv[1]);
    ifs2.open(argv[2]);
    ofs.open("merged.csv");
  }
  catch(char *e){
    cout << e << endl;
    return 1;
  }
  string str;
  while(ifs1 && getline(ifs1, str)){
    ofs << str << endl;
  }
  while(ifs2 && getline(ifs2, str)){
    ofs << str << endl;
  }
  ifs1.close();
  ifs2.close();
  ofs.close();
  return 0;
}
