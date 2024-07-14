---
title: binary tree
catalog: true
date: 2018-09-21 23:02:28
mathjax: true
subtitle:
header-img:
tags: Introduction to Algorithms
---

# 二叉树 binary tree

我注意到算导的第二章的堆排序需要二叉树，我发现我记得不是很清楚了，所以写这篇文章来复习，并且讲解一下。
we need binary tree to learn heapsort, so I write this artist to introduce binary tree.

## 定义 definition

二叉树的递归定义如下：二叉树要么为空，要么由根节点、左子树、右子树组成
The recursive definition of a binary tree is as follows: the binary tree is either empty or consists of a root node, a left subtree, and a right subtree.
<!--  -->

这里我们仅仅讨论完全二叉树
we talk about complete binary tree here.

## 性质 property

二叉树的\(i\)层至多有\( 2^{i-1} \)个节点。
>二叉树的第i层至多拥有\(2^{i-1} \)个节点；深度为\( k\)的二叉树至多总共有 \(2^{k+1}-1个节点（定义根节点所在深度\( k_{0}=0\)，而总计拥有节点数匹配的，称为“满二叉树”；深度为\(k\)有\(n\)个节点的二叉树，当且仅当其中的每一节点，都可以和同样深度\(k\)的满二叉树，序号为1到\(n\)的节点一对一对应时，称为完全二叉树。对任何一棵非空的二叉树 \(T\)，如果其叶片（终端节点）数为\(n_0\)，分支度为2的节点数为 \(n_{2}\)，则\(n_{0}=n_{2}+1 \).与普通树不同，普通树的节点个数至少为1，而二叉树的节点个数可以为0；普通树节点的最大分支度没有限制，而二叉树节点的最大分支度为2；普通树的节点无左、右次序之分，而二叉树的节点有左、右次序之分。

这里取自维基百科，其实注意观察上边的图就能理解。
just focus on the picture.
以上援引自[维基百科](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E6%A0%91)

## 代码 code

### 二叉树的编号

> 参考[UVa679](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=620)
> 参考[算法竞赛入门经典](https://book.douban.com/subject/25902102/)148页

***
具体题目见于[UVa679](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=620)

有一棵二叉树，最大深度为D，且所有的叶子深度相同。每个节点都有开关，初始节点都是关闭的，每当有小球落到开关上时，状态都会改变。当小球到达一个内节点时，如果该节点上的开关关闭，则往左走，否则往右走，直到走到叶子结点。
<!--  -->
***
注意到，对\(k\)结点，其左子叶的编号为\(2k\),其右子叶编号为\(2k+1\).
自己可以试试这道题,题解可以自行搜索到

### 二叉树的层次遍历

> 参考[UVa122](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=58)
> 参考[算法竞赛入门经典](https://book.douban.com/subject/25902102/)150页

具体题目见于[UVa122](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=58)

我们从根节点开始定义

```cpp
struct Node
{
    bool have_value;
    int v;
    Node *left,*right;
    Node():have_value(false),left(NULL),right(NULL){};
}
Node *root;//二叉树的根节点
```

该定义对绝大部分二叉树的节点定义基本类似。
同时，我们封装一个申请空间的函数如下，以增强代码可读性

```cpp
Node* newnode(){return new Node();}
```

这里给出addnode函数的定义

```cpp
void addnode(int v,char *s)
{
    int n=strlen(s);
    Node* u=root;
    for(int i=0;i<n;i++)
    {
        if(s[i]=='L')
        {
            if(u->left==NULL)
                u->left=newnode();
            u=u->left;
        }
        else if(s[i]=='R')
        {
            if(u->right==NULL)
                u->right=newnode;
            u=u->right;
        }
        if(u->have_value)
            failed=true;
        u->v=v;
        u->have_value=true;
    }
}
```

接下来就是重头戏，宽度优先遍历(BFS)

```cpp
bool bfs(vector<int>& ans)
{
    queue<Node* > q;
    ans.clear();
    q.push(root);
    while(!q.empty())
    {
        Node* u = q.front();
        q.pop();
        if(!u->have_value)
            return false;
        ans.push_back(u->v);
        if(u->left != NULL)
            q.push(u->left);
        if(u->right!=NULL)
            q.push(u->right);
    }
    return true;
}
```

我们认真阅读这段代码，最好画个图，这样有助于理解。
这段代码的意思就是，我们先创造一个队列，队列有先进先出的原则。我们先把跟结点放进队列，然后把他的子叶放进队列，然后弹出父节点，之后在每次弹出队列中元素时把他的子叶放进队列，重复这个循环，这就是层次遍历。

### 二叉树的递归遍历

这里我们给出给出二叉树的递归遍历的定义：

+PreOrder(T)=T的根节点+PreOrder(T的左子树)+PreOrder(T的右子树)
+InOrder(T)=InOreder(T的左子树)+T的根节点+InOrder(T的右子树)
+PostOrder(T)=PostOrder(T的左子树)+PostOrder(T的右子树)+T的根节点

这就是DFS
那之前那张图来举例
<!--  -->
这张图的先序遍历为1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
中序遍历为8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
后序遍历为8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
应该没写错，如果写错了，记得在下边留言。
如果有兴趣可以做一下UVa548和839.刘汝佳的书真的好。
