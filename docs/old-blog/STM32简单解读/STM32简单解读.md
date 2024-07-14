---
title: STM32简单解读
catalog: true
date: 2019-01-11 23:26:27
mathjax: true
subtitle:
header-img:
tags: 电子设计大赛
---

# STM32的简单解读

看了下这破玩意的手册，我觉得吧，还是用最小系统板合适，这种东西会的人嫌麻烦，不会的人还是不会。其实这玩意儿就是最小系统板。该文章由于本作者的水平限制，如有错漏之处，麻烦指出，实在抱歉。

## 开发环境

开发板：STM32F103c8
内核ARM Cortex-M3
软件开发环境：KEIL5

开发所需资料：[芯片手册](https://www.st.com/resource/en/datasheet/cd00161566.pdf)
[数据手册](https://www.st.com/resource/en/datasheet/cd00210843.pdf)
突然发现有些不太对，我用的是中文手册，晚点更改链接，我会把图全发出来，所以暂时以图为准吧，实在抱歉。
<!-- ![电路原理图](1.png) -->

## 基本知识

### 高低电平

电平也称电压,电势差，\(V=-\nabla E\)，一般在STM32中，高电平为3.3V，低电平为接地电压，0V。而在C51中，高电平为5V，低电平为0V。

### 特殊功能寄存器

特殊功能寄存器也是一种寄存器，他和内存并没有什么本质上的不同，用于存放相应功能部件的控制命令，状态或数据。这个东西在51中我记得叫SFR。控制这单片机内部所有的功能电路。

### 映射地址

比喻一下，就是你家的门牌号，把单片机中的物理地址分配给特殊功能寄存器就是地址映射。

## 芯片手册的查找

如图所示
<!-- ![图](2.png) -->
我们回到LED模块
<!-- ![LED](4.png) -->
我们可以看出RGB三条线分别接在\(R_7\) \(R_6\) \(R_5\)一端，电阻的另一端接在三种颜色的LED上。二极管的两个引脚具有正负极区分，如图所示，LED的正极连在3.3V上，负极经过电阻与RGB三条线。那俩个三极管暂时略过，暂时不分析他们。
记得刚刚基础知识里的高低电平的概念吗？如果我们现在要使LED灯亮，输入端需要置为高电平还是低电平呢？
我们要让二极管工作，从输入源需要输入一个低电平，即可让二极管两端压降大于0.6V(一般二极管工作电压为0.6V)，相反输入高电平则二极管的负极一端不会产生任何作用！
现在LED模块的电路原理图基本看懂了，现在就要知道LED模块连接在处理器的哪个总线上，这样就能达到控制LED灯的效果。

    这里就拿找人打个比喻吧：
    就像找人一样，你知道他是谁，是干什么的，但是你现在想要找到他，是不是要去他家里？
    那么去他家里之前你要知道他家在哪儿，房子编号是多少，有个具体的路线和编号就可以轻而易举的找到他家，然后才能找到他。

现在我们看一下，RGB这三根线接在哪里
<!-- ![电路原理图](1.png) -->
放大一点
如图所示
<!-- ![图](2.png) -->
注意到RGB连在PB3，PB4和PA15这几个
联系找人那个比喻和那个基础和基本知识中特殊功能寄存器和映射地址的介绍。我们现在就需要去找RGB三根线所对应的特殊功能寄存器。这里就可以看我们的[数据手册](https://www.st.com/resource/en/datasheet/cd00210843.pdf)12页。我们可以在这里找到对PB，PA特殊功能寄存器总线挂接介绍的原理图：
<!-- ![图](3.png) -->
放大一点
<!-- ![图](5.png) -->
如上图，我们以PB特殊寄存器为例，可以看到PB特殊功能寄存器是由GPIO端口为B的GPIO管脚所连接的，而GPIO端口B挂设到ABP2总线上，而AHB总线又挂载在AHB2系统总线上
<!-- ![图](6.png) -->
注意这个挂设怎么区分的，首先GPIO端口B实则上是一组GPIO管脚组成的，只不过该管脚负责PC特殊功能寄存器的I/O操作，其他GPIO管脚负责其它的特殊功能寄存器，列如PA,PC等，ARM为了加以区分，让开发人员更易读，所以为其进行了区分，也就是成了端口C，端口E，端口G等，分别对应不同的特殊功能寄存器，上面的总结和系统总线的区分打比喻就是一组里有小组的情况一样，每个小组对应不同的功能，但用管理一个组的方式管理所有的小组，而这个组的名字叫做系统总线。
地址总线，数据总线和控制总线都是系统总线。
<!-- 我们现在查[芯片手册](https://www.st.com/resource/en/datasheet/cd00161566.pdf)
![系统结构](7.png)
总线与存储之间的分组架构：
![图](8.png)
现在我们知道了挂设总线，就像找人需要找住址，现在我们就要知道特殊功能寄存器的映射。
![图](9.png)
放大看
![图](10.png)
也有如下图
![图](11.png) -->

    LED模块对应的特殊功能寄存器：PA,PB寄存器
    PA,PB寄存器对应的GPIO：GPIO_A,GPIO_B
    GPIO_C挂设在：APB2外设总线上,且偏移起始地址为：0x4001 0800 - 0x4001 0BFF及0X4001 0C00 - 0x4001 0FFF
    APB2外设总线挂接在：AHB2系统总线上
我们继续往下走，如下图，注意到，AHB总线又是由复位和时钟(RCC)电路控制的。
<!-- ![图](12.png) -->
至于我们为什么要设置这个RCC电路，其实是为了降低功耗,这里不展开，主要是我水平低，不知道具体为什么这个东西的工作原理是什么，更别说讲清楚了，所以讲一下结论。
有了这个RCC，我们可以保持住管脚电压，如果没有，存储单元需要一直把电平信号输出到管脚上去。所以能省电。
所以我们要想要让LED灯亮起就必须将控制AHB系统总线的RCC时钟电路设置成推送状态,查找手册
第六章6.3
然后我们只要看，
<!-- ![图](13.png)
![图](14.png) -->
如上图偏移地址为0x0C，同时找到RCC的地址，把头地址加上偏移量，就能找到该寄存器的位置即为‭0x 4002 100C。
‬到此，结束了地址的查找，挺难受的哈。
现在我们看GPIO口的描述
<!-- ![图](15.png) -->
x=A...E表示GPIOA到GPIOE都有该寄存器。
<!-- ![图](16.png) -->
y表示对应管脚号。
然后下边是对应引脚功能,然后是以4bit做分割的。
<!-- ![图](17.png) -->
ODR寄存器是端口输出寄存器，是output data register 的缩写
这里看好了，如果ODRy是PB寄存器，我们对GPIOB的BSRR寄存器的高16位写入一个高电平，对应的GPIOB就会向PB发送一个低电平。
如果想让PB0输出一个低电平，那么就是向GPIOB的BSRR寄存器的高第16位写入一个高电平，如果输出一个低电平，就是向GPIO的BSRR寄存器的低第16位写入一个低电平。
所以如果想让PB3输出一个低电平，就是向GPIO的BSRR寄存器的高第16+3位输出一个高电平，如果输出一个低电平，就是向GPIO的BSRR寄存器的低第16+3位写入一个低电平。

## 实践开发

创建新工程，开发包选STM32F103C8.
首先把基址定义出来

```c
#define BLOCK_2 (unsigned int)0x40000000
```

继续定义我们所需要的APB2的基址

```c
#define BLOCK_2_APB2_GPIO_B (BLOCK_2+0x10000)
```

然后CRL寄存器是控制工作状态的
偏移地址：0x00

```c
#define BLOCK_2_GPIOB_CRL  *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x00)
```

然后设置BSRR

```c
#define BLOCK_2_GPIOB_BSRR 	 	 *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x10)
```

除此之外，还要开启APB2时钟电路
基址为0x4002 1000

```c
#define BLOCK_2_RCC_BASE (BLOCK_2 + 0x21000)
#define BLOCK_2_RCC_APB2 *(unsigned int*)(BLOCK_2_RCC_BASE+0x14)
```

整理一下

```c
#define BLOCK_2 (unsigned int)0x40000000
#define BLOCK_2_APB2_GPIO_B (BLOCK_2+0x10000)
#define BLOCK_2_GPIOB_CRL  *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x00)
#define BLOCK_2_GPIOB_BSRR 	 	 *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x10)
#define BLOCK_2_RCC_BASE (BLOCK_2 + 0x21000)
#define BLOCK_2_RCC_APB2 *(unsigned int*)(BLOCK_2_RCC_BASE+0x14)
```

然后写下所有的代码，即为：

```c
#define BLOCK_2 (unsigned int)0x40000000
#define BLOCK_2_APB2_GPIO_B (BLOCK_2+0x10000)
#define BLOCK_2_GPIOB_CRL  *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x00)
#define BLOCK_2_GPIOB_BSRR  *(unsigned int*)(BLOCK_2_APB2_GPIO_B+0x10)
#define BLOCK_2_RCC_BASE (BLOCK_2 + 0x21000)
#define BLOCK_2_RCC_APB2 *(unsigned int*)(BLOCK_2_RCC_BASE+0x14)

void SystemInit()
{

}
void sleep(int time){
    while (time--);
}
int main()
{
    BLOCK_2_RCC_APB2 |= 1 << 4;
    BLOCK_2_GPIOB_CRL |= (2 << 4 * 0);
    BLOCK_2_GPIOB_BSRR= (1 << (16 + 3));
    while (1){
        BLOCK_2_GPIOB_BSRR = (1 << (16 + 3));
        sleep(0xFFFF);
        BLOCK_2_GPIOB_BSRR = (1 << (0));
    }
}
```
