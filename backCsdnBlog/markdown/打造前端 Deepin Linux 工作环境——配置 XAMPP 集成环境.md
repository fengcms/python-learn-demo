---
title: "打造前端 Deepin Linux 工作环境——配置 XAMPP 集成环境"
date: 2017-11-03 20:16:01 +0800
lastmod: 2017-11-03 20:16:01 +0800
author: fungleo
preview: "打造前端DeepinLinux工作环境——配置XAMPP集成环境虽然前后端分离开发的我们，已经很少需要跑一个apache+php+mysql的集成环境了。但是我想可能还是有很多的人是需要跑这个环境的。所以我讲一下，这个东西到底是怎么配置的。下载并安装XAMPP集成环境首先，我们打开官方网站的下载页面https://www.apachefriends.org/zh_cn/downl"
tags: ["apache", "mysql", "php", "deepin", "xampp"]
categories:
    - Linux\CentOS
---

#打造前端 Deepin Linux 工作环境——配置 XAMPP 集成环境

虽然前后端分离开发的我们，已经很少需要跑一个 `apache+php+mysql` 的集成环境了。但是我想可能还是有很多的人是需要跑这个环境的。所以我讲一下，这个东西到底是怎么配置的。

## 下载并安装 XAMPP 集成环境

首先，我们打开官方网站的下载页面 https://www.apachefriends.org/zh_cn/download.html 然后选择我们需要的版本进行下载，这里，我选择最新的版本，如下图所示：

![下载XAMPP](http://img.blog.csdn.net/20171103194353770?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我也是第一次下载安装 `XAMPP` ，以前在 `Arch linux` 是用命令行安装的，所以，我们来看一下帮助文档，点击下载页面右侧的 [linux常见问题](https://www.apachefriends.org/zh_cn/faq_linux.html)

好的，第一个就是告诉我们，如何来安装这个东东的。

![linux常见问题](http://img.blog.csdn.net/20171103194825004?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好的，我们来执行命令：

```#
# 设定安装文件的权限
chmod 755 xampp-linux-*-installer.run
# 用超级权限来执行安装文件
sudo ./xampp-linux-*-installer.run
```

运行结果如下图所示：

![设定安装文件的权限](http://img.blog.csdn.net/20171103195004496?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

然后居然很神奇的出现了这个图形界面的玩意儿。

![xampp1](http://img.blog.csdn.net/20171103195459563?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![xampp2](http://img.blog.csdn.net/20171103195510347?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![xampp3](http://img.blog.csdn.net/20171103195520946?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![xampp4](http://img.blog.csdn.net/20171103195532968?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这里有一个我们不需要的东西，我们去掉勾选。

![xampp5](http://img.blog.csdn.net/20171103195543100?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![xampp6](http://img.blog.csdn.net/20171103195555639?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![xampp7](http://img.blog.csdn.net/20171103195705362?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好的，安装完成了。然后就出现了这样的界面：

![xampp运行界面](http://img.blog.csdn.net/20171103195950039?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

然后，我们在浏览器中输入 http://127.0.0.1 就可以看到效果了。

![apache 运行界面](http://img.blog.csdn.net/20171103200204826?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好的。我们可以很方便的用图形界面来管理我们的 `xampp` 集成环境了，具体不再详述，使用过这个环境的朋友应该都知道怎么跑起来的。

## 配置 xampp 环境

首先，我们可以从刚刚的官方 `linux` 帮助文档里面找到两条命令，分别是启动和关闭 `xampp` 的。

```#
# 启动 xampp
sudo /opt/lampp/lampp start
# 关闭 xampp
sudo /opt/lampp/lampp stop
```

![运行结果](http://img.blog.csdn.net/20171103200826719?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

但是这个命令确实是有点太长了。还记得我们前面讲的如何讲长的命令变成短的命令吗？这里，我们也来配置一下：

```#
vim ~/.bash_profile
```
编辑个人终端配置文件，录入以下内容
```#
alias xpst="sudo /opt/lampp/lampp start"
alias xpsp="sudo /opt/lampp/lampp stop"
alias xprs="sudo /opt/lampp/lampp restart"
```
然后 `:wq` 保存文件

```#
. ~/.bash_profile
```
使配置文件生效，然后我们运行以下我们的简写命令，看能否正常运行：

![简写命令是否正常运行](http://img.blog.csdn.net/20171103201310193?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如上图所示，我们的简写命令是可以运行的，嘿嘿，这样我们就可以用很短的命令来运行环境，并且，不用管那个控制面板了。

这篇博文已经很长了，下一章我们再来讲更多的配置。

本文由 FungLeo 原创，允许转载，但转载必须保留首发链接。