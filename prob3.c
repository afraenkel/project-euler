#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* The prime factors of 13195 are 5, 7, 13 and 29. */

/*   What is the largest prime factor of the number 600851475143 ? */


// A function that returns an array of prime factors of n
int main(int argc, char *argv[])
{
  long long int n = atoll(argv[1]);
  long long int i = 0LL;
  
  while(n % 2LL == 0LL)
    {
      i = 2LL;
      n /= 2LL;
      printf("%lld ",i);
    }

  for(long long int j = 3LL; j <= sqrt(n); j += 2)
    {
      while(n % j == 0LL)
        {
          i = j;
          n /= j;
          printf("%lld ",i);
        }
    }

  if(n > 2LL){
    i = n;
  }

  printf("%lld ", i);
  
  return 0;
}

