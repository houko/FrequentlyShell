#!/bin/bash

# 1. check the version param
if [ $# == 0 ]
    then
	echo "请输入版本号 格式为: sh update_lanyue.sh version"
	exit;
fi

# 2. close the server
cd /data/game/server/s1/bin
sh serverOptions.sh all stop
echo "1. 准备停服更新版本"


# 3. change the version file
echo $1 > /data/game/server/s1/version
echo "2. 写入版本号 $1 到version文件"

cd /root/version

if [ ! -d $1 ]; then
    echo "找不到资源目录: $1"
    exit
fi
rm -rf /data/game/s1/server/core/*
cp -r /$1/server/core/$1 /data/game/s1/server/core
echo "4. 开始拷贝jar文件"

# 5.copy data
rm -rf /data/game/s1/server/data
cp -r /root/version/$1/server/data /data/game/s1/server
echo "5. 开始拷贝data目录"

# 6. open the server
cd /data/game/s1/server/bin
sh serverOptions.sh all start
echo " 6. 所有文件准备就绪,准备开服......... "