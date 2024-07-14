---
title: Growth of Functions
catalog: true
date: 2018-09-06 15:41:55
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---

# Growth of Functions

这次全是数学，我爱数学，我爱数学，我爱数学，重要的事说三遍，又要打好多数学公式了呢:)  
This time, this blog, all are about math. I love math, I love math, I love math, This is impossible.

## Asymptotic nation

### \(O\) nation

先给出\(O\)的定义
this is definition of \(O\)
$$f(n=O(g(n)))\quad\text{means there are constants }c\;\text{and }\,n_0\text{,} \text{such that }0\leq f(n)\leq cg(n)\text{ for all }n\geq n_0 $$
举例
ex:
$$2n^2 =O(n^3)$$
我们记\(f(n)=O(g(n))\),表示\(f(n)\)为集合\(O(g(n))\)的成员。所以，我们用\(\subseteq\)也是可以的，有时候有人这么写，但一般还是用\(=\).
\(f(n)=O(g(n))\)means \(f(n)\) is one of the set \(O(g(n))\). So, we use \(\subseteq\) is fine, sometime someone write the way, but we use \(=\) usually.
我们一般用\(O\) 表示上界，打个比方：
big O nation was used to show upper bound. For example:
$$\Theta(n^3)=n^3+O(n^2) $$
\(O\)就类似一个小于等于号
\(O\)actually like 'Less than or equal to'

### \(\Omega\) nation

先给出\(\Omega\)的定义
this is definition of \(\Omega\)
$$f(n=\Omega(g(n)))\quad\text{means there exists constants }c\;\text{and }\,n_0\text{,} \text{such that }0\leq cg(n) \leq f(n)  \text{ for all }n\geq n_0 $$
举例
ex:
$$\sqrt n=\Omega(\lg n)$$
\(\Omega\)就类似一个大于等于号
\(\Omega\)actually like 'greater than or equal to'

### \(\Theta\) nation

我不会在这写\(\Theta\)的定义
I won't show the definition of \(\Theta\)
但会说明啥是\(\Theta\)
But I will tell what's \(\Theta\)
$$\Theta=O\bigcap \Omega$$
有点丑。。。
A little ugly...

### \(o\) nation

举例
ex:
$$2n=o(n^2)\quad n^2\not=o(n^2)$$

### \(w\) nation

举例
ex:
$$ 2n^2=w(n)\quad n^2\not= w(n^2)$$

## solving recurrences

### substitution method

1. Guess the form of the solution

2. Verify by induction

3. solve fir consist

我们首先看一个证明反例
We first look at a proof counterexample

***
proof \(n=O(n)\)
\(1=O(1)\)
Assume \(n-1=O(1)\)
\(n=\underbrace{(n-1)}_{\rm O(1)}+1=O(1)\)
but false here
***
因为常数是在变化的，使用\(O\) 符号很危险，所以一般不用。
because the constants is changing. It isn't good.
So we never use \(O\) nation here.

来看正确的证明吧
This is a right proof
***
Ex proof \(T(n)=4T(n/2)+n\)
guess \(T(n)=O(n^3)\)
Assume \(T(k)\leq ck^3\text{for} k<q \)
$$
T(n)=4T(n/2)+n  
\leq 4c(\frac{n}{2})^3+n  
=\frac 1 2 cn^3+n=cn^3-(\frac 1 2 cn^3 -n)\quad  
\text{if }\frac{1}{2}cn^3-n\geq0
$$

***

### Recursion-tree method

ex
\(T(n)=3T(n/4)+n^2\)
<!--  -->

### master method

应用于如下递归式
apply for the recurrences of the form
$$
T(n)=aT(n/b)+f(n)
$$
有a个子问题，每个子问题规模为n/b,并且a>=1,b>1
So there are a subproblems, and each of them is of size n/b
And a>=1,b>1
f(n)渐进趋正，意思是存在特定\(n_0\),当\(n>n_0\)时,\(f(n)\)大于0
f(n)should be asymptotically positive which means f(n) is greater than zero for n, at least some \(n_0\).

第一步，对比\(f(n)\) 和 \(n^{\log _b a}\)
First, compare \(f(n)\) with \(n^{\log _b a}\)
There are three cases:
case 1:
For some \(\varepsilon>0\),\(f(n)=O(n^{\log _b {a-\varepsilon}})\),\(\Rightarrow T(n)=\Theta (n^{\log _b {a-\varepsilon}})\)
case 2:
For \(f(n)=\Theta (n^{\log _b {a}})\),\(\Rightarrow T(n)=\Theta (n^{\log _b {a}}\lg n)\)
case 3:
For sme \(\varepsilon>0\),\(f(n)=\Omega(n^{\log _b {a-\varepsilon}}\),and we need to higher level bigger than lower level,that is \(af(n)\leq (1-\varepsilon ')f(n)\),for some \(\varepsilon '>0\),\((\Rightarrow T(n)=\Theta (f(n))\)

真如你所见，他非常简单
so as you can see, it is very easy to apply.
举例
ex
$$
T(n)=4T(n/2)+n
$$

This is case 1, so

$$
T(n)=\Theta(n^2)
$$

And

$$
T(n)=4T(n/2)+n^2
$$

This is case 2, so

$$
T(n)=\Theta(n^2\lg n)
$$

and

$$
T(n)=4T(n/2)+n^3
$$

This is case 3, so

$$
T(n)=\Theta(n^3)
$$

but for

$$
T(n)=4T(n/2)+\frac{n^3}{\lg n}
$$
the master method doesn't apply

## summary

I hate math
I hate math
I hate math
