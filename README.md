![BlessWall-Python](https://socialify.git.ci/QNquenan/BlessWall-Python/image?description=1&font=JetBrains+Mono&forks=1&issues=1&language=1&name=1&owner=1&pattern=Brick+Wall&pulls=1&stargazers=1&theme=Light)

# BlessWall-Python 祝福墙

这是一个用 Python 和 Tkinter 编写的简单祝福墙应用程序，会在屏幕上随机显示各种温馨祝福语的小窗口。

## 安装和运行

### 方法一：直接运行源码

1. 克隆或下载此仓库
2. 确保已安装 Python 3.x
3. 运行程序：
   ```
   python main.py
   ```

### 方法二：使用打包的可执行文件

1. 克隆或下载此仓库
2. 进入 `dist` 目录
3. 双击运行 `main.exe`

## 打包

如果你想自己打包程序，可以使用 PyInstaller：

1. 安装 PyInstaller：
   ```
   pip install pyinstaller
   ```

2. 使用以下命令打包：
   ```
   pyinstaller --add-data "Blessing.json;." --windowed main.py
   ```

或者使用现有的 spec 文件：
   ```
   pyinstaller main.spec
   ```

## 自定义祝福语

所有的祝福语都存储在 [Blessing.json](https://github.com/QNquenan/BlessWall-Python/blob/master/Blessing.json) 文件中。你可以编辑这个文件来添加、删除或修改祝福语。每条祝福语应为一个字符串，整个文件是一个包含所有祝福语的 JSON 数组。

## 代码说明

- [main.py](https://github.com/QNquenan/BlessWall-Python/blob/master/main.py)：主程序文件，包含所有功能逻辑
- [Blessing.json](https://github.com/QNquenan/BlessWall-Python/blob/master/Blessing.json)：包含所有祝福语的 JSON 文件
- [main.spec](https://github.com/QNquenan/BlessWall-Python/blob/master/main.spec)：PyInstaller 的配置文件

## 许可证

该项目基于 MIT 许可证发布。