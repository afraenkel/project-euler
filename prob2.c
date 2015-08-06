#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>


int * fibonacci(int N)
// returns the fibonacci sequence with entries less than N.
// the end of the sequence is demarcated with the entry 0.
{
  int *F = malloc(N*sizeof(int));
  int i = 0;
  int window[3] = {0,1,1};
  for(i = 0; i < N; i++){
    window[0] = window[1];
    window[1] = window[2];
    window[2] = window[0] + window[1];
    if( window[0] < N ){
      F[i] = window[0];
    } else {
      F[i] = 0;
      break;
    }
        
  }
  return F;
}


int main(int argc, char **argv )
// returns the sum of the even fibonacci
// numbers less than argv[1]
{
  int *fib;
  int i = 0;
  int sum = 0;
  int N = atoi(argv[1]);

  fib = fibonacci(N);

  for(i = 0; i < N; i++){
    if( fib[i] == 0 ){
      break;
    } else if( fib[i] % 2 == 0 ){
      sum += fib[i];
    }
  }

  free(fib);

  printf("%d",sum);

  return 0;
}

    
    
      
