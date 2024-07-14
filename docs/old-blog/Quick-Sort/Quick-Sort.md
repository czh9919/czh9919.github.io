---
title: Quick Sort
catalog: true
date: 2018-10-08 19:08:01
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---

# Quick sort

## Description

这是一个分治法，我不会花太长时间在快排上。这是书上的伪代码。
It is a divide and conquer algorithm. I won't spend a lot of time describe quick sort. so this is pseudocode. And I will use the code in the book not in the video.

    QUICKSORT(A,p,r)
        if  p<r
            q=PARTITION(A,p,r)
            QUICKSort(A,p,q-1)
            QUICKSort(A,q+1,r)
    PARTITION(A,p,r)
        x=A[r]
        i=p-1
        for j=p to r-1
            if A[j]<=x
                i=i+1
                exchange A[i] with A[j]
        exchange A[i+1] with A[j]
        return i+1

这里我们选取了最后一个元素作为**主元**，主元把原数组划分成俩子数组，对右边那个数组来说他们都比主元大，而对左边的子数组说，他们都比主元小。所以，在这里，我们注意到，最坏情况的发生是输入数组已经被排好或逆序排好。\(T(n)=T(n-1)+\Theta (n)\).我们使用主方法得到时间复杂度为\(\Theta (n^2)\)。
而最好情况的递归式为 \(T(n)=2T(\frac{n}{2}+\Theta (n)\)，用主方法得到时间复杂度为\(\Theta (n\log n)\).
Here we use the last element as the **pivot element**. we use the pivot element to divide the array to two subarray. for the right array, all element is bigger than the pivot element. And the right subarray is smaller than the pivot element. Here, we notice the worst case is the array is sorted or reversed sorted.\(T(n)=T(n-1)+\Theta (n)\). And we use master method to get the time complexity is \(\Theta (n^2)\) .And the best case is \(T(n)=2T(\frac{n}{2}+\Theta (n)\), and we use master method to get the time complexity is \(\Theta (n\log n)\).

```python
def QuickSort(A,p,r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(r - p):
        if A[j + p] <= x:
            i = i + 1
            A[i], A[j + p] = A[j + p], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
B = [6,8,9,72,4,6,4,1,56,6]
QuickSort(B,0, 9)
```

```cpp
#include<cstdio>
#include<algorithm>
int Partition(int *A,int p,int r)
{
    int x = A[r];
    int i = p - 1;
    for (int j = p; j < r;j++)
    {
        if(A[j]<=x)
        {
            i++;
            std::swap(A[i], A[j]);
        }
    }
    std::swap(A[i + 1], A[r]);
    return i + 1;
}
void QuickSort(int *A,int p,int r)
{
    if(p<r)
    {
        int q;
        q = Partition(A, p, r);
        QuickSort(A, p, q - 1);
        QuickSort(A, q + 1, r);
    }
}
int main(int argc, char const *argv[])
{
    int A[10] = {6, 8, 9, 72, 4, 6, 4, 1, 56, 6};
    QuickSort(A, 0, 9);
    return 0;
}
```
