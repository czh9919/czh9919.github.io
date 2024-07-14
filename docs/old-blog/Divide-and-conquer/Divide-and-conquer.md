---
title: Divide and conquer
catalog: true
date: 2018-09-09 15:05:25
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---
# Divide and conquer

开始写这篇文章三天前，我写了一篇关于归并算法的文章，但由于我的军训，现在这篇文章一直没完成。
About three days ago, I have writed the article about merge sort, remember?
归并算法是一个关于分治法的实例，现在，我将介绍一些关于分治法的具体例子。
That is a instance of using Divide and conquer.
today, I will introduce a lot of example of divide and conquer.

## what is Divide and conquer

1. Divide the problem(instance) into one or more subproblem 把一个大问题分解为一个或多个小问题
2. Conquer each subproblems recursively 递归解决小问题
3. Combine solution 合并成大问题

看上去很简单，但其实挺复杂
It looks quite easy. seriously, it isn't.

## Merge sort

让我们快速复习归并算法，我认为写代码并让他运行起来挺重要的，这能让我记得深刻。
Let's review the merge sort quickly.
I thought write the code and make it run is really important which make you remember it deeply.

1. divide 分成小问题
2. conquer recursively 递归解决问题
3. combine  linear time merge 归并解决问题

Running time花费时间
$$
T(n)=2T(n)+\Theta(n)
$$


$$
T(n)=\Theta T(nlgn)
$$

## binary search

The problem is find x in a sorted array 二分查找已排序数组中的数字

1. Divide : compare x in middle 与位于数组中的x进行对比
2. Conquer: Recurse in one subarray 在一个数组中递归
3. conmbine: trivial 后边都是小问题

运行时间：
Running Time:
$$
T(n)=T(n/2)+\Theta(1)
$$


$$
T(n)=\Theta (\lg n)
$$
python:

```python
l = [1, 2, 3, 4, 5, 6,7]
def binary_search(l,num,t):
    length=int((len(l) - 1) / 2)
    if l[length] == num:
        return length + t
    if l[length+1] == num:
        return length + t+1
    elif l[length] > num:
        return binary_search(l[:length], num, 0)
    elif l[length] < num:
        return binary_search(l[length:], num, length+t)
print(binary_search(l,7,0))
```

C/Cpp:

```cpp
#include<stdio.h>
int binary_search(int l[],int num,int start,int end,int len)
{
    int flag = -1;
    while(start<=end)
    {
        int mid = start + (end - start) / 2;
        if(l[mid]==num)
        {
            flag = mid;
            break;
        }
        else if(l[mid]>num)
        {
            end = mid - 1;
        }
        else if(l[mid]<num)
        {
            start = mid + 1;
        }
    }
    return flag;
}
int main(int argc, char const *argv[])
{
    int l[7] = {1, 2, 3, 4, 5, 6, 7};
    int obj = binary_search(l, 5, 0,6, 7);
    printf("%d", obj);
    return 0;
}

```

## Powering a number

计算某个数x的乘方，如果我们用相加的方法，会花费\(\Theta (n)\)的时间
The problem is "given a number ,then compute \(x^n\)
if we use the normal way that is x puls x n times."
it costs \(\Theta (n)\)
但是如果我们使用分治法，就会花费\(\Theta (lgn)\)的时间。
if we use the Divide and conquer method, it will cost \(\Theta (lgn)\)

$$
\begin{cases}
x^n=x^{n/2} * x^{n/2} \text{if x is even}
\\\\
x^{(n-1)/2}*x^{(n-1)/2}*x=x^n \text{if x is odd}
\\\\
 \end{cases}
$$

python:

```python
def pow(num,n):
    if n % 2 == 0:
        if n != 0:
            num2 = pow(num, n / 2) * pow(num, n / 2)
            return num2
        else:
            return num
    else:
        if n != 1:
            num2 = pow(num, (n - 1) / 2) * pow(num, (n - 1) / 2) * num
            return num2
        else:
            return num
print(pow(2,1))
```

