---
title: VS code写C/C++
catalog: true
date: 2019-03-07 22:21:14
mathjax: true
subtitle:
header-img:
tags: 安利
---
# VS code写C++

c++兼任c，所以干脆一点，就出一个VS code写c++的教程。参考资料见文章最后。
>If you just want a lightweight tool to edit your C++ files, Visual Studio Code is a great choice but if you want the best possible experience for your existing Visual C++ projects or debugging on Windows, we recommend you use a version of the Visual Studio IDE such as Visual Studio Community.
如果您只想要一个轻量级工具来编辑C ++文件，Visual Studio Code是一个很好的选择，但如果您希望获得现有Visual C ++项目的最佳体验或在Windows上进行调试，我们建议您使用Visual Studio IDE的一个版本例如Visual Studio社区版。

其实我推荐Clion，嘻嘻。但VS code在我看来很适合写平时的作业。

## Get started

先安装VS code，就，[VS code官网](https://code.visualstudio.com/)下载安装。
然后安装插件，在这里
<!-- ![1](1.png) -->
<!-- 里面搜索![c/c++](2.png)这个插件 -->
单击“ 安装”，然后单击“ 重新加载”。

>题外话：这个拓展没有包含编译器，所以我们要自己下，这里我一会儿将以clang为例继续讲。

这里我们打开一个包含c/c++代码的文件夹，在里面新建一个名为.vscode的子文件夹，这里我们用来储存设置文件。

## 设置IntelliSense

文档里说这个拓展会根据系统自动生成，我们在.vscode里可以找到c_cpp_properties.json文件文件来更改设置，当然你现在找不到也是正常的。

<del>这里我们随便打开一个一个c/c++文件，在#include下有绿色波浪线，前面有一个灯泡，点一下，(玩一年:)),点击"Edit includePath setting"，就打开了那个c_cpp_properties.json文件</del>

我们按Ctrl+Shift+P，里点c/c++：Edit configuration，这里我们就找到了c_cpp_properties.json文件，这里我们阅读该文件，发现我们win系统下的默认编译器为MSVC，可能和我不一样。。。
我的文件是这样的

```js
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "windowsSdkVersion": "10.0.16299.0",
            "compilerPath": "C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.12.25827/bin/Hostx64/x64/cl.exe",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "msvc-x64"
        }
    ],
    "version": 4
}
```

我现在想把他改为clang，只需以官方文档的MinGW C++ compiler的设置文件为基础，拿来用就好。

```js
{
    "name": "Win32",
    "includePath": [
        "${workspaceFolder}"
    ],
    "defines": [
        "_DEBUG",
        "UNICODE",
        "__GNUC__=7",
        "__cdecl=__attribute__((__cdecl__))"
    ],
    "compilerPath": "C:\\mingw-w64\\bin\\gcc.exe",
    "intelliSenseMode": "clang-x64",
    "browse": {
        "path": [
            "${workspaceFolder}"
        ],
        "limitSymbolsToIncludedHeaders": true,
        "databaseFilename": ""
    }
}
```

然后按照你的安装自己改路径，我当时把clang和mingw合并了，即用clang直接编译，头文件用mingw的，这样就很方便了。
最后我们把自己的路径放进去，就是这样的

```js
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "__GNUC__=7",
                "__cdecl=__attribute__((__cdecl__))"
            ],
            "compilerPath": "C:\\mingw-w64\\bin\\gcc.exe",
            "intelliSenseMode": "clang-x64",
            "browse": {
                "path": [
                    "${workspaceFolder}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            }
        }
            ],
    "version": 4
}
```

## 编译

在写完代码之后，我们需要编译，并build。
打开the Command Palette (Ctrl+Shift+P).点击Tasks: Configure Task，点击Create tasks.json file from templates,然后选择others.
我们这里用clang，所以我们先把文档中的示例拿出来，以他为基础进行更改。
我们先看下微软给的示例

```js
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build hello world",
            "type": "shell",
            "command": "g++",
            "args": [
                "-g", "helloworld.cpp"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

他这里是用g++的，我们用的是clang，所以改成clang即可，lebel微软默认是build，因为他这里其实是用来构建项目的，（其实这里没啥要求，反正我感觉微软的定义是这里为一个任务，所以这里放个啥任务都行，碎碎念）我们这里用来编译，保持一个好习惯很重要，所以把label改成Compile,然后arg是用来写在调用此任务时传递给命令的参数，这里就看个人，你爱加啥加啥

```js
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Compile",
            "type": "shell",
            "command": "clang++",
            "args": [
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}.exe",
                "-g",
                "-Wall",
                "-static-libgcc",
                "-fcolor-diagnostics",
                "--target=x86_64-w64-mingw",
                "-std=c++17"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

## Debug

如果你不打算debug的话，这里就结束了:).
所以我们这里继续，先生成一个名为launch.json的文件。
步骤为
在左侧边栏有个debug的图标，在绿色箭头的右边有个没有配置:),下拉，添加配置，选择C++ (GDB/LLDB)，这将创建一个launch.json文件。我们这里用的是GDB调试。

```js
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "enter program name, for example ${workspaceFolder}/a.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "/path/to/gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

program是调试路径，我们这里改下(废话)

```js
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "/path/to/gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": false
                }
            ]
        }
    ]
}
```

而且，如果你有过在命令行下调试的基础的话，在你调试前，肯定是需要先编译的，所以还要再改一个地方，就是在执行调试之前先编译构建。

```js
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "gdb.exe",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": false
                }
            ],
            "preLaunchTask": "Compile"
        }
    ]
}
```

至此，全部搞定。
推荐一波插件吧

## 插件

1.Bracket Pair Colorizer 彩虹花括号
2.C/C++ clang Command Adapter
3.C/C++ Snippets
4.code runner(神器)
5.Include Autocomplete
6.Visual Stdio IntelliCode
7.VS Live Share(面向对象编程???)

## 补充

有人不知道我的clang的安装过程，所以我在这补充一下
进入该网站
http://releases.llvm.org/download.html
选Pre-Built Binaries中的Windows (64-bit)，不需要下.sig文件。
和这个网站
https://sourceforge.net/projects/mingw-w64/
下载就行。
然后安装clang的时候要添加环境变量，就是那个Add LLVM to the system PATH for all/current users
MinGW随便装哪，Architecture选x86_64，装好以后把东西全部复制到Clang的文件夹里去，他们会无冲突合并。
这里其实有点像Linux的包管理。
呃，你说下载不了，打不开，呃，正常，自己想办法。
然后在cmd中输入clang，返回为clang.exe: error: no input files，这样就对了(起码你clang的环境变量没忘记加，应该成功安装了)。

>参考资料：https://www.zhihu.com/question/30315894  
https://code.visualstudio.com/docs/languages/cpp#_windows-debugging-with-gdb