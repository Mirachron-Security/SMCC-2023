#include <stdio.h>
#include <string.h>

#define str(s) #s
#define xstr(s) str(s)

#define input_size 100

char flag[] = "flaggg";

int main(void) {
  char input[input_size];

  while (1) {
    printf("What is the flag?: ");
    scanf("%" xstr(input_size) "s", input);

    if (strcmp(input, flag) == 0) {
      printf("Input is correct!\n");
      break;
    } else {
      printf("Input is not correct, try again\n");
    }
  }

  return 0;
}