c/cpp:

```cpp
#include<stdio.h>
int pow(int num,int n)
{
    if(n%2==0)
        if(n!=0)
        {
            int num2 = pow(num, n / 2) * pow(num, n / 2);
            return num2;
        }
        else
        {
            return num;
        }
    else
    {
        if(n!=1)
        {
            int num2 = pow(num, (n - 1) / 2) * pow(num, (n - 1) / 2) * num;
            return num2;
        }
        else
        {
            return num;
        }
    }
}
int main(int argc, char const *argv[])
{
    int num=pow(2, 3);
    printf("%d", num);
    return 0;
}

```

## maximum-subarray problem

这次让我们想办法用分治法解决最大子数组问题。
对任意连续数组必须处于以下三种情况

1. 完全位于'大'数组的前半部分
2. 完全位于'大'数组的后半部分
3. 跨越了大数组的中点

我们只需要关心这三种情况，更简单些，就是只关注第三种情况，因为我们本身就是在分治得解决问题。
Let’s think about how we might solve the maximum-subarray problem using the divide-and-conquer technique.  
if we need to find the maximum subarray in a array. What should we do? we use divide and conquer method.  
First, we divide the problem to three cases.

1. entirely in the subarray A[low……mid], so that low <=i <=j <=mid
2. entirely in the subarray A[mid + 1…… high], so that mid < i<=  j <= high, or
3. crossing the midpoint, so that low <= i <= mid < j <= high.

we only need to care about the third case. We can find maximum subarrays of A[low,……,mid] and A[mid+1,high] recursively, because these two subproblems are smaller instances of the problem of finding a maximum subarray.

伪代码
pseudocode:

    Find_max_crossing_subarray(A,low,mid,high)
        left_sum=-\infinity
        sum=0
        for i=mid downto low
            sum=sum+A[i]
            if sum>left_sum
                left_sum=sum
                max_left=i
        right_sum=-\infinity
        sum=0
        for j=mid+1 to high
            sum=sum+A[j]
            if sum>right_sum
                right_sum=sum
                max_right=j
        return (max_left,max_right,left_sum+right_sum)
    Find_maximum_subarray(A,low,high)
        if high==low
            return (low,high,A[low])
        else
            mid=[(low+high)/2]
            left_low,left_high,left_sum=Find_maximum_subarray(A,low,mid)
            right_low,right_high,right_sum=Find_maximum_subarray(A,mid+1,high)
            cross_low,cross_high,cross_sum= Find_max_crossing_subarray(A,low,mid,high)
            if left_sum>=right_sum and left_sum>=cross_sum
                return (left_low,left_high,left_sum)
            elif right_sum>=left_sum and right_sum>=cross_sum
                return (right_low,right_high,right_sum)
            else
                return (cross_low,cross_high,cross_sum)

python:

```python
def Find_Cross_Max_Array(l, low, mid, high):
    sum = 0
    max_left = mid
    left_sum = l[mid]
    for x in range(mid - low):
        sum = sum + l[mid - x]
        if x == 0:
            left_sum = l[mid - x]
            max_left = mid - x
        if x > 0:
            if sum > left_sum:
                left_sum = sum
                max_left = mid - x
    sum = 0
    max_right = mid + 1
    right_sum = l[mid + 1]
    for x in range(high - mid):
        sum = sum + l[mid + 1 + x]
        if x == 0:
            right_sum = l[mid + 1 + x]
            max_right = mid + 1 + x
        if x > 0:
            if sum > right_sum:
                right_sum = sum
                max_right = mid + 1 + x
    return max_left, max_right, left_sum + right_sum
def Find_Max_array(l, low, high):
    if high == low:
        return low, high, l[low]
    else:
        mid = ((low + high) / 2)
        mid=int(mid)
        left_low, left_high, left_sum = Find_Max_array(l, low, mid)
        right_low, right_high, right_sum = Find_Max_array(l, mid + 1, high)
        cross_low, cross_high, cross_sum = Find_Cross_Max_Array(l, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low,cross_high,cross_sum
l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low, high, sum = Find_Max_array(l, 0, len(l)-1)
print(low)
print(high)
print(sum)
```

