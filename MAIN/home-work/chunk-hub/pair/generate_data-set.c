#include <stdio.h>

void main() {
	FILE *fp = NULL;
	fp = fopen("stk.csv", "w");
	for(int i=0; i<10000000; i++)
		fprintf(fp, "%i\n", i);
	fclose(fp);
}
