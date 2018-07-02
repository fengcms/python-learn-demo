---
title: "Vue2+VueRouter2+Webpack+Axios 构建项目实战2017重制版（三）认识项目所有文件"
date: 2017-08-25 18:58:45 +0800
lastmod: 2017-08-25 18:58:45 +0800
author: fungleo
preview: "Vue2+VueRouter2+Webpack+Axios构建项目实战2017重制版（三）认识项目所有文件在《Vue2+VueRouter2+Webpack+Axios构建项目实战2017重制版（二）安装nodejs环境以及vue-cli构建初始项目》中，我们通过安装nodejs系统环境，以及vue-cli脚手架工具，在执行完命令后，我们就已经将一个初始项目跑起来了。但是，我们的"
tags: ["vue", "vuerouter", "webpack", "axios", "vue文件说明"]
categories:
    - vuejs
---

# Vue2+VueRouter2+Webpack+Axios 构建项目实战2017重制版（三）认识项目所有文件

在《[Vue2+VueRouter2+Webpack+Axios 构建项目实战2017重制版（二）安装 nodejs 环境以及 vue-cli 构建初始项目](http://blog.csdn.net/fungleo/article/details/77584701)》中，我们通过安装 `nodejs` 系统环境，以及 `vue-cli` 脚手架工具，在执行完命令后，我们就已经将一个初始项目跑起来了。

但是，我们的项目代码，还一个都没有看到。因此，这个章节，我们来认识一下所有的文件。

## 初始文件解析

```#
├── README.md						// 项目说明文档
├── node_modules					// 项目依赖包文件夹
├── build							// 编译配置文件，一般不用管
│   ├── build.js
│   ├── check-versions.js
│   ├── dev-client.js
│   ├── dev-server.js
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   └── webpack.prod.conf.js
├── config							// 项目基本设置文件夹
│   ├── dev.env.js				// 开发配置文件
│   ├── index.js					// 配置主文件
│   └── prod.env.js				// 编译配置文件
├── index.html						// 项目入口文件
├── package-lock.json			// npm5 新增文件，优化性能
├── package.json					// 项目依赖包配置文件
├── src								// 我们的项目的源码编写文件
│   ├── App.vue					// APP入口文件
│   ├── assets						// 初始项目资源目录，回头删掉
│   │   └── logo.png
│   ├── components				// 组件目录
│   │   └── Hello.vue			// 测试组件，回头删除
│   ├── main.js					// 主配置文件
│   └── router						// 路由配置文件夹
│       └── index.js			// 路由配置文件
└── static							// 资源放置目录
```

好，如上，就是我们的 `vue` 初始化后得到的一个项目的完整结构。其他大多数文件我们是不用管的。如果要管的话，我在后面的章节也会去详细说明。

我们绝大多数的操作，就是在 `src` 这个目录下面。默认的 `src` 结构比较简单，我们需要重新整理。

另外 `static` 资源目录，我们也需要根据放置不同的资源，在这边构建不同的子文件夹。

## 我们来配置 src 目录

先不要管这些文件的内容，我们先建立这些空的文件在这边。然后我们后面去完善它。

我们的这个项目是要做两个页面，一个是 `cnodejs` 的列表页面，一个是详情页面。

所以，我把项目文件夹整理成如下的结构

```#
├── App.vue							// APP入口文件
├── api								// 接口调用工具文件夹
│   └── index.js					// 接口调用工具
├── components						// 组件文件夹，目前为空
├── config							// 项目配置文件夹
│   └── index.js					// 项目配置文件
├── frame							// 子路由文件夹
│   └── frame.vue					// 默认子路由文件
├── main.js							// 项目配置文件
├── page								// 我们的页面组件文件夹
│   ├── content.vue				// 准备些 cnodejs 的内容页面
│   └── index.vue					// 准备些 cnodejs 的列表页面
├── router							// 路由配置文件夹
│   └── index.js					// 路由配置文件
├── style							// scss 样式存放目录
│   ├── base						// 基础样式存放目录
│   │   ├── _base.scss			// 基础样式文件
│   │   ├── _color.scss		// 项目颜色配置变量文件
│   │   ├── _mixin.scss		// scss 混入文件
│   │   └── _reset.scss		// 浏览器初始化文件
│   ├── scss						// 页面样式文件夹
│   │   ├── _content.scss		// 内容页面样式文件
│   │   └── _index.scss		// 列表样式文件
│   └── style.scss				// 主样式文件
└── utils							// 常用工具文件夹
    └── index.js					// 常用工具文件
```

因为我们删除了一些默认的文件，所以这个时候项目一定是报错的，先不管他，我们根据我们的需求，新建如上的项目结构。这些都是在 `src` 目录里面的结构。

## 我们来配置 static 目录

这个目录比较简单，因为这个项目我们的资源不多，但是，为了我的这系列博文能够适合大多数的项目的开发，一般，我搞成下面这个样子：

```#
├── css				// 放一些第三方的样式文件
├── font				// 放字体图标文件
├── image			// 放图片文件，如果是复杂项目，可以在这里面再分门别类
└── js				// 放一些第三方的JS文件，如 jquery
```

你可能很奇怪，我们不是把样式和 `JS` 都写到里面去么，为什么还要在这边放呢？

因为，如果是放在 `src` 目录里面，则每次打包的时候，都需要打包的。这回增加我们的打包项目的时间长度。而且，一些地方放的文件，我们一般是不会去修改的，也没必要 `npm` 安装，直接引用就好了。你可以根据自己的情况，对这些可以不进行打包而直接引用的文件提炼出来，放在资源目录里面直接调用，这样会大大的提高我们的项目的打包效率。

好，就这么搞，我们的文件架构就搞好了，下一张，我们来开始写代码了。

> 如果文章由于我学识浅薄，导致您发现有严重谬误的地方，请一定在评论中指出，我会在第一时间修正我的博文，以避免误人子弟。

本文由 FungLeo 原创，允许转载，但转载必须保留首发链接。


