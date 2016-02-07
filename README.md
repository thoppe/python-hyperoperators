# Hyperoperators

`hyperop` is a small pure python library for representing ridiculously large numbers in python. It does so using [hyperoperations](https://en.wikipedia.org/wiki/Hyperoperation).

+ Hyperoperation 0 is the [successor](https://en.wikipedia.org/wiki/Successor_function), `H0(None, 4) = 5`
+ Hyperoperation 1 is [addition](https://en.wikipedia.org/wiki/Addition), `H1(2,4) = 2 + (1+1+1+1) = 6`
+ Hyperoperation 2 is [multiplication](https://en.wikipedia.org/wiki/Multiplication) (repeated addition), `H2(2,4) = 2+2+2+2 = 8`
+ Hyperoperation 3 is [exponentiation](https://en.wikipedia.org/wiki/Exponentiation) (repeated multiplication), `H3(2,4) = 2*2*2*2 = 16`
+ Hyperoperation 4 is [tetration](https://en.wikipedia.org/wiki/Tetration) (repeated exponentiation) `H4(2,4) = 2^(2^(2^(2))) = 65536`
+ ...
+ Hyperoperation n is repeated Hyperoperation (n-1)


## TO DO:

+ [x] Write `H0`, the [successor](https://en.wikipedia.org/wiki/Successor_function) operator.
+ [ ] Add `FLAG` to use intermediate speedup operators or not.
+ [ ] Create as proper library, push into [pyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
+ [ ] Finish documentation (add cool examples like sqrt(2) power + [Graham's number](https://en.wikipedia.org/wiki/Graham%27s_number)