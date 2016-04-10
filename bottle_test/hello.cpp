// hello.c
#include <iostream>
#include <cstring>
using namespace std;

int add(int x, int y){
	return x + y;
}

void out(const char* firstname, const char* lastname, char* const str_out, const size_t len){
	str_out[0] = '\0';
	strncat(str_out, "Hello, ", len);	
	strncat(str_out, firstname, len);	
	strncat(str_out, " ", len);	
	strncat(str_out, lastname, len);	
	strncat(str_out, "!", len);
}
