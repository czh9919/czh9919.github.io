---
title: Sorting in Linear Time
catalog: true
date: 2018-10-10 19:01:43
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---

# Sorting in Linear Time

## Lower bounds for sorting

### The decision-tree model

作为一个未来的工程师，我们应当考虑具体情况，我们在分析算法有多快的时候，应当注意计算模型，我们应当定义在这个情况下计算机能做什么才能把数字排好序，比如，**我们只能通过比较元素的大小来判断元素的大小关系**。于是，我们引出决策树模型，一个决策树模型是一个完全二叉树，如图所示。
As a enigineer, we should care about the occasion, so this time, if we analysics the problem that how fast the algorithm can be fast, we should pay attention to computional model. we should define the thing that is allowed to do in this computional model in this occasion to find the correct order. That is **we only can compare pair of elements to determine the relative order of elements**
A decision-tree model can be seen as a complete binary tree. As the picture shown.
<!-- ![decision-tree model](\jueceshu.png) -->
首先，我们比较第一个和第二个元素，如果第一个元素大于第二个，我们走右侧道路，如果第一个元素小于或等于第二个元素，我们走左侧。 之后我们再对比其他元素。每当我们到达决策树模型的结点，这就意味这算法已经确定了一部分排好序的序列，当我们到达树的底部，这就意味着数组已经排好序了。这就是决策树模型做的事。
如果我们使用决策树模型分析算法。但这不是一个方便的方法。 我们可以用决策树模型证明排序算法不会快于\(n\lg n\)，我就不在这里写证明了，这太麻烦了。
但我们给出定理如下
**在最坏情况下，任何比较排序算法都需要做\(\Omega (n\lg n)\)次比较。**

这个定理只是在我们上边加粗字的基础上的。
First, we compare the first element and the second element, if the first one is bigger than the seond one, we select the right way,if the first one is smaller or equal to the second one, we select the left way. Then we compare the others. When we get a node of the decision-tree model, that means the sort algorithm have determined a sequence.When the get the the bottom of the tree, that means the sequence is sorted.And this is the thing we do in decision-tree model.
And we can use decision-tree to analysics the sort algorithm. But this is not a convenient way. We can use this decision-tree model to proof that all sort algorithm can't be faster than \(n\lg n\), I don't want to write the proof in the article, it is troublesome.
But we give a theorem.
**Any comparison sort algorithm requires\(\Omega (n\lg n)\) comparisons in the worst case.**
Remember all this theorem is based on the definition of we only can compare pair of elements to determine the relative order of elements.

## Counting sort

伪代码：
pseudocode:

    COUNTING-SORT(A,B,k)
        let C[0...k]be a new array
        for i=0 to k
            C[i]=0
        for j=1 to A.length
            C[A[j]]=C[A[j]]+1
        for i=1 to k
            C[i]=C[i]+C[i+1]
        for j=A.length downto 1
            B[C[A[j]]]=A[j]
            C[A[j]]=C[A[j]]-1

```python
def CountingSort(A, B, k):
    C = list()
    for i in range(k + 1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A)):
        B[C[A[j]] - 2] = A[j]
        C[A[j]] = C[A[j]] - 1


A = [5, 7, 9, 5, 6, 65, 4]
B = list()
for i in range(7):
    B.append(0)
CountingSort(A,B,65)
```

```cpp
#include<stdio.h>
#include<algorithm>
#include<cstring>
int *CountintSort(int A[],int B[],int k,int len)
{
    int *C = (int *)malloc(k * (sizeof(int)));
    memset(C, 0, k);
    for(int i=0;i<k+1;i++)
    {
        C[i] = 0;
    }
    for (int j = 0; j < len;j++)
    {
        C[A[j]] = C[A[j]] + 1;
    }
    for (int i = 1; i < k + 1;i++)
    {
        C[i] = C[i] + C[i - 1];
    }
    for (int j = 0;j<len;j++)
    {
        B[C[A[j]]-1]=A[j];
        C[A[j]]--;
    }
    return B;
}
int main()
{
    int A[7] = {5, 7, 9, 5, 6, 65, 4};
    int B[7] = {0};
    CountintSort(A, B, 65, 7);
    return 0;
}
```

正如你所见，时间复杂度为\(\Theta (n)\)
As you can see, the time complexity of these code is  \(\Theta (n)\), we are luckily.

## radix sort

我们每次从最低有效位开始排序，即从个位，十位这样。
We sort from the least significant digit of the number, just like we have a lot of numbers(893,567,798),we first sort 3,7,8,then 9,6,8, last,8,5,7.

伪代码：
pseudocode:

    RADIX-SORT(A,d)
        for i=1 to d
            use a stable sort to sort array A to digit i