c/cpp:

```cpp
#include<stdio.h>
int Find_cross_left(int *l,int low,int mid,int high)
{
    int sum=0;
    int max_left = mid;
    int left_sum=l[mid];

    for (int i = mid; i >= low; i--)
    {
        sum = sum + l[i];
        if (i<mid)
        {
            if(sum>left_sum)
            {
                left_sum = sum;
                max_left = i;
            }
        }
    }
    return max_left;
}
int Find_cross_right(int *l,int low,int mid,int high)
{
    int sum=0;
    int max_right = mid;
    int right_sum=l[mid];

    for (int i = mid + 1; i < high; i++)
    {
        sum = sum + l[i];
        if (i>mid+1)
        {
            if(sum>right_sum)
            {
                right_sum = sum;
                max_right = i;
            }
        }
    }
    return max_right;
}
int Find_cross_array(int *l,int low,int mid,int high)
{
    int sum=0;
    int max_left = mid;
    int left_sum=l[mid];
    int max_right = mid;
    int right_sum=l[mid];

    for (int i = mid; i >= low; i--)
    {
        sum = sum + l[i];
        if (i<mid)
        {
            if(sum>left_sum)
            {
                left_sum = sum;
                max_left = i;
            }
        }
    }
    sum = 0;
    for (int i = mid + 1; i < high; i++)
    {
        sum = sum + l[i];
        if (i>mid+1)
        {
            if(sum>right_sum)
            {
                right_sum = sum;
                max_right = i;
            }
        }
    }
    return left_sum + right_sum;
}
int low_find_max_array(int *l,int low,int high)
{
    if(high==low)
    {
        return low;
    }
    else
    {
        int mid = ((low + high) / 2);
        int left_low = low_find_max_array(l, low, mid);
        int right_low = low_find_max_array(l, mid + 1, high);
        int cross_low = Find_cross_left(l, low, mid, high);
        int cross_high = Find_cross_right(l, low, mid, high);
        int cross_sum = Find_cross_array(l, low, mid, high);

    }
}
int sum_find_max_array(int *l,int low,int high)
{
    if(high==low)
    {
        return l[low];
    }
    else
    {
        int mid = ((low + high) / 2);
        int left_sum = sum_find_max_array(l, low, mid);
        int right_sum = sum_find_max_array(l, mid + 1, high);
        int cross_low = Find_cross_left(l, low, mid, high);
        int cross_high = Find_cross_right(l, low, mid, high);
        int cross_sum = Find_cross_array(l, low, mid, high);
        if(left_sum>=right_sum &&left_sum>=cross_sum)
            return left_sum;
        else if (right_sum>=left_sum && right_sum>=cross_sum)
            return left_sum;
        else
            return cross_sum;
        }
}
int main(int argc, char const *argv[])
{
    int l[16] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    int sum = sum_find_max_array(l, 0, 15);
    printf("%d", sum);
    return 0;
}
```

### Analyzing the algorithm of the max subarray

对第一个函数分析\(T(n)=\Theta (n)\)
对整个进行分析，每次分解问题，就是把一个'大'数组分解成两个小数组，且每个小数组的求解时间为\(T(n/2)\),所以得出

$$
T(n)=2T(n/2)+\Theta (n)
$$

we analyze the first function,\(T(n)=\Theta (n)\)
And now, let's care about the whole case, every time, we divide a big array to two subarray, and the time to solve a subarray is \(T(n/2)\),so we get

$$
T(n)=2T(n/2)+\Theta (n)
$$

## wait for my math class

由于我的线代没跟上，所以后边的暂时不写。
sorry for that.
