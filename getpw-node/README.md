# 密码生成以及管理工具

## 使用说明

1. 将代码 clone 到本地，并 npm i 安装依赖

2. 创建 `~/.bin` 目录

3. 在 `~/.zshrc` (zsh 环境) 或 `~/.bash_profile` (bash 环境) 中添加以下代码

```
PATH=${PATH}:/Users/{替换为你的电脑用户名}/.bin
```

4. 执行 `. ~/.zshrc` 或 `. ~/.bash_profile` 使配置生效

6. 在 `~/.bin` 目录中创建软连接

```
ln -s  {替换为你存储代码的路径}/getpw-node/bin/index.js getpw
ln -s  {替换为你存储代码的路径}/getpw-node/bin/seepw.js seepw
```

7. 将 `db` 目录下的 `passwd-default.db` 重命名为 `passwd.db`

8. 执行 `getpw -h` 或 `seepw -h` 查看相应使用帮助
