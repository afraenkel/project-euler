#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* The sum of the squares of the first ten natural numbers is, */

/*   1^2 + 2^2 + ... + 10^2 = 385 */
/*   The square of the sum of the first ten natural numbers is, */

/*   (1 + 2 + ... + 10)^2 = 552 = 3025 */
/*   Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. */

/*   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. */

/* (1 + 2 + ... + N)^2 = (N*(N+1)/2)^2 = N^2*(N+1)^2/4 */
/* 1^2 + ... + N^2 = N*(N+1)*(2N+1)/6 */

// exponentiation of ints
int int_pow(int base, int exp)
{
  if(exp == 0) return 1;
  if(exp == 1) return base;
  return base * int_pow(base, exp - 1);
}


int main(int argc, char *argv[])
{
  int N = atoi(argv[1]);
  int diff = int_pow(N,2)*int_pow(N+1,2)/4 - N*(N+1)*(2*N+1)/6;
  printf("%d",diff);
  return 0;
}
  
