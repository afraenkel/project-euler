## Computing the number of steps of Euclid's algorithm.

* Single: Computes as few gcds as possible.

* Parallel: a mapper + reducer to be run either with hadoop streaming
  or gnu parallel. Could be further optimized with partial memoization.
