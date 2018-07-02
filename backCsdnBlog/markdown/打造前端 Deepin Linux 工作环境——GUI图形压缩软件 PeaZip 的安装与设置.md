---
title: "打造前端 Deepin Linux 工作环境——GUI图形压缩软件 PeaZip 的安装与设置"
date: 2017-11-05 14:57:18 +0800
lastmod: 2017-11-05 14:57:18 +0800
author: fungleo
preview: "打造前端DeepinLinux工作环境——GUI图形压缩软件PeaZip的安装与设置说实话，谁不喜欢简单明了的图形化的软件呢。但是在linux和mac上关于压缩软件的图形化的实在是不多，并且mac上的还收费还不好用。为此，我才用命令行的工具atool的。今天我找到一个好用的图形化的压缩软件PeaZip这个软件。跨平台，开源，功能全面，支持的格式也多。因此，推荐给大家使用"
tags: ["deepin", "压缩", "PeaZip", "Linux"]
categories:
    - Linux\CentOS
    - Tools
---

#打造前端 Deepin Linux 工作环境——GUI图形压缩软件 PeaZip 的安装与设置

说实话，谁不喜欢简单明了的图形化的软件呢。但是在 `linux` 和 `mac` 上关于压缩软件的图形化的实在是不多，并且 `mac` 上的还收费还不好用。为此，我才用命令行的工具 `atool` 的。

今天我找到一个好用的图形化的压缩软件 `PeaZip` 这个软件。跨平台，开源，功能全面，支持的格式也多。因此，推荐给大家使用。

## 安装 PeaZip 压缩软件

打开终端，输入下面的命令进行搜索

```#
apt-cache search peazip
```
看是否包含这个安装包。 `deepin` 我这边看到是有这个包的。所以执行下面的命令安装：

```#
sudo apt-get install peazip -y
```

这个软件依赖的包还比较多，不过没关系，一会儿就安装完成了。

打开软件

![PeaZip](http://img.blog.csdn.net/20171105144723278?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好，我们可以看到这个软件和我们在 `windows` 上接触的 `winrar` 是差不多的。但是默认是英文。所以我们需要设置一下：

## 设置 PeaZip 压缩软件

![PeaZip Menu](http://img.blog.csdn.net/20171105145024432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

首先，我们点击菜单栏的 `Options` 然后点击 `Localization`，会弹出如下方的选择本地语言配置选框，我们选择 `chs.txt` 然后点击 `打开` 就设置好了。

![PeaZip Chs](http://img.blog.csdn.net/20171105145035425?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

设置语言之后，软件会自动重启，重启之后，就可以看到已经全部变成中文了。应该说，还是感到很亲切的。

![PeaZip cinese](http://img.blog.csdn.net/20171105145045384?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

`peazip` 的官方网址是 http://www.peazip.org/peazip-linux.html

本文由FungLeo原创，允许转载，但转载必须附注首发链接。谢谢。