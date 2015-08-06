#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

// returns the fibonacci sequence of lenth N
int * fibonacci(int N)
{
  int *F = malloc(N*sizeof(int));
  int i = 0;
  int window[3] = {0,1,1};
  for(i = 0; i < N; i++){
    window[0] = window[1];
    window[1] = window[2];
    window[2] = window[0] + window[1];

    F[i] = window[0];
  }
  return F;
}


// A function that returns an array of prime factors of n
int * primes(int n)
{
  int *P = malloc(n*sizeof(int));
  int i = 0;

  while(n % 2 == 0)
    {
      P[i] = 2;
      n /= 2;
      i += 1;
    }

  for(int j = 3; j <= sqrt(n); j += 2)
    {
      while(n % j == 0)
        {
          P[i] = j;
          n /= j;
          i += 1;
        }
    }

  if(n > 2){
    P[i] = n;
    i += 1;
  }

  P[i] = 0;
  return P;
}


int main(int argc, char *argv[])
{

  int i = 0;
  int N = atoi(argv[1]);

  int *P = primes(N);
  int n = sizeof(P)/sizeof(int);
  while(P[i] != 0)
    {
      printf("%d ", P[i]);
      i++;
    }
  return 0;
}
