#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. */

/*   What is the 10,001st prime number? */


int main(int argc, char *argv[])
{
  int i = 2; // i is the number to primality test
  int num_primes = 0; // counter for number of primes found
  int last_prime = 0; // last prime found
  
  while(num_primes < atoi(argv[1]))
    {
      int is_prime = 1;
      for(int j = 2; j <= i/2; j++)
        {
          if(i % j == 0)
            {
              is_prime = 0;
              break;
            }
        }
      if(is_prime)
        {
          last_prime = i;
          num_primes++;
        }
      i++;
    }

  printf("%d", last_prime);
  return 0;
}
         
