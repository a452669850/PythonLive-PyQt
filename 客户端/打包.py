# coding:utf-8
from __future__ import unicode_literals
# 将当前的pycode转化为exe，需安装PyQt， pyinstaller
import os
import os.path

# Ui文件所在路径
dir = './'


def code2exe(pyfile):
    # -F 打包为单独的exe文件； -w 使用窗口显示； -D 生成目录
    cmd = 'pyinstaller -F -w -D {pyfile}'.format(pyfile=pyfile)
    os.system(cmd)

if __name__ == "__main__":
    code2exe('login_interface.py')
