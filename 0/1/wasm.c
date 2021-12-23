void print(char* msg);  //function prototype

//poor man's malloc
int MALLOC_PTR = 65536;
void* malloc(int size){
  MALLOC_PTR = MALLOC_PTR - size;
  return MALLOC_PTR;
}

void mem_cpy(char* destiny, int destiny_index, char* source, int source_index, int length){
  for(int i = 0; i < length; i++)
    destiny[destiny_index + i] = source[source_index + i]; 
}

int str_len(char* str){
  int c = 0;
  while(str[c] != 0)
    c = c + 1;
  return c;
}

char* str_concat(char* a, char* b){
  int la = str_len(a);
  int lb = str_len(b);
  char* result = malloc(la + lb + 1);
  result[la + lb] = 0;
  mem_cpy(result,0,a,0,la);
  mem_cpy(result,la,b,0,lb);
  return result;
}

char a[] = "Hola ";
char b[] = "Mundo!";

char* demo(){
  print("Ejecutando");
  return str_concat(a,b);
}

int main() { 
  print("Iniciando");
  return str_len("ABC");
}

//C++
extern "C"
void print(char* msg);

//poor man's malloc
int MALLOC_PTR = 65536;
char* malloc(int size){
  MALLOC_PTR = MALLOC_PTR - size;
  return (char*)MALLOC_PTR;
}

void mem_cpy(char* destiny, int destiny_index, char* source, int source_index, int length){
  for(int i = 0; i < length; i++)
    destiny[destiny_index + i] = source[source_index + i]; 
}

int str_len(char* str){
  int c = 0;
  while(str[c] != 0)
    c = c + 1;
  return c;
}

char* str_concat(char* a, char* b){
  int la = str_len(a);
  int lb = str_len(b);
  char* result = malloc(la + lb + 1);
  result[la + lb] = 0;
  mem_cpy(result,0,a,0,la);
  mem_cpy(result,la,b,0,lb);
  return result;
}

char a[] = "Hola ";
char b[] = "Mundo!";

extern "C"
char* demo(){
  print(a);
  return str_concat(a,b);
}

int main() { 
  return 1;
}
