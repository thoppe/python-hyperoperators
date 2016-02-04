# Hyperoperators

`hyperop` is a small pure python library for representing ridiculously large numbers in python. It does so using [hyperoperations](https://en.wikipedia.org/wiki/Hyperoperation).

+ Hyperoperation 1 is addition
+ Hyperoperation 2 is multiplication (repeated addition)
+ Hyperoperation 3 is exponentiation (repeated multiplication)
+ Hyperoperation 4 is tetration (repeated exponentiation)
+ ...
+ Hyperoperation n is repeated Hyperoperation (n-1)



## TO DO:

+ Add `FLAG` to use intermediate speedup operators or not.
+ Write `H0`, the successor operator.
+ Create as proper library, push into [pyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
+ Finish documentation (add cool examples like sqrt(2) power + [Graham's number](https://en.wikipedia.org/wiki/Graham%27s_number)