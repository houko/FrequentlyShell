#!bin/sh

# 1. check the version param
if [ $# == 0 ]
    then 
	echo "请输入版本号 格式为: sh update9998.sh version"
	exit;
fi

# 2. close the server
cd /data/game/s9998/server/bin
sh serverOptions.sh all stop
echo "1. 准备停服更新版本"


# 3. change the version file 
echo $1 > /data/game/s9998/server/version
echo "2. 写入版本号 $1 到version文件"

# 4. unzip the zip
rm -rf __MACOSX
unzip /root/$1.zip
echo "3. 开始解压版本资源包......"
cd $1/server/core
cp -r /root/$1/server/core/$1 /data/game/s9998/server/core
echo "4. 开始拷贝jar文件"

# 5.copy data 
cd /data/game/s9998/server
rm -rf data
cd /root/$1/server
cp -r data /data/game/s9998/server
echo "5. 开始拷贝data目录"

# 6. open the server
cd /data/game/s9998/server/bin
sh serverOptions.sh all start
echo "6. 所有文件准备就绪,准备开服........."
