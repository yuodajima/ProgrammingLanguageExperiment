
/*
 *ポインタで二分木を作り，課題1について
 *同様に絶対値昇順ソートし，総和をとる
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct _Node{
  double dnum;
  struct _Node* left;
  struct _Node* right; 
} Node;

int main(void){

  void insert(Node** root, double dnum);
  void make_tree(Node* root, double dnum);
  double sum_tree(Node* root);
  void print_tree(Node* root);

  FILE *fp;
  char *fname = "num.dat";
  char s[100];
  
  Node* root = NULL;

  fp =  fopen(fname, "r");
  //ファイルオープン失敗
  if(fp == NULL){
    printf("%sの読み込みに失敗しました\n", fname);
    return -1;
  }

   //成功->データ取り込み
  printf("読み込んだデータ:\n");
  int i = 0;
  while(fgets(s, 100, fp) != NULL){
    insert(&root, atof(s));
    printf("Data[%d]: %s", i++, s);
  }
  printf("\n");
  printf("----------------------------------------\n");
  fclose(fp);

  printf("二分木内のデータを昇順に取り出す\n");
  print_tree(root);
  printf("----------------------------------------\n");

  printf("昇順に総和をとった結果: %f\n", sum_tree(root));
      
  return 0;
  
}

void insert(Node** root, double dnum){
  Node* cursor = *root;
  Node* new_node = (Node*)malloc(sizeof(Node));
  new_node->dnum = dnum;
  new_node->left = NULL;
  new_node->right = NULL;

  if(cursor != NULL){
     double abs_new_dnum = fabs(new_node->dnum);
     double abs_crnt_dnum = fabs(cursor->dnum);
       
     while(1){
       abs_crnt_dnum = fabs(cursor->dnum); 
       if(abs_new_dnum <= abs_crnt_dnum){
         if(cursor->left == NULL) break;
         cursor = cursor->left;
       }
       if(abs_new_dnum > abs_crnt_dnum){
         if(cursor->right == NULL) break;
         cursor = cursor->right;
       }
     }
     if(abs_new_dnum <= abs_crnt_dnum) cursor->left = new_node;
     if(abs_new_dnum > abs_crnt_dnum) cursor->right = new_node;
  } else {
    *root = new_node;    
  }
}

void print_tree(Node* root){
  if(root != NULL){
  Node* cursor = root;
  Node* left = root->left;
  Node* right = root->right;

  print_tree(left);
  printf("data: %f\n", cursor->dnum);
  print_tree(right);
  }  
}

double sum_tree(Node* root){
  double result = 0;
  if(root != NULL){
    Node* cursor = root;
    Node* left = root->left;
    Node* right = root->right;
    
    result += sum_tree(left);
    result += cursor->dnum;
    result += sum_tree(right);
  }
  return result;
}
