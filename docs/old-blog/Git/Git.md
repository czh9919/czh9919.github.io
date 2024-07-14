---
title: Git
catalog: true
date: 2018-10-13 19:31:17
subtitle:
header-img:
tags: Git
---

# Git 备忘

从[这个牛逼的网站学的](https://learngitbranching.js.org/)，自己可以去试试。

git commit 提交一个更改，git会把更改打包在新结点中，所以git是个树结构
git branch新建一个分支。
git checkout < new branch> 告诉git我们想切换到那个新建的分支上。
如果你想创建一个新的分支同时切换到新创建的分支的话，可以通过 git checkout -b < your-branch-name> 来实现。
git merge 如图
<!-- <!--  --> -->
<!-- <!--  --> -->
***
git rebase
有点懵
head指针通常指向最近一次更改
git checkout head^
表示移动到父位置
git branch -f master HEAD~3
上面的命令会将 master 分支强制指向 HEAD 的第 3 级父提交。
git reset HEAD~1 撤销更改
git revert HEAD是创建一个新提交，这个提交与原提交的父提交相同
***
git cherry-pick c2 c4 Git 就将被c2 c4抓过来放到当前分支下了。 就是这么简单!
git rebase -i HEAD~4
