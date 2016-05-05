#include <cstdio>
#define Feats_dim 99120
using namespace std;

const char *filepath = "./result/descriptor.csv";

int main()
{
	FILE *fp = fopen(filepath, "r");
	char name[1024];
	double val;

	while(fscanf(fp, "%[^,]", name) != EOF) {
		printf("%s", name);
		for(int i = 0; i < Feats_dim; i++) {
			fscanf(fp, ",%lf", &val);
			printf(" %f", val);
		}
		fscanf(fp, "\n");
		printf("\n");
	}

	fclose(fp);
	return 0;
}
