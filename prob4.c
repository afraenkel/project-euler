#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

// determine the number of digits in an integer
int num_places (int n)
{
  if(n < 0)
    {
      return num_places (-1 * n);
    }
  if(n < 10)
    {
      return 1;
    }

  return 1 + num_places(n / 10);
}

// exponentiation of ints
int int_pow(int base, int exp)
{
  if(exp == 0) return 1;
  if(exp == 1) return base;
  return base * int_pow(base, exp - 1);
}

// determine if an integer is a palidrome
int is_palindrome(int N)
{
  int numdigits = num_places(N);
  int left = 0;
  for(int i=1; i <= numdigits/2; i++)
    {
      int left = (N / int_pow(10,numdigits-i)) % 10;
      int right = (N % int_pow(10,i)) / int_pow(10,i-1);
      if(left != right)
        {
          return 0;
        }
    }
  return 1;
}



// find the largest palindrome made by the
// product of two three digit numbers.
int main(int argc, char *argv[])
{
  int pal = 0;
  for(int i=100; i<1000; i++)
    {
      for(int j=0; j + i < 1000; j++)
        {
          int tmp = i * (i+j);
          if( is_palindrome(tmp) && (tmp > pal))
            { pal = tmp;
            }
        }
    }

  printf("%d",pal);
  return 0;
}


