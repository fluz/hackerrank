This problem can be solved using Arithmetic Progression.

To do this, I sum all multiples of three, all multiples of five and remove the numbers counted twice subtracting the sum of fifteen.

To sum all multiples of three, under a limit number **N**:

    sum = ((a_1 + a_n) * n) / 2

    where:
      * a_1 = 0;
      * a_n = (N-1) / 3) * 3;
      * n = (N-1) / 3.

