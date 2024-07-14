---
title: VS code 安装STM32教程
catalog: true
date: 2019-01-15 22:38:11
mathjax: true
subtitle:
header-img:
tags: 电子设计大赛
---
# VS code 安装STM32教程

今天实在觉得KELI太丑，突然想到VS code也可以实现STM32代码的编写，遂决定写一个博客，把VScode变成一个STM32的IDE，实现KELI的绝大部分功能，实现编译，链接，下载为一体的DE。参考了如下[开源项目](https://github.com/damogranlabs/VS-Code-STM32-IDE), [GITHUB](https://www.github.com)牛逼。如果有什么问题，欢迎询问我。

## 基于CUBEMX构建VS凑得IDE

先安装[VS code](https://code.visualstudio.com/)

先**安装python**，这个...我就不写教程了，网上多的很，但我还是推荐一波吧，[廖雪峰的博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)

**下载 GNU Eclipse tools:**

* [GNU Eclipse ARM Embedded GCC](https://github.com/gnu-mcu-eclipse/arm-none-eabi-gcc/releases)
* [GNU Eclipse Windows Build Tools](https://github.com/gnu-mcu-eclipse/windows-build-tools/releases)
* [GNU MCU Eclipse OpenOCD](https://github.com/gnu-mcu-eclipse/openocd/releases)  

有点同学可能由于速度或国内的原因无法下载，请自行解决。我也懒得上传百度云了。当然咯，如果你是我的同学，欢迎自行来用U盘拷。注意版本问题，不要下了Linux系统的哈。

等待的时候，我们去VS code的插件市场安装一下Cortex-Debug插件和python插件
如下图
<!-- ![社区市场](3.png)
![Cortex-Debug](1.png)
![python](2.png) -->

然后继续下载CPU特定的SVD文件
在[这里](https://www.keil.com/dd2/pack/)下载。
不用全部下，你也不可能全部下下来，笑:)。
<!-- 只需下载你需要的板子型号所对应的开发包即可。如![开发包](4.png) -->

然后我们把上面下的三个文件和刚刚下载的SVD文件放在一个你熟悉的文件夹下，这个文件夹一定自己要找得到，不过我建议如下目录：％userprofile％\ AppData \ Roaming \ GNU MCU Eclipse，如果不是的话，一会可能要改代码，如图
<!-- ![图](5.png) -->
然后**解压**，我建议把解压出来的文件放在同一个文件夹下。
<!-- 如图![图](8.png) -->

最后，**下载STM32 cubemx**，安装。

## 到这里，就可以开始安装了

打开STM32CUBEMX，创建一个工程，可以看我下边的图，一起做
<!-- ![图](7.png)
创建一个新工程
![图](9.png)
挑选好自己的开发板
之后，我们改下设置
![图](10.png)
![图](11.png)
然后生成代码
![图](12.png) -->
然后用VS code打开工程生成的代码的文件夹

然后，我们下载[这里的所有文件](https://github.com/damogranlabs/VS-Code-STM32-IDE/tree/master/ideScripts),放入CUBEMx生成代码的目录，也就是VS code现在打开的目录，如图

<!-- ![图](13.png) -->

这是我的完成版
然后用python运行ideScripts的update.py
按如图所示填入
<!-- ![图](15.png) -->
然后，如图所示，即为成功
<!-- ![图](16.png) -->
这里有一个问题，需要注意，所有路径不要包含空格，不然无法构建。
然后，打开main.c,按Ctrl+P，输入>Run，可见运行任务，然后build，测试即可。
至此，我们完成了基本构建，如果，还有别的需求，请自行查阅资料，或在评论区询问。

    参考资料：https://github.com/damogranlabs/VS-Code-STM32-IDE