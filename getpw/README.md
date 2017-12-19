# CLI 版密码生成与管理器脚本的说明

## 脚本概要

**脚本结构**

```#
├── README.md       说明文档
├── db.py           数据库驱动脚本，不单独提供功能
├── getpw.py        生成密码脚本
├── passwd.db       sqlite 数据库文件，如果不存在，则保存密码时会自动创建
└── seepw.py        查看和删除密码脚本
```

**实现功能**

1. `getpw.py` 根据设定的长度和密码复杂级别，生成符合要求的密码
    1. `-s/--simple` 简单级别的密码，由纯数字构成
    2. `-c/--commonly` 一般级别的密码，由数字与大小写字母构成(默认)
    3. `-d/--difficult` 复杂密码，由数字与大小写字母加上英文标点符号构成
    4. 指定长度为数字参数，默认为8位长度。
    5. `-n NAME` 该参数是为密码取一个名字，并且保存进数据库。支持中文。
2. `seepw.py` 为查看和删除密码的脚本
    1. `-d ID` 为删除指定 ID 的密码，ID 必须是数字。
    2. `-i ID` 为根据 ID 查看对应的密码的信息
    3. `-n NAME` 为根据保存时填写的名字来查询相应的密码，模糊查询。

两个脚本文件均可以使用 `-h` 参数来查看详细的帮助信息。

## 使用演示

### 生成密码的使用

生成一个普通的8位的密码

```#
$ python3 getpw.py
New password:	Fege2428
Tip: The password has been copied to the clipboard
```

>生成密码后，会自动复制到剪切板

生成一个6位的数字密码

```#
$ python3 getpw.py -s 6
New password:	384596
Tip: The password has been copied to the clipboard
```

生成一个12位的复杂的密码

```#
$ python3 getpw.py -d 12
New password:	9r+diD:,@q:b
Tip: The password has been copied to the clipboard
```

生成一个12位的复杂的密码,并保存到数据库

```#
$ python3 getpw.py -d 12 -n myPassword
New password:   n-6=+:y/RbqT
Tip: The password has been copied to the clipboard
And the password has been saved in data base
```

查看帮助信息

```#
$ python3 getpw.py -h
usage: getpw.py [-h] [-v] [-n NAME] [-s | -c | -d] [length]

This program is used to generate simple or complex passwords

positional arguments:
  length                The length of the password (Default 8)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -n NAME, --name NAME  Take a name for your password and Write it in data
                        base
  -s, --simple          The password is made up of pure numbers
  -c, --commonly        The password is made up of numbers and letters
                        (Default)
  -d, --difficult       The password is made up of numbers, letters, and
                        punctuation
```

### 管理密码的使用

查看所有的密码

```#
$ python3 seepw.py
+----+------------+--------------+---------------------+
| id | name       |   password   |         time        |
+----+------------+--------------+---------------------+
| 3  | love       |   N727726i   | 2017-12-19 10:14:53 |
| 32 | myPassword | icwpe3X/Ps:k | 2017-12-19 15:53:08 |
| 33 | myPassword | n-6=+:y/RbqT | 2017-12-19 15:55:19 |
+----+------------+--------------+---------------------+
```

查看名字中包含 `my` 的密码

```#
$ python3 seepw.py -n my
+----+------------+--------------+---------------------+
| id | name       |   password   |         time        |
+----+------------+--------------+---------------------+
| 32 | myPassword | icwpe3X/Ps:k | 2017-12-19 15:53:08 |
| 33 | myPassword | n-6=+:y/RbqT | 2017-12-19 15:55:19 |
+----+------------+--------------+---------------------+
```
查看ID为 32 的密码

```#
$ python3 seepw.py -i 32
+----+------------+--------------+---------------------+
| id | name       |   password   |         time        |
+----+------------+--------------+---------------------+
| 32 | myPassword | icwpe3X/Ps:k | 2017-12-19 15:53:08 |
+----+------------+--------------+---------------------+
```

如果数据库中的所有结果都不符合查找的条件

```#
$ python3 seepw.py -i 50
Info: record is empty
```

删除 ID 为 32 的密码

```#
$ python3 seepw.py -d 32
Success: ID 32 password has been deleted
```

如果删除的 ID 数据库中不存在

```#
$ python3 seepw.py -d 50
Failure: the password was not found
```

查看管理密码的帮助

```#
usage: seepw.py [-h] [-v] [-i ID | -n NAME | -d DELETE]

This program is used to manage the password saved in the database

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i ID, --id ID        The ID of the password you want to look at
  -n NAME, --name NAME  The NAME of the password you want to look at
  -d DELETE, --delete DELETE
                        Delete mode, the parameter is ID
```

> 程序有使用一些需要安装的库，如果报错，请按照提示安装对应的库即可。
> 本程序为开源程序，仅供大家参考学习，禁止用于商业用途。
