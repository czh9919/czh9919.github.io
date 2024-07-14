---
title: Get Started
catalog: true
date: 2018-09-05 10:14:49
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---

# 算法基础 Get Started

从今天起，开始看算法导论，不出意外的话，我将会用英文和中文同时记录下我的笔记和心得。如果有人在看的话，如果对我写的有问题，请直接留言指出，不胜感激。  
From today, I begin to read the book named Introduction to Algorithms. Without accident, I will record my notes and my thoughts in both English and mandarin. If someone is watching, if there is a problem with me or the blog, please leave a message and point out, I would be grateful.  

## 插入排序 Insertion sort

相信大家都玩过斗地主，每个人在抓牌后，拿到手里的牌是无序的，我们常用的理牌手段就是插入排序。  
I trust everyone has played poker before. After draw cards, the cards we hold is disordered, the way we always used is Insertion sort.  
我会用伪代码和不同的计算机语言展示插入排序  
I will use pseudocode and a lot of computer language show Insertion sort.  

伪代码如下  
pseudocode:

    for j=2 to A.length
        key=A[j]
        //Insert A[j] into the sorted sequenceA[1..j-1]
        i=j-1
        while i>0 and A[i]>key
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
python:

```python
A=[9,7,6,4,3,1]
for j in range(len(A)-1):
    key=A[j+1]
    i=j
    while(i>=0 and A[i]>key):
        A[i+1]=A[i]
        i=i-1
    A[i+1]=key
for num in A:
    print(num)
```

C/C++:

```cpp
#include<bit/stdc++>
#define length 6
int main()
{
    int A[length]={9,7,6,4,3,1};
    for(int j = 1;j < length;j++){
        int key = A[j];
        int i = j - 1;
        while(i>=0&&A[i]>key){
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = key;
    }
    for (int i = 0;i<length;i++){
        printf("%d ", A[i]);
    }
    return 0;
}
```

### 插入算法的分析 Analysis of the insertion sort

算法所需时间依赖于输入的规模和已被排序的程度，抛去这两个因素单独讨论算法所需时间是毫无根据的。  
The time the algorithms used rely on the size and the degree of sorting. It is unfounded to discuss the algorithm separately without these two factors.  
我们往往集中于对最坏情况的讨论。  
We usually focus on the discussion of the worst case.
但有时，我们也要讨论期望时间。  
But sometimes, it is needed to discuss the average case.
这里，我将展开说明。  
Here, I will expand the instructions.  
如何获取这个“average case”？  
how to get the "average case"?  
加权平均，每种输入的运行时间乘以那种输入出现的概率。  
we use the weighted average. it's the time of every input times probability that it will be input.  
但是我们如何得到那种输入出现的概率呢？
But how to get the probability that it will be input?  
做个假设。  
Make a assumption.  
一个有关输入的统计分布的假设  
An assumption of the statistical distribution of inputs.  
我们假设所有输入的出现可能是相同的。 
We assume that the probability of every input showed is the same.  

#### 渐进分析 Asymptotic Analysis

这里我们引入渐进符号  
Here, we used asymptotic nation.  
$$
\Theta
$$
简单来说就是弃掉他的低阶项，忽略掉前边的常数因子  
which means drop low order terms and ignore leading constants.  
举例来说就是:  
such as:  
$$
100n^3+1000n^2+10=\Theta (n^3)
$$
至于数学定义，下次我们将探讨这个。  
we will discuss its mathematical definition next time.  
这样，对一个\(\Theta (n^3)\)的算法，迟早会快于\(\Theta (n^2)\)的算法，在\(n\to \infty\)的情况下  
As \(n\to \infty\),\(\Theta (n^3)\) algorithm always beats \(\Theta (n^2)\) algorithm.  
如图所示  
As the picture showed  
<!-- ![comparison](comparison.png) -->

#### 最差情况的分析 the analysis of the worst case

在最差的情况下，
In the worst case,
$$
T_n=\sum^n_{j=2}(\Theta j)=\Theta (n^2)
$$

## 归并排序 merge sort

这是一个利用分治法来解题的实例。  
This is an example of using The divide-and-conquer approach to solve problem.  
伪代码:
pseudocode:

    n1=q-p+1
    n2=r-q
    let L[1...n1+1]and R[1..n2+1]be new arrays
    for i=1 to n1
        L[i]=A[p+i-1]
    for j=1 to n2
        R[j]=A[q+j]
    L[n1+1]=\infty
    R[n2+1]=\infty
    i=1
    j=1
    for k=p to r
        if L[i]<=R[j]
            A[k]=L[i]
            i=i+1
        else
            A[k]=R[j]
            j=j+1
python:

```python
A = [9, 8,7, 6, 5,4, 3, 1]
def merge_sort(l):
    if len(l)==1:
        return l
    num = len(l) / 2
    left = merge_sort(l[:int(num)])
    right = merge_sort(l[int(num):])
    return merge(left,right)
def merge(left, right):
    result = []
    r = 0
    l = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[r])
            l += 1
    result += left[l:]
    result += right[r:]
    return result
A = merge_sort(A)
for i in range(len(A)):
    print(A[i])
```

c/cpp:

```cpp
#include<stdio.h>
#include<stdlib.h>
void merge_sort_recursive(int arr[], int reg[], int start, int end)
{
    if (start >= end)
        return;
    int len = end - start, mid = (len >> 1) + start;
    int start1 = start, end1 = mid;
    int start2 = mid + 1, end2 = end;
    merge_sort_recursive(arr, reg, start1, end1);
    merge_sort_recursive(arr, reg, start2, end2);
    int k = start;
    while (start1 <= end1 && start2 <= end2)
        reg[k++] = arr[start1] < arr[start2] ? arr[start1++] : arr[start2++];
    while (start1 <= end1)
        reg[k++] = arr[start1++];
    while (start2 <= end2)
        reg[k++] = arr[start2++];
    for (k = start; k <= end; k++)
        arr[k] = reg[k];
}
void merge_sort(int arr[], const int len) {
    int reg[len];
    merge_sort_recursive(arr, reg, 0, len - 1);
}
int A[8]={9,8,7,6,5,4,3,2};
int r[8] = {0};
int main(int argc, char const *argv[])
{
    merge_sort_recursive(A, r, 0, 7);
    return 0;
}

```

### 归并排序的算法分析 Analysis of the merge sort

对单次递归做分析得
After analysis to one recursive, we get:
$$
T(n)= \begin{cases}
c \quad \text{若}n=1
\\\\
2T(n/2)+cn \quad \text{若}n>1
\ \end{cases}
$$
再由递归树得
we use recursion tree get the last result
如图所示
As the picture showed:
<!--  -->
所以，最后分析得
So, we get
$$
T(n)=cn\log _2 n+cn=\Theta(n\lg n)
$$
