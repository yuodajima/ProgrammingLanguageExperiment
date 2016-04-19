
/*
*中置記法の式を逆ポーランド記法に変換し出力する関数を作成
*また，例を取りその実行結果を示す
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node{
  char token;
  int order;
  struct _Node* next;
} Node;

typedef struct _Stack{
  Node* head;
  Node* crnt;
} Stack;

int main(void){

  void init_stack(Stack* stack);
  char pop(Stack* stack);
  void push(Stack* stack, char token);
  int show_order(char token);
  void input_token(Stack* stack, char* formulae);
  void reverse_polish(char* formulae);
  void print_stack(Stack* stack);
  void print_array(char* array);
  
  char* infix1 = "A=(B-C)/D+E*F";
  char* infix2 = "A=B(C/D+E)*F";
  char* infix3 = "A=B-C/(D+E*F)";

  Stack stack1;
  Stack stack2;
  Stack stack3;

  init_stack(&stack1);
  init_stack(&stack2);
  init_stack(&stack3);

  input_token(&stack1, infix1);
  input_token(&stack2, infix2);
  input_token(&stack3, infix3);

  printf("読み込む中置記法の式:\n");
  printf("式1: %s\n", infix1);
  printf("式2: %s\n", infix2);
  printf("式3: %s\n", infix3);
  printf("------------------------------\n");

  printf("逆ポーランド記法へ変換し，出力:\n");
  printf("式1: "); reverse_polish(infix1);
  printf("式2: "); reverse_polish(infix2);
  printf("式3: "); reverse_polish(infix3);
  printf("------------------------------\n");
  
  return 0;
}

void init_stack(Stack* stack){
  stack->head = NULL;
  stack->crnt = NULL;
}

char pop(Stack* stack){
  char token = '\0';
  Node* tmp = NULL;
  if(stack->head != NULL){
    token = stack->head->token;
    tmp = stack->head;
    stack->head = stack->head->next;
    if(tmp->next == NULL) stack->head = NULL;
    free(tmp);
  }
  return token;
}

void push(Stack* stack, char token){
  Node* new_node = (Node*)malloc(sizeof(Node));
  new_node->token = token;
  if(stack->head == NULL) new_node->next = NULL;
  if(stack->head != NULL) new_node->next =stack->head;
  stack->head = new_node;
}

int show_order(char token){
  int order;
  switch(token){
    case '=':
      order = 0;
      break;
    case ')':
      order = 1;
      break;
    case '+':
    case '-':
      order = 2;
      break;
    case '*':
    case '/':
      order = 3;
      break;
    case '(':
      order = 4;
      break;
    default:
      order = 5;
      break;
  }
  return order;
}

void input_token(Stack* stack, char* formulae){
  int formula_length = strlen(formulae);
  for(int i = 0; i < formula_length; i++){
    push(stack, formulae[i]);
  }
}

void reverse_polish(char* formulae){
  int formulae_size = strlen(formulae);
  Stack stack;
  init_stack(&stack);
  for(int i = 0; i < formulae_size; i++){
    char new_token = formulae[i];
    while(stack.head != NULL &&
          stack.head->token != '(' &&
          show_order(new_token) <= show_order(stack.head->token)){
      printf("%c", pop(&stack));
    }
    if(new_token != ')') push(&stack, new_token);
    else  pop(&stack);
  }
  while(stack.head != NULL){
    printf("%c", pop(&stack));
  }
  printf("\n");
}

void print_stack(Stack* stack){
  Node* node = stack->head;
  printf("スタックの内容: ");
  while(node != NULL){
    printf("%c", node->token);
    node = node->next;
  }
  printf("\n");
  node = stack->head;
}

