---
title: "javascript 判断参数是否为非0整数数字或者整数数字字符串的简单方法（小装逼）"
date: 2018-04-26 17:33:33 +0800
lastmod: 2018-04-26 17:33:33 +0800
author: fungleo
preview: "javascript判断参数是否为非0整数数字或者整数数字字符串的简单方法（小装逼）我们来判断一个值是否为数字，可以把它转化为数字，看是否为NaN然后，再判断是否等于0即可简单的来实现判断了。所以，代码如下(num)=&amp;gt;{if(!isNaN(parseInt(num))){if(num!==0){//dosomething..."
tags: ["javascript", "NaN", "isNaN", "判断是否为数字"]
categories:
    - JavaScript
---

#javascript 判断参数是否为非0整数数字或者整数数字字符串的简单方法（小装逼）

我们来判断一个值是否为数字，可以把它转化为数字，看是否为`NaN` 然后，再判断是否等于0即可简单的来实现判断了。

所以，代码如下

```js
(num) => {
  if (!isNaN(parseInt(num))){
    if (num !== 0) {
      // do something
    }
  }
}
```

逻辑非常清楚。但是有点冗余。其实 `isNaN` 对于非数字的输出都是 `true` ，所以，代码可以修改为：

```js
(num) => {
  if (!isNaN(num)){
    if (num !== 0) {
      // do something
    }
  }
}
```

好一点，但是两层判断，感觉恶心。所以继续优化

```js
(num) => {
  if (!isNaN(num) && parseInt(num) !== 0){
    // do something
  }
}
```

去掉一层循环，好了很多。但是这个代码还是感觉恶心。能不能再优化一下呢？

```js
(num) => {
  if (!!+num) {
    // do something
  }
}
```

看不懂了，得解释以下， `+` 可以把任何东西变成 数字或者 `NaN` ，而如果值等于0，转化为布尔值也是为`false`，所以，判断可以合并为 `!!+num` 即可。

看上去不错，换个思路，既然 0 是`false` 那么我们能不能把所有的非数字或者数字字符串的内容变成 0 呢？代码出炉：

```js
(num) => {
  if (~~num) {
    // do something
  }
}
```

这里用了两个字符，比上面的三个字符更加精简了。我们能不能用一个字符来实现呢？可以。判断条件是可以自动转化为布尔值的。所以，上上个例子中的 `!!`是多余的。

```js
(num) => {
  if (+num) {
    // do something
  }
}
```

> 请谨慎在项目中使用这样的代码，挨打不要找我。

本文由FungLeo原创，允许转载，但转载必须附带首发链接。