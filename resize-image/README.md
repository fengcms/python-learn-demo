# 图片重新设置大小的脚本

我们经常会收到大量的图片需要处理，最常处理的是图片的等比例缩放，缩放到一定的规格，用于网站的产品展示等部分。一般情况下，我都是使用 photoshop 来进行批量处理。当然，也会有 isee 之类的比较简单好用的软件来进行处理。只是 ps 来处理的时候比较繁琐，而 isee 这款软件是 windows 平台的，所以呢，还是不方便。

因此，我想用 Python 来实现这个功能，更加方便我们的日常的工作。

好，我写出来了。实际使用效果如下：

## 脚本帮助信息

```#
$ py reimg.py -h
usage: reimg.py [-h] [-v] [-q QUALITY] size sourceDir [targetDir]

Reduce the picture in the source directory and save it to the target directory
based on the longest side parameters

positional arguments:
  size                  The max width or max height of a picture
  sourceDir             Source directory
  targetDir             Target directory

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -q QUALITY, --quality QUALITY
                        Save picture quality, default 60
```

`size` 是设置图片的最长边。必填的。然后就是设置图片的源目录，脚本会自动处理源目录里的所有图片。目标目录为选填，如果不填写的话，则会输出到源目录中覆盖原有的图片。为了避免误操作，需要确认一下，如下演示：

```#
$ py reimg.py 400 image
Warning: If the target directory isn't set, the processing results will cover the picture in the source directory
Whether to Continue(Y/n)
Confirm:n
```

直接回车的话，就会继续处理了。

`QUALITY` 是设置图片的保存质量，默认为60。一般情况下，保持默认即可，除非有特殊要求。

总得来说，这个脚本还是非常实用的。
