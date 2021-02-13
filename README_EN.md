# server tag
*server tag is tag for server plugin on iterm2.*

![GitHub](https://img.shields.io/github/license/shawn-bluce/server_tag)
![GitHub top language](https://img.shields.io/github/languages/top/shawn-bluce/server_tag)
![GitHub repo size](https://img.shields.io/github/repo-size/shawn-bluce/server_tag)

## function
Color your tab and show server name on your iterm, when you ssh to server.

## show
[![ScreenShot](https://raw.githubusercontent.com/shawn-bluce/pics_home/master/20200822140557.png)](https://www.bilibili.com/video/BV1r64y1c7su/)

## quick start
1. check your python and pip using python3. **only support Python 3.** `python3 --version && pip3 --version`
2. install iterm2 library with python, `pip3 install iterm2 --user`
3. clone this project to your workspace
4. use `install.sh` to install. you can manual install if this script is not work.

## manual install
1. check your python and pip using python3. **only support Python 3.** `python3 --version && pip3 --version`
2. install iterm2 library with python, `pip3 install iterm2 --user`
3. clone this project to your workspace
4. edit .zshrc or .bashrc, add `alias ssh="xxx/server_tag/server_tag.py"`
5. edit .zshrc or .bashrc, add source `alias _ssh="/usr/bin/ssh"`(optional)
6. restart iterm2, test and check result for `ssh user@host`

## manage server
Edit `server_config.json`. Outermost is server group, all server in same group use same color.

## color
You can get RGB color on [https://www.w3schools.com/colors/colors_rgb.asp](https://www.w3schools.com/colors/colors_rgb.asp).
