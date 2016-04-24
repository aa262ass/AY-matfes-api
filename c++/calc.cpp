#include <dlib/matrix.h>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#define Feats_dim 99120
using namespace dlib;
using namespace std;

const char *filepath = "./result/descriptor.csv";

string search_max_similarity(std::vector<double> guest_feats)
{
	ifstream ifs(filepath);
	if(!ifs) {
		cerr << "Cannot open the file: " << filepath << endl;
		return "";
	}

	matrix<double, Feats_dim, 1> v1;
	matrix<double, 1, Feats_dim> v2;
	for(int i = 0; i < Feats_dim; i++)
		v1(i,0) = guest_feats[i];
	v1 /= length(v1);
	
	double max_sim;
	string line, max_name;
	max_sim = 0;

	// おとなしくfscanf使ったほうが自明に速そう
	while(getline(ifs, line)) {
		int i =  0;
		double sim;
		string str, name = "";
		istringstream ss(line);
		while(getline(ss,str,',')) {
			if(name.empty()) name = str;
			else {
				istringstream iss(str);
				iss >> v2(0, i++);
			}
		}
		v2 /= length(v2);
		if((sim = v2*v1) > max_sim) {
			max_sim = sim;
			max_name = name;
		}
	}

	ifs.close();
	return max_name;
}

// テスト用のmain
int main()
{
	int i;
	ifstream ifs(filepath);
	std::vector<double> feats(Feats_dim);
	string line, str, name;

	i = 0;
	name = "";
	getline(ifs, line);
	istringstream ss(line);
	while(getline(ss, str, ',')) {
		if(name.empty()) name = str;
		else {
			istringstream iss(str);
			iss >> feats[i++];
		}
	}
	ifs.close();

	cout << search_max_similarity(feats) << endl;
	return 0;
}

