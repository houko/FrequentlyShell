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


# 3. change the version file 
echo $1 > /data/game/s9998/server/version


# 4. unzip the zip
rm -rf __MACOSX
unzip /root/$1.zip
cd $1/server/core
cp -r /root/$1/server/core/$1 /data/game/s9998/server/core

# 5.copy data 
cd /data/game/s9998/server
rm -rf data
cd /root/$1/server
cp -r data /data/game/s9998/server

# 6. open the server
cd /data/game/s9998/server/bin
sh serverOptions.sh all start
