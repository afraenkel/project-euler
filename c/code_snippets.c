#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* This contains useful functions for the project euler problems. */


// returns the fibonacci sequence of lenth N
// array *needs* to be freed when called.
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
// array *needs* to be freed when called.
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


// gcd function
int gcd(int a, int b)
{
  int tmp = 0;
  if(a < b)
    {
      tmp = a;
      a = b;
      b = tmp;
    }
        
  while(b)
    {
      tmp = a;
      a = b;
      b = tmp % b;
    }
  return a;
}


// exponentiation of ints
int int_pow(int base, int exp)
{
  if(exp == 0) return 1;
  if(exp == 1) return base;
  return base * int_pow(base, exp - 1);
}


// test function
int main(int argc, char *argv[])
{

  int N = atoi(argv[1]); int M = atoi(argv[2]);
  printf("%d", gcd(N,M));

  return 0;
}
