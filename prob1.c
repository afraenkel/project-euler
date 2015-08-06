#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  /* returns the sum of all numbers between
     less than argv[1] that are multiples of 3 or 5. */

  if(argc != 2){
    printf("Please enter exactly one input digit");
    return 1;
  }

  int sum = 0;
  int i = 0;
  for(i=0; i < atoi(argv[1]); i++){
    if(i % 3 == 0){
      sum += i;
        } else if(i % 5 == 0){
      sum += i;
        }
  }

  printf("%d", sum);
  return 0;
}


  
