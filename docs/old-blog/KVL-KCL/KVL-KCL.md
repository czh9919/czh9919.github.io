---
title: KVL-KCL
catalog: true
date: 2018-10-19 19:50:17
mathjax: true
subtitle:
header-img:
tags: Circuit Theory
---

# KVL-KCL

## 基尔霍夫电流定律（KCL）

## 基本介绍

基尔霍夫电流定律是用于电路分析的基本定律之一。由于节点不能储存电能，所以流入节点的电流与流出节点的电流相同。(英文版本：His current law states that for a parallel path the total current entering a circuits junction is exactly equal to the total current leaving the same junction. )
$$
\sum I_{in}=\sum I_{out}
$$

## 例子

对某个节点，如图
<!-- ![基尔霍夫电流定律](\1.png) -->
我们可以轻松观察到干路电流等于两支路电流之和，而节点不存储电能。
即\(I_3=I_1+I_2\)

## 基尔霍夫电压定律(KVL)

基尔霍夫电压定律也是电路分析的基本定律之一。在闭合回路中，电能不会放大或缩小，所以在闭合回路中，所有元件的电压的代数和为零（怎么讲都好奇怪，这里最好看英文的）
(英文版本：His voltage law states that for a closed loop series path the algebraic sum of allthe voltages around any closed loop in a circuit is equal to zero.)
$$
\sum V=0
$$

## 例子

<!-- ![基尔霍夫电压定律](\2.png) -->

如图所示，有三个可以用来列方程的闭合回路,但有一个没啥用，所以只列两个，和那个特勒根定律一样，注意极性。
$$
V_{Ref 1}+V_{Ref 3}+V_{Ref 2}+V_{Ref 5}+V_{Ref 6}=0
$$
很简单的问题，不多说/