// hello.c
#include <cstdio>
#include <cstring>
using namespace std;

int add(int x, int y){
	return x + y;
}

void out(const char* firstname, const char* lastname, char* const str_out, const size_t len){
	snprintf(str_out, len, "Hello, %s %s!", firstname, lastname);
}
