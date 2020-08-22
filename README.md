
# server tag
*server tag 是一个给服务器打标签的 iterm2 插件*

**[English README.md](https://github.com/shawn-bluce/server_tag/blob/master/README_EN.md)**

## 功能
我们经常要登录到各种不同的服务器上，有些是自己个人的、有些是公司的测试环境、有些是公司的生产环境、有些又是开发环境等等。。。。当你使用的服务器多起来的时候就几乎不可避免的迷失在多个服务器之间，terminal 开了好多却分不清哪个是哪个，一不小心来了一手 `rm -rf` 当场人就没了。这个插件就是帮你实时的标记出当前操作的 tab 具体是连接到了哪台服务器上。

## 效果展示
这里可以看到 4 个 tab 分别有不同的颜色。具体的颜色和 terminal 右上角的内容（badge）都是可以自定义的，每一组服务器配置一个颜色，每一个 ip 配置一个badge。

图片可以点，是一段视频演示效果
[![ScreenShot](https://raw.githubusercontent.com/shawn-bluce/pics_home/master/20200822140557.png)](https://www.bilibili.com/video/BV1r64y1c7su/)

## 开始使用
1. 检查 Python 版本和 pip 版本，该插件仅支持 Python3. 可以使用 `python3 --version && pip --version` 来检查版本
2. 安装 `iterm2` 的官方库，使用 `pip3 install iterm2 --user`
3. 克隆项目到本地，例如`/Users/shawn/Workstadion/server_tag/`
4. 按需编辑你的`.bashrc`或者`.zshrc`（看你用的是哪个 shell），添加`alias ssh="xxx/server_tag/server_tag.py"`
5. 如果想要保留原始的 ssh 命令，可以在上面的 alias 下添加`alias _ssh="/usr/bin/ssh"` （以后使用原始 ssh 就用 \_sshi 替代了）
6. 生成配置文件 `python3 generate_config.py`
7. 重启你的 iterm2， 然后尝试使用 ssh 登录一台服务器试试看🎉

## 管理服务器
服务器的配置是项目目录的`server_config.json`文件，如果没有则使用`python3 generate_config.py`创建。大家都是程序员，这里就不过多解释文件格式的问题了。

## 配置文件
* json 文件最外层的是一组组的数据，就比如默认生成的配置文件里的 product 和 testing
* 每一组服务器下的 color 就是指的 tab 和 badge 的颜色
* 每一组服务器下的server 下层是一个个的服务器
* 因为同功能的服务器可能有多台，所以一个名字下可以配置多个 ip

## 颜色
可以在这个地址方便的找到并生成需要的 RGB 颜色值：[https://www.w3schools.com/colors/colors_rgb.asp](https://www.w3schools.com/colors/colors_rgb.asp)。

