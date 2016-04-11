// hello.c
#include <cstdio>
#include <cstring>

int add(int x, int y){
	return x + y;
}

void out(const char* firstname, const char* lastname, char* const strout, const size_t len){
	snprintf(strout, len, "Hello, %s %s!", firstname, lastname);
}

int mycat(const char* filename, char* const strout, const size_t len)
{
	int i;
	FILE* fp;
	if((fp = fopen(filename, "r")) == NULL) {
		fprintf(stderr, "Can't open file: \"%s\"\n", filename);
		return -1;
	}

	for(i = 0; i < (int)len-1 && (strout[i] = getc(fp)) != EOF; i++)
		;
	strout[i] = '\0';
	fclose(fp);
	return i;
}
