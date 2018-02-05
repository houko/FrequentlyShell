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
 Description:
 Copyright(©) 2017 by xiaomo.
"""

import os
import shutil

import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python updateServer_lanyue.py version")
    exit(1)

# 开服/关服脚本
shell_path = "/data/game/server/s1/bin/"
# 目标根路径
target_base_url = "/data/game/server/s1/"
# 目标jar的路径
target_jar_path = target_base_url + "core/"
# 配置表根目录
target_data_base_path = target_base_url + "data/"
# 版本号
version = sys.argv[1]


# 关服
def close_server():
    os.system("cd" + shell_path)
    os.system("sh " + shell_path + " all stop")


# 拷贝文件
def update_code():
    # 处理jar包
    os.chdir(target_jar_path)
    os.system("rm -rf *.jar")
    os.chdir("/root/version/" + version + "/server/core/" + version)
    os.system("svn up")
    files = os.listdir(os.getcwd())
    for file in files:
        if file.endswith(".jar"):
            shutil.copy(file, target_jar_path)

    # 处理配置表
    os.chdir(target_base_url)
    os.system("rm -rf data")
    source_data_url = "/root/version/" + version + "/server/data"
    shutil.copytree(source_data_url, target_data_base_path)
    os.chdir(target_data_base_path)
    os.system("rm -rf .git")


# 修改版本号
def change_version():
    os.chdir(target_base_url)
    with open('version', 'w+', encoding='utf-8') as f:
        f.write(version)


def start_server():
    os.system("sh " + shell_path + " all stop")


def main():
    os.system("rm -rf " + version)
    print("---------------------------------关闭服务器---------------------------------")
    close_server()
    print("---------------------------------更新jar包---------------------------------")
    update_code()
    print("---------------------------------修改版本号---------------------------------")
    change_version()
    print("---------------------------------开启服务器---------------------------------")
    start_server()
    print("\n脚本执行完毕")


if __name__ == '__main__':
    main()
