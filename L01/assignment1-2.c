
/*
 *既知の要素数のデータに対し総和を取る
 *(a)データを絶対値でソートせずに総和を取る
 *(b)データを絶対値でソートして総和を取る
 *2つの結果を比較する
 */



#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct _data{
  double dnum;
  struct _data* next;
} data;

typedef struct{
  data* head;
  data* crnt;
} list;

void abs_sort(list* list);

data* add_node(void);

void init_list(list* list);

void print_list(list* list);

double dsum(list list);

void check_sum(list list1, list list2);

int main(void)
{
  FILE *fp;
  char *fname = "num.dat";
  char s[100];
  int i = 0;
  list list1;
  list list2;

  init_list(&list1);
  init_list(&list2);
  
  fp =  fopen(fname, "r");
  //ファイルオープン失敗
  if(fp == NULL){
    printf("%sの読み込みに失敗しました\n", fname);
    return -1;
  }

  //成功->データ取り込み
  printf("読み込んだデータ:\n");
  while(fgets(s, 100, fp) != NULL){
    data* next1 = (data*)malloc(sizeof(data));
    data* next2 = (data*)malloc(sizeof(data));
 
    next1->dnum = atof(s);
    next2->dnum = atof(s);
    
    if(list1.head == NULL) {
      list1.head = next1;
      list1.crnt = list1.head;
    } else {
      list1.crnt->next = next1;
      list1.crnt = list1.crnt->next;
    }
    if(list2.head == NULL) {
      list2.head = next2;
      list2.crnt = list2.head;
    } else {
      list2.crnt->next = next2;
      list2.crnt = list2.crnt->next;
    }

    printf("Data[%d]: %s", i++, s);
  }
  list1.crnt = list1.head;
  list2.crnt = list2.head;
  printf("\n");
  printf("----------------------------------------\n");
  fclose(fp);

  //未ソートデータ表示
  printf("ソートされていないデータ:\n");
  print_list(&list1);
  printf("----------------------------------------\n");
 
  //ソート後のデータ表示 
  abs_sort(&list2);
  printf("ソートしたデータ:\n");
  print_list(&list2);
  printf("----------------------------------------\n");
  
  //未ソートで総和を取る
  double result1 = dsum(list1);
  printf("ソートしない値の和: %f\n", result1);
  
  //絶対値ソートしてから総和を取る
  double result2 = dsum(list2);
  printf("ソートされた値の和: %f\n", result2);
  printf("----------------------------------------\n");
 
  //和の様子の比較
  check_sum(list1, list2);
 
  return 0;
  
}

void init_list(list* list){
  list->head = NULL;
  list->crnt = NULL;
}

data* add_node(void){
  return (data*)malloc(sizeof(data));
}

void print_list(list* list){
  int i = 0;
  data* ptr = list->head;
  while(ptr != NULL){
    printf("data[%d]: %f\n", i++, ptr->dnum);
    ptr = ptr->next;
  }
}

double dsum(list list){
  double result = 0;
  data* data = list.head;
  while(data != NULL){
    result += data->dnum;
    data = data->next;
  }
  return result;
}

void abs_sort(list *list){
  data* ptr1 = list->head;
  while(ptr1 != NULL){
    data* ptr2 = ptr1->next;    
    while(ptr2 != NULL){
      if(fabs(ptr1->dnum) > fabs(ptr2->dnum)){
        double tmp = ptr2->dnum;
        ptr2->dnum = ptr1->dnum;
        ptr1->dnum = tmp;
      }
      ptr2 = ptr2->next;
    }
    ptr1 = ptr1->next;
  }
}

void check_sum(list list1, list list2){
  double sum1, sum2;
  sum1 = sum2 = 0;
  int i = 0;
  data* data1 = list1.head;
  data* data2 = list2.head;
  
  printf("ソートの有無で総和の経過を比較:\n");
  while(data1 != NULL && data2 != NULL){
    if(data1 != NULL) sum1 += data1->dnum;
    if(data2 != NULL) sum2 += data2->dnum;
    printf("sum1[%d]: %f\n", i, sum1);
    printf("sum2[%d]: %f\n", i, sum2);
    printf("\n");
    i++;
    data1 = data1->next;
    data2 = data2->next;
  }
}
