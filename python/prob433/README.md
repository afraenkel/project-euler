## Computing the sum of the number of steps of Euclid's algorithm over the integer lattice.

The lower triangle of the lattice is computed. Then one uses the
observations ```(1) if x > y, then E(x, y) = E(y, x) + 1``` and ```(2)
E(x,x) = 1``` to compute the sum over any square 1<=x,y<=N.

* Single: Computes as few gcds as possible.

* Parallel: a mapper + reducer to be run either with hadoop streaming
  or gnu parallel. Could be further optimized with partial memoization.
