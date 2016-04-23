#include <stdio.h>

int main(void)
{
  FILE *fp;
  char *fname = "test.dat";
  char s[100];
  int i = 0;

  fp =  fopen(fname, "r");

  if(fp == NULL){
    printf("%s was not found or opend\n", fname);
    return -1;
  }

  printf("file is opened...\n");
  while(fgets(s, 100, fp) != NULL){
    printf("Data[%d]: %s", i++, s);
  }
  fclose(fp);
  return 0;
  
}
