---
title: "linux|mac 日常入门命令行使用——搜索文件|文件夹"
date: 2017-11-09 14:43:07 +0800
lastmod: 2017-11-09 14:43:07 +0800
author: fungleo
preview: "linux|mac日常入门命令行使用——搜索文件|文件夹搜索文件或者文件夹，是一个常见的需求。我们可以用多种命令来实现我们的需求。find命令实现搜索find是英文，寻找的意思。这个命令可以很方面的来搜索我们需要的内容。标准命令如下：find./-iname'*.txt'命令搜索的目录参数关键词-iname是不区分大小写。如果要区分大小写的话-name即可。一般情况下，我们搜"
tags: ["linux", "mac", "搜索", "find", "grep"]
categories:
    - Linux\CentOS
---

# linux\mac 日常入门命令行使用——搜索文件\文件夹

搜索文件或者文件夹，是一个常见的需求。我们可以用多种命令来实现我们的需求。

## find 命令实现搜索

`find` 是英文，寻找的意思。这个命令可以很方面的来搜索我们需要的内容。

标准命令如下：

```
find ./ -iname "*.txt"
```

命令 搜索的目录 参数 关键词

![find](http://img.blog.csdn.net/20171109143227657?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

`-iname` 是不区分大小写。如果要区分大小写的话 `-name` 即可。一般情况下，我们搜索内容都是不区分大小写的。

关键词可以用 `*` 号进行通配。事实上，也支持正则表达式。不过我估计你可能不熟悉正则表达式，所以不强求了。

这是标准用法。但是我下面再推荐一个我喜欢的组合命令的用法

## find + grep 搜索

默认的 `find` 命令，功能及其强大，并且最基础的也需要知道一个 `*` 这样的通配符。但是通过这个组合命令，可以让你啥都不懂的进行任意的搜索。

我们知道 `find ./` 命令，可以把当前文件夹下的所有内容全部列出来。同时 `grep` 命令可以根据关键词进行过滤。然后我们就可以组合这个命令了。

```
find ./ | grep txt
```

这个命令就可以将当前目录里面的所有文件名中包含 `txt` 的全部列出来。

![find+grep](http://img.blog.csdn.net/20171109143357071?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

另外，我们还可以组合多个关键词进行进一步的过滤，只要在后面接着输入 `| grep 关键词`即可。

最重要的是，还可以取反，就是 `grep` 加上 `-v` 这个参数。

举例如下：

```
find ./ | grep txt | grep Site
find ./ | grep txt | grep Site | grep -v linux
```

![find+grep2](http://img.blog.csdn.net/20171109143719023?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

看，重要我们就可以不用管什么正则，什么通配符，用我们简单的组合命令，就可以进行我们想要的任意搜索了。

> `|` 是管道的意思。作用是把前面的命令的结果传给后面的命令继续去执行。这是命令行中非常重要并且非常好用的概念。我们可以用这些来进行很多的组合操作。

对了，写完了才想起来，我们用不着用 `find ./` 作为第一个命令，还可以用 `find .` 作为命令。效果是一样的。嘿嘿。

本文由 FungLeo 原创，允许转载，但转载必须保留首发链接。

