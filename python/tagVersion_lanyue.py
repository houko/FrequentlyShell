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
 Date: 18/1/31 14:53
 Description: 更新蓝月传奇线上版本
 Copyright(©) 2017 by xiaomo.
"""

import os
import shutil
import sys

versionBasePath = "/data/game/server/miracle-version"
jarBasePath = "/data/game/server/miracle-server"
dataBasePath = "/data/game/server/miracle-data"


# 检查是否正确
def check_param():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python tagVersion_lanyue.py version")
        exit(1)
    else:
        print("开始执行脚本:'" + sys.argv[0] + "', 版本号为:")
        for i in range(1, len(sys.argv)):
            print(sys.argv[i], end=' ')


# 创建文件夹
def create_dir():
    print("开始创建文件夹")
    os.chdir(versionBasePath)
    version = sys.argv[1]
    if os.path.exists(version):
        print("文件夹己存在")
        exit(1)
    else:
        os.makedirs(version, 0o700, False)
        os.chdir(version)
        os.makedirs("server", 0o700, True)
        os.chdir("server")
        os.makedirs("core", 0o700, True)
        os.chdir("core")
        os.makedirs(version, 0o700, True)
        os.chdir(version)


# 编译jar包
def compile_jar():
    os.chdir(jarBasePath)
    os.system("git checkout master")
    os.system("mvn clean package")


# 拷贝Jar包
def copy_jar():
    version = sys.argv[1]
    print("版本为 %s" % version)

    # 拷贝game包
    game_server_url = jarBasePath + "/game-codex/target/game-server-0.0.1.jar"
    game_file_list = os.listdir(game_server_url)
    for file in game_file_list:
        shutil.copy(file, versionBasePath + version + "/server/core/" + version)

    # 拷贝 api包
    game_api_url = jarBasePath + "/game-api/target/game-api-0.0.1.jar"
    api_file_list = os.listdir(game_api_url)
    for file in api_file_list:
        shutil.copy(file, versionBasePath + version + "/server/core/" + version)


# 拷贝jqr包
def copy_data():
    version = sys.argv[1]
    os.chdir(dataBasePath)
    os.system("git pull")
    target = versionBasePath + version + "/server/data"
    shutil.copytree(dataBasePath, target)
    os.chdir(target)
    os.system("rm -rf .git")


# 执行
def main():
    check_param()
    compile_jar()
    create_dir()
    copy_jar()
    copy_data()
    print("\n脚本执行完毕")


if __name__ == '__main__':
    main()
