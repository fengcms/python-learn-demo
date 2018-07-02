---
title: "打造前端 Deepin Linux 工作环境——安装最新版本的火狐firefox浏览器"
date: 2017-11-06 18:02:56 +0800
lastmod: 2017-11-06 18:02:56 +0800
author: fungleo
preview: "打造前端DeepinLinux工作环境——安装最新版本的火狐firefox浏览器尝试使用apt-get命令安装火狐浏览器，但是，居然是55的版本，而最新的已经是56了。当然，这并不是我最关心的。而是重要的是，我需要的一些插件只能在最新版本的火狐浏览器里安装。这就让我有点小小的不爽了。没关系，我们手动安装最新版本的火狐浏览器即可。首先，我们在火狐浏览器官方找到最新版本的中文版本的下载"
tags: ["firefox", "deepin", "火狐", "前端"]
categories:
    - Linux\CentOS
---

#打造前端 Deepin Linux 工作环境——安装最新版本的火狐firefox浏览器

尝试使用 `apt-get` 命令安装火狐浏览器，但是，居然是 `55` 的版本，而最新的已经是 `56` 了。当然，这并不是我最关心的。而是重要的是，我需要的一些插件只能在最新版本的火狐浏览器里安装。这就让我有点小小的不爽了。

没关系，我们手动安装最新版本的火狐浏览器即可。

首先，我们在火狐浏览器官方找到最新版本的中文版本的下载地址。打开官方网站：http://www.firefox.com.cn/download/#more

![火狐浏览器官方](http://img.blog.csdn.net/20171106172958011?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我右击，复制出来链接地址，进入终端，开启装逼模式：

```#
# 进入下载目录
cd ~/Downloads/
# 下载安装包
wget http://download.firefox.com.cn/releases/firefox/56.0/zh-CN/Firefox-latest-x86_64.tar.bz2
# 解压压缩包(我用的是 atool 工具，标准命令是：tar -jxvf 难记，建议安装 atool)
atool -x Firefox-latest-x86_64.tar.bz2
# 移动文件到系统目录
sudo mv firefox/ /opt/
# 创建图标文件
sudo vim /usr/share/applications/firefox.desktop
```

进入 `vim` 之后，输入以下内容：

```#
[Desktop Entry]
Name=Firefox
Exec=/opt/firefox/firefox
Icon=/opt/firefox/browser/icons/mozicon128.png
Terminal=false
Type=Application
Categories=Application;Network;
```

`:wq` 保存退出。

然后，我们的应用列表里面就有最新版本的火狐浏览器了。

![最新版本的火狐浏览器](http://img.blog.csdn.net/20171106173700841?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


好，然后我们就能打开火狐愉快的玩耍了！

本文由FungLeo原创，允许转载，但转载必须附注首发链接。谢谢。

## 2017年11月17日补充

火狐浏览器已经升级到57版本了。照以上教程也是一样安装的，没有问题。如果之前按照本教程安装了56的版本，只需要用火狐自带的升级功能升级一下，就升级到57版本了。