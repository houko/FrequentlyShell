#! /usr/bin/python3
# coding=utf-8

"""
 把今天最好的表现当作明天最新的起点．．～
 いま 最高の表現 として 明日最新の始発．．～
 Today the best performance  as tomorrow newest starter!
 author: xiaomo
 github: https://github.com/syoubaku
 email: xiaomo@xiamoo.info
 QQ_NO: 83387856
 Date: 17/5/31 14:53
 Description:
 Copyright(©) 2017 by xiaomo.
"""

import os


def close_server():
    os.system("sh /data/game/s1/dev_control/scripts/stopServer.sh")


def update_code():
    os.system("cd /data/game/s1/dev_control/servercode")
    os.system("svn up")


def compile_jar():
    os.system("cd /data/game/s1/dev_control/servercode/release")
    os.system("ant")


def copy_jar():
    os.system("cp -f /data/game/s1/dev_control/servercode/release/bin/* /data/game/s1/server/core/1.0.1.0")


def start_server():
    os.system("sh /data/game/s1/dev_control/scripts/startServer.sh")

    # 顺序执行  关服 更新 打包 开服
    update_code()
    close_server()
    compile_jar()
    start_server()


print("\n脚本执行完毕")
