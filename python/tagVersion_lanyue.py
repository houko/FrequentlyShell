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
 Description: 更新蓝月传奇线上测试版本
 Copyright(©) 2017 by xiaomo.
"""

import os
import shutil
import sys

# 打版本根目录
versionBasePath = "/data/game/server/miracle-version/"
# 服务端代码根目录
serverBasePath = "/data/game/server/miracle-server/"
# 配置表根目录
dataBasePath = "/data/game/server/miracle-data/"
# 目标版本位置
run_base_url = "/data/game/server/s1/"

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python tagVersion_lanyue.py version")
    exit(1)

# 版本号
version_num = sys.argv[1]
# 目录版本的路径
target_version_url = (versionBasePath + version_num + "/server/core/" + version_num)
# 游戏包jar
game_server_url = serverBasePath + "game-codex/target/game-server-0.0.1.jar"
# api包jar
api_file_list = serverBasePath + "game-api/target/game-api-0.0.1.jar"


# 创建文件夹
def create_dir():
    os.chdir(versionBasePath)
    os.system("svn up")
    version = sys.argv[1]

    if os.path.exists(version):
        print("文件夹己存在")
    else:
        os.makedirs(version, 0o700, False)

    os.chdir(version)
    os.makedirs("libs", 0o700, True)
    os.makedirs("server", 0o700, True)
    os.chdir("server")
    os.makedirs("core", 0o700, True)
    os.chdir("core")
    os.makedirs(version, 0o700, True)
    os.chdir(version)


# 编译jar包
def compile_jar():
    os.chdir(serverBasePath)
    os.system("git checkout master")
    os.system("git pull")
    os.system("mvn clean package")


# 打tag
def tag_version():
    # 打服务端代码的tag
    os.chdir(serverBasePath)
    os.system("git tag -l | xargs git tag -d")
    os.system(" git tag " + version_num)
    os.system("git push --tags ")

    # 打配置表的tag
    os.chdir(dataBasePath)
    os.system("git tag -l | xargs git tag -d")
    os.system(" git tag " + version_num)
    os.system("git push --tags ")


# 拷贝Jar包
def copy_jar():
    print("版本为 %s" % version_num)
    # 拷贝game包
    shutil.copy(game_server_url, target_version_url)
    # 拷贝 api包
    shutil.copy(api_file_list, target_version_url)


# 拷贝jqr包
def copy_data():
    os.chdir(dataBasePath)
    os.system("git pull")
    target = versionBasePath + version_num + "/server/data"
    shutil.copytree(dataBasePath, target)
    os.chdir(target)
    os.system("rm -rf .git")


# 修改版本号
def change_version():
    os.chdir(run_base_url)
    with open('version', 'w', encoding='utf-8') as f:
        f.write(version_num)


def submit_svn():
    os.chdir(versionBasePath)
    os.system("svn up")
    os.system("svn st | grep '^\?' | tr '^\?' ' ' | sed 's/[ ]*//' | sed 's/[ ]/\\ /g' | xargs svn add ")
    os.system("svn commit -m " + version_num + " --force-log")


# 执行
def main():
    print("----------------开始执行脚本:'%s', 版本号为: %s -------------------" % (sys.argv[0], sys.argv[1]))
    print("----------------------编译jar包----------------------------------")
    compile_jar()
    print("----------------------打tag----------------------------------")
    tag_version()
    print("----------------------创建目录----------------------------------")
    create_dir()
    print("----------------------拷贝jar包---------------------------------")
    copy_jar()
    print("----------------------编译配置表----------------------------------")
    copy_data()
    print("----------------------修改版本号----------------------------------")
    change_version()
    print("----------------------提交svn代码----------------------------------")
    submit_svn()
    print("\n脚本执行完毕")


if __name__ == '__main__':
    main()
