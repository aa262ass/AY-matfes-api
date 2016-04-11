// hello.c
#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

int add(int x, int y){
	return x + y;
}

void out(const char* firstname, const char* lastname, char* const strout, const size_t len){
	snprintf(strout, len, "Hello, %s %s!", firstname, lastname);
}

int mycat(const char* filename, char* const strout, const size_t len)
{
	int i;
	char ch;
	ifstream ifs(filename);
	if(!ifs) {
		fprintf(stderr, "Can't open file: \"%s\"\n", filename);
		return -1;
	}

	for(i = 0; i < (int)len-1 && ifs >> ch; i++) {
		strout[i] = ch;
	}
	strout[i] = '\0';
	return i;
}
