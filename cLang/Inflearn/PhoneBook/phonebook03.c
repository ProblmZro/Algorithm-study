#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define INIT_CAPACITY 3 // 동적할당 테스트 위해 일부러 작은값
#define BUFFER_SIZE 50

char** names; // char* 타입의 배열 이름이기 때문
char** numbers;
int capacity = INIT_CAPACITY;
int n = 0;

char delim[] = " ";

void init_directory();
void process_command();

int main() {
  char command[BUFFER_SIZE];

  init_directory();
  process_command();

  return 0;
}

void reallocate() {
  capacity *= 2;
  char **tmp1 = (char **)malloc(capacity*sizeof(char *));
  char **tmp2 = (char **)malloc(capacity*sizeof(char *));

  for(int i=0; i<n; i++) {
    tmp1[i] = names[i];
    tmp2[i] = numbers[i];
  }

  // 더 이상 필요없는 애들 동적 메모리 할당 해제
  free(names);
  free(numbers);

  // 새로운 배열 가리키도록 함
  names = tmp1;
  numbers = tmp2;
}

void init_directory() {
  names = (char **)malloc(sizeof(char *) * INIT_CAPACITY);
  numbers = (char **)malloc(sizeof(char *) * INIT_CAPACITY);
}

int read_line(char str[], int limit) {
  int ch, i = 0;

  while ((ch = getchar()) != '\n') {
    if (i < limit - 1)
      str[i++] = ch;
  }
  str[i] = '\0';
  
  return i;
}

void process_command() {
  char command_line[BUFFER_SIZE]; // 한 라인 통으로 읽기 위한 버퍼
  char *command, *arg1, *arg2;

  while (1) {
    printf("$ ");

    // 아무 입력 없을 때
    if(read_line(command_line, BUFFER_SIZE) <= 0)
      continue;
    
    command = strtok(command_line, delim);
    if(strcmp(command, "read") == 0) {  
      arg1 = strtok(NULL, delim); // 파일명 받기
      if(arg1 == NULL) {
        printf("파일 이름이 필요합니다.\n");
        continue;
      }
      load(arg1);
    }
    else if(strcmp(command, "add") == 0) {
      arg1 = strtok(NULL, delim);
      arg2 = strtok(NULL, delim);
      if(arg1 == NULL || arg2 == NULL) {
        printf("이름, 전화번호를 입력해야 합니다.\n");
        continue;
      }
      add(arg1, arg2);
    }
    else if(strcmp(command, "find") == 0) {
      arg1 = strtok(NULL, delim);
      if(arg1 == NULL) {
        printf("찾을 이름을 입력해야 합니다.\n");
        continue;
      }
      find(arg1);
    }
    else if(strcmp(command, "status") == 0)
      status();
    else if(strcmp(command, "delete") == 0) {
      arg1 = strtok(NULL, delim);
      if(arg1 == NULL) {
        printf("삭제할 이름을 입력해야 합니다.\n");
        continue;
      }
      delete(arg1);
    }
    else if(strcmp(command, "save") == 0) {
      arg1 = strtok(NULL, delim);
      if(arg1 == NULL) {
        printf("파일명을 입력해야 합니다.\n");
        continue;
      }
      save(arg1);
    }
  }
}

void add(char *name, char *number) {
  if(n >= capacity)
    reallocate();

  int i = n-1;
  while (i>=0 && strcmp(names[i], name) > 0) // i번째 항목이 항목이 입력값보다 크면 i번째 항목을 뒤로 민다. (이름 알파벳 순으로 정렬)
  {
    names[i+1] = names[i];
    numbers[i+1] = numbers[i];
    i--;
  }
  names[i+1] = strdup(name);
  numbers[i+1] = strdup(number);
  n++;

  printf("%s was added successfully.\n", name);
}

void find(char *name) {
  int index = search(name);

  if(index == -1)
    printf("No person named '%s' exists.\n", name);
  else
    printf("%s\n", numbers[index]);
}

void status() {
  for(int i=0; i<n; i++) {
    printf("%s %s\n", names[i], numbers[i]);
  }
  printf("Total %d persons.\n", n);
}

void delete(char *name) {

  int index = search(name);
  if (index == -1) {
    printf("No person named '%s' exists.\n", name);
    return;
  }

  int j = index;
  for(; j<n-1; j++) {
    names[j] = names[j+1];
    numbers[j] = numbers[j+1];
  }

  n--;
  printf("%s was deleted successfully.\n", name);
}

void load(char *fileName) {
  char buf1[BUFFER_SIZE], buf2[BUFFER_SIZE];

  FILE *fp = fopen(fileName, "r");
  if(fp == NULL) {
    printf("파일 열기를 실패했습니다.\n");
    return;
  }

  while ((fscanf(fp, "%s", buf1) != EOF)) // 이름 읽기
  {
    fscanf(fp, "%s", buf2); // 전번 읽기
    add(buf1, buf2);
  }
  
  fclose(fp);
}

void save(char *fileName) {
  FILE *fp = fopen(fileName, "w");
    if(fp == NULL) {
    printf("파일 열기를 실패했습니다.\n");
    return;
  }

  for(int i=0, i<n; i++) {
    fprintf(fp, "%s %s\n", names[i], numbers[i]);
  }

  fclose(fp);
}

int search(char *name) {
  for(int i=0; i<n; i++){
    if(strcmp(name, names[i] == 0)) {
      return i;
    }
    return -1;
  }
}