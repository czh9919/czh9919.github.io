---
title: 安装docker
catalog: true
date: 2018-11-30 05:14:23
mathjax: true
subtitle:
header-img:
tags: 好玩的东西
---
# Docker

老服务器被人ddos了，烦人，就换了个新的，想着好玩，得做点啥。暂时没想好就先把docker搭出来，过几天想想咋玩，就先写个安装docker的教程吧. docker可玩性很高的，比如配置复杂环境时，可以直接生成镜像，让大家低成本使用。

## Docker安装

首先设置存储库，
    更新apt

    $ sudo apt-get update

安装包使apt通过HTTPS使用存储库：

    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
之后添加Docker的官方GPG密钥

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

通过搜索指纹的最后8个字符，确认现在拥有指纹9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88的密钥。

    $ sudo apt-key fingerprint 0EBFCD88
返回值应为

    pub   4096R/0EBFCD88 2017-02-22
          Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
    uid                  Docker Release (CE deb) <docker@docker.com>
    sub   4096R/F273FCD8 2017-02-22
使用以下命令设置stable分支下的存储库。即使您还想从其他分支存储库安装构建，您始终需要stable分支下的存储库。要添加其他分支存储库，请在以下命令中的单词stable之后添加单词edge或test（或两者都加，这个随便）。

>Note: The lsb_release -cs sub-command below returns the name of your Ubuntu distribution, such as xenial. Sometimes, in a distribution like Linux Mint, you might need to change $(lsb_release -cs) to your parent Ubuntu distribution. For example, if you are using Linux Mint Rafaela, you could use trusty.

加入docker的源

    $ sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"

[Learn about stable and edge channel](https://docs.docker.com/install/)
接下来更新apt

    $ sudo apt-get update

要安装特定版本的Docker CE，请列出repo中的可用版本，然后选择并安装：
a. 列出您的仓库中可用的版本：

    apt-cache madison docker-ce

之后安装，如果需要安装某个特定版本，就在后边加package的name
这里我就安装最新版本

    $ sudo apt-get install docker-ce

安装完就测试下

    $ sudo docker run hello-world

以上是Ubuntu18.04.1下的安装方法。

## 其他问题

如果出现权限问题，要把用户加入docker组中

    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER # $USER改成自己用户名

>参考资料[安装文档](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1) 
[权限问题的处理](https://docs.docker.com/install/linux/linux-postinstall/#configuring-remote-access-with-systemd-unit-file)