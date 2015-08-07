#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. */

/* What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */


// lcm function
int lcm(int a, int b)
{
  int tmp = 0; int arg_a = a; int arg_b = b;
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
  int gcd = a;
  return (arg_a * arg_b) / gcd;
}


int main(int argc, char *argv[])
{
  int N = atoi(argv[1]);
  int r = 1;
  
  for(int i = 1; i < N; i++)
    {
      r = lcm(r,i);
    }
  printf("%d\n", r);
  return 0;
}
        
    
