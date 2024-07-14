---
title: Affine/softmax层的实现
catalog: true
date: 2018-08-29 15:30:17
subtitle:
mathjax: true
header-img:
tags: Machine Learning
---
# Affine/Softmax层的实现

## Affine层

如图
<!-- <!--  --> -->

现在来考虑该图的反向传播
$$
\frac {\partial f} {\partial X}=\frac{\partial L}{\partial Y}\cdot W^T
$$
和
$$
\frac{\partial L}{\partial W}=X^T\cdot \frac{\partial L}{\partial Y}
$$
其中\(W^T\)中的**T**表示转制。如下
$$
W=\begin{pmatrix} w_{11} & w_{12}&w_{13} \\\\ w_{12} & w_{22}&w_{23} \\\\ \end{pmatrix}
$$
那么转制为
$$
W^T=\begin{pmatrix} w_{11} & w_{21}\\\\ w_{12} & w_{22} \\\\ w_{13}&w_{23} \\\\ \end{pmatrix}
$$

## 批版本的Affine层

<!-- <!--  --> -->
代码如[Affine](https://github.com/czh9919/Study-notes/blob/master/common/layers.py)中的Affine类所示

### Softmax-with-Loss层

先引出softmax-with-Loss层的计算图,呃，没找到，pass，以后找到了补上
其实这个地方十分复杂，不展开说明
我们直接说明结论，推导将在后面的博文中进行解释
我们正向传播通过softmax层会得到正规化的值(不记得的去复习一下)
把1作为L，反向传播通过softamx层，我们会得到类似于\( y_1-t_1\)这样的结果，这样的话，输出的是当前神经网络的输出与教师标签的误差
代码实现如下

    class SoftmaxWithLoss:
        def __init__(self):
            self.loss=None
            self.y=None
            self.t=None
        def forward(self,x,t):
            self.t=t
            self.y=softmax(x)
            self.loss=cross_entropy_error(self.y,self.t)
        def backward(self,dout=1):
            batch_size=self.t.shape[0]
            dx=(self.y-self.t)/batch_size
            return dx
也可见于[Softmax with Loss](https://github.com/czh9919/Study-notes/blob/master/Deep_Learning/SoftmaxWithLoss.py)

## 误差反向传播法的实现

在组装之前，先去复习下神经网络的全貌图，这里就不写了
这里我们将会在[原两层神经网络](https://github.com/czh9919/Study-notes/blob/master/Deep_Learning/TwoLayerNet.py)上进行更改
具体代码如下[两层神经网络](https://github.com/czh9919/Study-notes/blob/master/Deep_Learning/NewTwoLayerNet.py)
注意OrderedDict，这是有序字典，顺序是向字典里添加元素的顺序。

## 误差反向传播法的梯度确认

确认数值微分求出的梯度呵误差反向传播法求出的结果是否一致的操作叫做梯度确认。
代码[在这](https://github.com/czh9919/Study-notes/blob/master/Deep_Learning/gradient_check.py)

## 使用误差反向传播法的学习

直接展示[代码](https://github.com/czh9919/Study-notes/blob/master/Deep_Learning/new_train_neuralnet.py)
我这里的最后正确率达到了97.858333%