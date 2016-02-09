# `hyperop`
_python library for representing really, really, ridiculously large numbers_
----------
!(figures/zoolander.gif)  <<height:300px>>
!(figures/zoolander2.gif) <<height:300px>>
----------   
### [Travis Hoppe](http://thoppe.github.io/)
[https://github.com/thoppe/python-hyperoperators](https://github.com/thoppe/python-hyperoperators)

====
### *Addition*, $H_1$
### $2 + 4 = 2 + (1+1+1+1) = 6$
====+<br/>
### *Multiplication*, $H_2$
### $2 \times 4 = 2+2+2+2 = 8$

### *Exponentiation*, $H_3$
### $2^4 = 2 \times 2 \times 2 \times 2 = 16$

### *Tetration*, $H_4$
### $\ ^4 2 = 2 ^ {2^{2^2}} = 65536 \neq 2^{2\times 2\times 2}$
  
%+ `H3` is [exponentiation](https://en.wikipedia.org/wiki/Exponentiation) (repeated multiplication), `H3(2,4) = 2*2*2*2 = 16`
%+ `H4` is [tetration](https://en.wikipedia.org/wiki/Tetration) (repeated exponentiation) `H4(2,4) = 2^(2^(2^(2))) = 65536`
====*

### What about higher order operations?
### $H_5$? $H_6$? $H_{1000000}$?

====+
<br/>


# hyperop
!(https://travis-ci.org/thoppe/python-hyperoperators.svg?branch=master) <<transparent;height:60px>>
!(https://coveralls.io/repos/github/thoppe/python-hyperoperators/badge.svg?branch=master) <<transparent;height:60px>>
!(https://badge.fury.io/py/hyperop.svg) <<transparent;height:60px>>

    pip install hyperop
====

# How does it work?
Functional programming in python, fold-right


#### <div style="text-transform: none;"> `reduce(lambda x, y: self.lower(y, x), [a]*b)` </div>

====*

### (boring) Examples

    from hyperop import hyperop
    
    H1 = hyperop(1)
    print H1(2,3), H1(3,2), H1(5,4)
    # >> 5, 5, 8

    H3 = hyperop(3)
    print H3(2,3), H3(3,2), H3(5,4)
    # >> 8, 9, 243

    from math import log
    H = hyperop(4)
    print H(2,5)
    >>> 200352993040684646497....45587895905719156736
    
    print log(log(log(log(H(2,5),2.0),2.0),2.0),2.0) == 2
    >>> True  

====*

# Infinte tetration! $\lim_{n \rightarrow \infty} H_4(\sqrt{2},n)$
# $\sqrt{2}^{\sqrt{2}^{\sqrt{2}^{\sqrt{2}^{\ldots}}}} = 2$

    H4 = hyperop(4)
    print H4(2**0.5, 200)
    # >> 2.0

====*

## Complex tetration!
## $H_4(z,4), z \in \mathcal{C}$
!(figures/tetration_example.png) <<transparent;height:600px>>

====

# Graham's number
_`hyperop` is almost surely the first python library to offer support for it._
_Was the largest computable finite number ever used in a proof._

!(figures/out.gif) <<height:400px; transparent>>
_it's kinda big_
====*

## $g_1 = H_6(3,3)$

# $ g_1 =  \left.    \begin{matrix}3^{3^{\cdot^{\cdot^{\cdot^{\cdot^{3}}}}}}\end{matrix}  \right \}  \left.    \begin{matrix}3^{3^{\cdot^{\cdot^{\cdot^{3}}}}}\end{matrix}  \right \}    \dots  \left.    \begin{matrix}3^{3^3}\end{matrix}  \right \}    3  \quad \text{where the number of towers is} \quad  \left.    \begin{matrix}3^{3^{\cdot^{\cdot^{\cdot^{3}}}}}\end{matrix}  \right \}  \left.    \begin{matrix}3^{3^3}\end{matrix}  \right \} 3 $

Larger than all the atoms of the Universe.

Larger than all _arrangements_ of the atoms of the Universe.

This isn't Graham's number.
====*

## $g_2 = H_{g_1}(3,3)$
====+
## $g_{n} = H_{g_{n-1}}(3,3)$ ...

# $G = g_{64}$

    def GrahamsNumber():
        # This may take awhile...
        g = 6
        for n in range(1,64+1):
            g = hyperop(g)(3,3)
        return g

Comp. sci. technical question:
given infinite memory and time, will python fail?
====

#  Thanks, you!
[@metasemantic](https://twitter.com/metasemantic)


[https://github.com/thoppe/python-hyperoperators](https://github.com/thoppe/python-hyperoperators)