---
title: Basic Concepts
catalog: true
date: 2018-10-08 15:24:47
mathjax: true
subtitle:
header-img:
tags: Circuit Theory
---

# Get started

写这篇博客时，还是发现国内电子方向的学习交流网站较少，比较大的网站像[电子发烧友](http://www.elecfans.com/),缺少对学生的帮助，小的网站或博客也有，有不少有趣的，像[动力老男孩的博客](http://www.diy-robots.com/)，但基础方向的，似乎还是较少,当然咯，动力老男孩的博客是真的有趣。

# introduction

把各个电子元件用导线连接起来(interconnection of electrical elements)就是电路
而我们要学习的就是电路分析。

## Electrical elements

电路中一般分为两类，有源元件和无源元件，有源元件(passive elements)一般指向电路中供电的元件类似电池，发电机这样的，而无源元件(active elements)则指那些只消耗电能的元件，像电阻，电容这样的。  

### 电阻

<!--  -->

### 电容

<!--  -->

### 电感

<!--  -->

### 电压或电流源

这里就不找图了  
在实际中，电压源一般用的比电流源较多。  
电压源又分为独立电压源(Independent Voltage Source)和受控电源(Independent Voltage Source)  
独立电压源就像电池，他的值仅由自身决定  
受控电源就像运算放大器，他的值会因流过源的电流或电压决定。  
受控电压源又分为四小类

+ VCVS: 电压控制电压源(Voltage-Controlled Voltage Source)
+ CCVS: 电流控制电压源(Current-Controlled Voltage Source)
+ VCCS: 电压控制电流源(Voltage-Controlled Current Source)
+ CCCS: 电流控制电流源(Current-Controlled Current Source)

<!--  -->

### 运算放大器(Operational amplifier)

> Amplifier is the generic term used to describe a circuit which produces and increased version of its input signal.

放大器就是用来放大信号的，输出信号与输入信号的比值叫做放大增益(gain)。

### 变压器(Transformer)

未来会细讲

## Charge and Current

电流

$$
I=\frac{Q( C)}{t(s)}
$$


电压


$$
U=\frac{W(J)}{Q( C)}
$$

## Tellegen’s theorem

在满足基尔霍夫定律的任何   电网中，所有分支中的瞬时功率的总和等于零。

$$
\sum ^n_{k=1} P_k =V_k\times I_k =0
$$
\(n\)是电路中元件的数量
\(P_k\)是第k个元件的瞬时功率
\(V_k\)是电路中第k个元件的瞬时电压降
\(I_k\)是流过第k个元件的瞬时电流

例如以下这道题,求\(I_0\)
<!--  -->
*图片如有侵权，请通知博主，博主将立刻删除*

解题如下,注意元件极性(polarity),**如果电流流入元器件正极，那么代入公式时，电流为正，如果流入负极，那么在公式中，电流值为负**

$$
\sum P=P_{2A}+P_1+P_2+P_3+P_{4V}+P_{DS}=6\times (-2)+6\times I_0+12\times (-9)+10\times (-3)+4\times (-8)+4\times (-8)=0
$$

解得\(I_0=1A\)
