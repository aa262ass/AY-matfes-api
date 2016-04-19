#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char **argv){
  if(argc != 2){
    cout << argc << "error" << endl;
    return 0;
  }

  ifstream ifs(argv[1]);
  string buf;

  while(ifs && getline(ifs, buf)) {
    cout << buf << endl;
  }

  return 0;



}
