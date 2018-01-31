#! /usr/bin/python3
# coding=utf-8

"""
 把今天最好的表现当作明天最新的起点．．～
 いま 最高の表現 として 明日最新の始発．．～
 Today the best performance  as tomorrow newest starter!
 Created by IntelliJ IDEA.
 author: xiaomo
 github: https://github.com/syoubaku
 email: xiaomo@xiamoo.info
 QQ_NO: 83387856
 Date: 17/5/31 14:53 
 Description: 梁山传奇打版本
 Copyright(©) 2017 by xiaomo.
"""

import os
import shutil
import sys

versionBasePath = "/Users/xiaomo/IdeaProjects/version"
jarBasePath = "/Users/xiaomo/IdeaProjects/MIR/server/release"
dataBasePath = "/Users/xiaomo/IdeaProjects/MIR/config/data"


# 检查是否正确
def check_param():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: tagVersion version")
        exit(1)
    else:
        print("开始执行脚本" + sys.argv[0] + "参数为:")

        for i in range(1, len(sys.argv)):
            print(i, end=' ')


def create_dir():
    print("\n开始创建文件夹")
    os.chdir(versionBasePath)
    version = sys.argv[1]
    if os.path.exists(version):
        print("文件夹己存在")
    else:
        os.makedirs(version, 0o700, False)
        os.chdir(version)
        os.makedirs("server", 0o700, True)
        os.chdir("server")
        os.makedirs("core", 0o700, True)
        os.chdir("core")
        os.makedirs(version, 0o700, True)
        os.chdir(version)


def compile_jar():
    os.chdir(jarBasePath)
    os.system("ant")


def copy_jar():
    version = sys.argv[1]
    file_list = os.listdir("bin")
    os.chdir("bin")
    for file in file_list:
        shutil.copy(file, "/Users/xiaomo/IdeaProjects/version/" + version + "/server/core/" + version)


def copy_data():
    version = sys.argv[1]
    os.chdir(dataBasePath)
    os.system("svn up")
    target = "/Users/xiaomo/IdeaProjects/version/" + version + "/server/data"
    shutil.copytree(dataBasePath, target)
    os.chdir(target)
    os.system("rm -rf .svn")


check_param()
create_dir()
compile_jar()
copy_jar()
copy_data()

print("\n脚本执行完毕")
