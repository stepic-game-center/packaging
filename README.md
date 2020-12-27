# STEPIC打包安装程序指南

## 一 打包EXE

首先下载Stepic前端文件

```shell
$ git clone https://github.com/stepic-game-center/Stepic.git
```

### 初始化

打开Stepic文件夹：

删除：删除.git文件夹，删除.idea文件夹，删除windows/\__pycache__文件夹，删除windows下所有ui文件。

清空：清空config文件夹，清空game文件夹，清空image/game文件夹。

新增：config文件夹下新增.init空白文件，game文件夹下新增.init空白文件，image/game文件夹下新增.init空白文件。

### 对于用户程序

stepic-user下，service文件夹下保留UserMainService.py，windows文件夹下保留User*.py文件。

删除其他文件。

UserMainService.py重命名为stepic.pyw。

把favicon.ico放在stepic-user/service 文件夹下。

打开stepic.pyw，编辑，添加以下代码：

```python
# 为游戏做准备
import pygame
from PyQt5.QtWebEngineWidgets import *
```

目的是为了将pygame库打包进软件，以便于运行pygame库支持的游戏。

stepic-user/service 文件夹下shift+右键此处打开powershell：

```powershell
PS > pyinstaller -F -i .\favicon.ico stepic.pyw
```

打包完成后将service/dist 文件夹下的stepic.exe 移动到 service 文件夹下。

### 对于开发者和管理员

stepic-admin下，service文件夹下保留AdminMainService.py，windows文件夹下保留Admin\*.py文件和Developer*.py文件。

删除其他文件。

AdminMainService.py重命名为stepic-admin.pyw。

把favicon.ico放在stepic-admin/service 文件夹下。

打开stepic-admin.pyw，编辑，添加以下代码：

```python
from PyQt5.QtWebEngineWidgets import *
```

stepic-admin/service 文件夹下shift+右键此处打开powershell：

```powershell
PS > pyinstaller -F -i .\favicon.ico stepic-admin.pyw
```

打包完成后将service/dist 文件夹下的stepic-admin.exe 移动到 service 文件夹下。

## 打包可执行安装文件

使用vs 插件操作