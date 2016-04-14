
/*
 *既知の要素数のデータに対し総和を取る
 *(a)データを絶対値でソートせずに総和を取る
 *(b)データを絶対値でソートして総和を取る
 *2つの結果を比較する
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 21

int main(void)
{
  FILE *fp;
  char *fname = "num.dat";
  char s[100];
  double data1[N];
  double data2[N];
  int i = 0;

  void print_array(int size, double * array);
  
  void abssort(double *array);

  double dsum(int size, double *array);

  void check_sum(int size, double* array1, double* array2);
  
  fp =  fopen(fname, "r");
  //ファイルオープン失敗
  if(fp == NULL){
    printf("%sの読み込みに失敗しました\n", fname);
    return -1;
  }

  //成功->データ取り込み
  printf("読み込んだデータ:\n");
  while(fgets(s, 100, fp) != NULL){
    data1[i] = atof(s);
    data2[i] = atof(s);
    printf("Data[%d]: %s", i++, s);
  }
  printf("\n");
  printf("----------------------------------------\n");
  fclose(fp);
 
  //未ソートデータ表示
  printf("ソートされていないデータ:\n");
    print_array(N, data1);
  printf("----------------------------------------\n");
  
  //ソート後のデータ表示
  abssort(data2);
  printf("ソートしたデータ:\n");
  print_array(N, data2);
  printf("----------------------------------------\n");
 
  //未ソートで総和を取る
  double result1 = dsum(N, data1);
  printf("ソートしない値の和: %f\n", result1);

  //絶対値ソートしてから総和を取る
  double result2 = dsum(N, data2);  
  printf("ソートされた値の和: %f\n", result2); 
  printf("----------------------------------------\n");
 
  //和の様子の比較
  check_sum(N, data1, data2);
 
  return 0;
  
}

void print_array(int size, double* array){
  for(int i = 0; i < size; i++){
    printf("data[%d]: %f\n", i, array[i]);
  } 
}

double dsum(int size, double *array){
  double result = 0;
  for(int i = 0; i < size; i++){
    result += array[i];
  }
  return result;
}

void abssort(double *array){
  //絶対値でソート
  for(int i = 0; i<20; i++){
    for(int j = i+1; j<20; j++){
      if(fabs(array[i]) > fabs(array[j])){
        double tmp = array[j];
        array[j] = array[i];
        array[i] = tmp;
      }
    }
  }
}

void check_sum(int size, double* array1, double* array2){
  double sum1, sum2;
  sum1 = sum2 = 0;

  printf("ソートの有無で総和の経過を比較:\n");
  for(int i = 0; i < size; i++){
    sum1 += array1[i];
    sum2 += array2[i];
  
    printf("ソート無しデータの和[%d番目まで]: %f\n", i, sum1);
    printf("ソート有りデータの和[%d番目まで]: %f\n", i, sum2);
    if(i+1 != size){
    printf("次に和を取る値(ソート無し): %f\n", array1[i+1]);
    printf("次に和を取る値(ソート有り): %f\n", array2[i+1]);
    }
    printf("\n");
  }
}
