# satsolve

## Background
Briefly stated, the SAT problem is to find a set of true/false assignments for a set of propositions that will make a given propositional logic sentence true. For example, suppose that you have the following sentence in conjunctive normal form (CNF):

`(A ∨ ¬D) ^ (B ∨ ¬D) ^ (¬A ∨ ¬B ∨ D)`

Three propositions (A, B, and D) appear in this sentence, and the sentence consists of 3 clauses. For this particular example,the assignment A = 0, B = 1, D = 0 causes the entire sentence to be true. We say that the sentence is therefore satisfiable, and we refer to the assignment A = 0, B = 1, D = 0 as a satisfying model for this sentence. Several other satisfying models also exist for this particular sentence. However, if no assignment for A, B, and D caused the sentence to be true, then we would say that it is unsatisfiable.

After making a random assignment of 0/1 values to all propositions in a given sentence, this algorithm randomly “flips” (toggles) those values, one proposition at a time, as it searches for a satisfying model. For each iteration of the search, the algorithm selects an unsatisfied clause, and then selects a symbol in the clause to flip. This is implemented by the WalkSAT algoritm in `logic.py`.

Use the DIMACS format for representing CNF sentences, as described at http://people.sc.fsu.edu/~burkardt/data/cnf/cnf.html, with some minor simplifications as described below. As an example of this format, consider the following sentence:

`(X1 ∨ ¬X4) ^ (X2 ∨ ¬X4) ^ (¬X1 ∨ ¬X2 ∨ X4) ^ (¬X4 ∨ X5) ^ (¬X3 ∨ X5) ^ (X3 ∨ X4 ∨ ¬X5)`

It is assumed that the propositions Xi are numbered sequentially beginning at i = 1. Examples of the modified CNF format can be found in `testcases/`

After any comment line(s), there will be a “problem” line, which will always start with “p cnf”. Next on the problem line is n, which tells the program the number of propositions in the sentence. The last item on the problem line is the number of clauses in the file. The rest of the file will contain clauses, with one clause per line of text. Each clause will be represented as a sequence of integers that correspond to subscripts of the propositions Xi. A negative integer means that the proposition is negated, and a positive integer means that it is not negated. All subscripts lie in the range [1, n]. Each clause can contain any number of literals up to n. In each clause, a particular proposition will appear at most one time. A “0” will appear at the end of each line as a delimiter.

## Usage
`satsolve(cnf_file, max_flips)`

Using python2:
```python
from satsolve import satsolve
satsolve('testcase1.txt', 2000)
```

Example output:

```
Solution found:                 10101
Flips needed to find solution: 	1
Time to find solution (s): 	    0.000866
```

The solution is a list of literals that map to X1, X2, ...,Xn. If the max number of flips is reached before a solution is found, then satsolve will show a solution that it found that best fits the logic sentence supplied by the CNF file:

```
Solution not found
Best solution found:            0101001111011
Flips needed to find solution: 	1
Time to find solution (s): 	    0.006644
```

