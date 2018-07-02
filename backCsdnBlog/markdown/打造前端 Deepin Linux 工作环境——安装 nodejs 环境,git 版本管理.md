---
title: "打造前端 Deepin Linux 工作环境——安装 nodejs 环境,git 版本管理"
date: 2017-11-03 13:57:31 +0800
lastmod: 2017-11-03 13:57:31 +0800
author: fungleo
preview: "打造前端DeepinLinux工作环境——安装nodejs环境,git版本管理好的，前面我们已经对系统进行了基本的设置，然后我们从这一篇博文开始，就要非常认真的开始配置我们的工作环境了。对了，我们要理解，我们的deepinlinux系统是基于Debian系统开发的，所以，我们在找资料的时候，以Debian系统为准。安装nodejs首先，我们打开nodejs官方网站h"
tags: ["git", "debian", "deepin", "nodejs", "npm"]
categories:
    - Linux\CentOS
---

#打造前端 Deepin Linux 工作环境——安装 nodejs 环境,git 版本管理

好的，前面我们已经对系统进行了基本的设置，然后我们从这一篇博文开始，就要非常认真的开始配置我们的工作环境了。

对了，我们要理解，我们的 `deepin linux` 系统是基于 `Debian` 系统开发的，所以，我们在找资料的时候，以 `Debian` 系统为准。

## 安装 nodejs

首先，我们打开 `nodejs` 官方网站 https://nodejs.org/en/ 点击菜单栏的 **Download** 链接，进入下载界面

![nodejs](http://img.blog.csdn.net/20171103131234544?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

滚动页面到下面，点击 `Installing Node.js via package manager` 链接，进入用包管理安装软件的页面。

![Installing Node.js via package manager](http://img.blog.csdn.net/20171103131423598?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

点击 `Debian and Ubuntu based Linux distributions` 跳转到安装指导内容区域

![Debian and Ubuntu based Linux distributions](http://img.blog.csdn.net/20171103131737778?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我们可以看到，执行命令 `sudo apt-get install -y nodejs` 来进行安装 `nodejs`，然后我们就打开终端，输入这个命令，然后盲输入密码，就可以安装我们需要的 `nodejs` 了。

> 我大可以直接给出命令，让大家直接执行就好，通过这段在网站的查找资料，是为了告诉大家，如何在网上找我们的需要的资料。

![install nodejs](http://img.blog.csdn.net/20171103132310809?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

另外，我们还需要安装 `npm` 包管理器。同样，我们执行命令 

```#
sudo apt-get install -y npm
```

进行安装。

![install npm](http://img.blog.csdn.net/20171103132504234?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如上图所示，我们输入 `npm -v` 可看到输出了我们安装的版本号，说明安装已经成功了。

但是我发现，输入 `node` 不能进入到 `node` 环境，而要输入 `nodejs` 才可以进入环境，这多多少少让我感觉有点不爽。所以我决定做一个命令映射，让我的输入和 `mac`平台一样。

首先，我在 `~` 家目录中，用 `ls -a` 命令，看是否存在 `.bash_profile` 文件。看来系统默认是没有这个文件的。

于是，我用 `vim .bash_profile` 创建这个文件，录入以下内容：

```#
alias node="nodejs"
```
`:wq` 保存退出之后，在终端里输入

```#
. ~/.bash_profile
```
命令，使我们刚刚输入的内容生效，然后我们输入

```#
node -v
```

看是否能够输出我们的版本号

![node -v](http://img.blog.csdn.net/20171103134300194?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如上图所示，已经和我设想的是一样一样的了。

> 其实我们大可以使用 `nodejs` 来启动 `node` 环境，我补充这一段内容是为了告诉大家，如何将一个较长的命令，通过我们的 `~/.bash_profile` 的配置变成一个较短的命令，这样便于我们更好的使用我们的命令行工具。

## 安装 git 版本工具

我们在终端中输入

```#
apt-cache search git | grep ^git
```
来搜索我们的 `git` 安装包，为什么我后面增加了一个`| grep ^git` 这样的东西？这是为了过滤我们的信息，默认信息会非常的多，我们可以通过 `grep` 工具来对各种信息进行过滤。更多内容请参考 http://blog.csdn.net/fungleo/article/details/76588993

![apt-cache search git](http://img.blog.csdn.net/20171103135220717?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我们可以看到，我们要安装的，就叫 `git`。于是，我们输入

```#
sudo apt-get install git -y
```

安装 `git` 版本管理工具

![sudo apt-get install git -y](http://img.blog.csdn.net/20171103135424432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如上图所示，我们输入 `git --version` 可以看到输出了正确的 `git` 版本号。说明我们的 `git` 已经安装完成了。

> 我在博文中会穿插更多的内容，引申出来一些东西，是为了让大家更好的思考一些东西。我建议大家收藏我的博客，因为我的博客里面干货满满哦！

本文由 FungLeo 原创，允许转载，但转载必须保留首发链接。