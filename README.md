# 1. update9998.sh
该脚本的作用是将上传的新版本zip包解压并更新到服务器中 。9998是我们的外网服务器,以前更版本总要是手动去操作，不熟悉的话要10分钟甚至更久，熟悉的人至少也得花3分钟。而我花了半个小时写了这个脚本，更新版本只需要1分钟，甚至更少。

# 2. updateSever.sh
该脚本的作用将内网更新的svn代码编译释出为jar包,然后并更新服务器。以前的情景是策划只能在老版本测，有新功能做完之后需要程序手动更新代码并通知测试。过程极其繁琐，而且更新频率特别高。因此萌生了做工具的想法。最初是使用jenkins做的自动部署,后来觉得用jenkins太小题大作了 。在CTO的建议下采用了shell脚本的方式写这个工具 。
![image](https://cloud.githubusercontent.com/assets/12625278/25697071/2ab56e4c-30ec-11e7-8354-5599e79659ef.png)

```

   1 At revision 38773.
   2 服务器地址：127.0.0.1，端口：8003
   3 开始连接服务器....
   4 发送关服请求....
   5 断开所有连接....
   6 关闭登录线程....
   7 关闭场景事件派发线程....
   8 等待所有场景中的命令执行完毕....
   9 关闭场景公共驱动线程....
  10 关闭封魔谷驱动线程....
  11 关闭边境小村驱动线程....
  12 关闭业务逻辑线程....
  13 关闭数据保存线程(保存服务器缓存数据)....
  14 保存排行榜缓存数据....
  15 保存邮件数据....
  16 关闭延迟入库线程(保存未入库的数据)....
  17 关闭Grizzly网络监听....
  18 关服逻辑处理完毕...
  19 服务器已关闭...
  20 游戏服务器停止  [ ^[[1;32;1m ok ^[[0m ]
  21 日志服进程ID: 4920,JAR路劲: /data/game/s1/server/core/1.0.1.0/LoggerServer.jar
  22 日志服务器停止  [ ^[[1;32;1m ok ^[[0m ]
  23 Buildfile: /data/game/s1/dev_control/servercode/release/build.xml
  24
  25 clean:
  26      [echo] 初始化项目编译...
  27     [mkdir] Created dir: /data/game/s1/dev_control/servercode/release/class/MainServer/classes
  28     [mkdir] Created dir: /data/game/s1/dev_control/servercode/release/class/LogServer/classes
  29     [mkdir] Created dir: /data/game/s1/dev_control/servercode/release/class/SecurityServer/classes
  30    [delete] Deleting directory /data/game/s1/dev_control/servercode/release/bin
  31     [mkdir] Created dir: /data/game/s1/dev_control/servercode/release/bin
  32    [delete] Deleting directory /data/game/s1/dev_control/servercode/release/lib
  33     [mkdir] Created dir: /data/game/s1/dev_control/servercode/release/lib
  34
  35 copyLib:
  36      [copy] Copying 27 files to /data/game/s1/dev_control/servercode/release/lib
  37
  38 CompileMainServer:
  39      [echo] 编译项目MainServer...
PackageLogServer:
      [jar] Building jar: /data/game/s1/dev_control/servercode/release/bin/LoggerServer.jar

CompileSecurityServer:
     [echo] 编译项目SecurityServer...
    [javac] Warning: rpg/security/SecurityServerLinux.java modified in the future.
    [javac] Warning: rpg/security/SecurityServerWin.java modified in the future.
    [javac] Warning: rpg/security/SecurtyFilter.java modified in the future.
    [javac] Compiling 3 source files to /data/game/s1/dev_control/servercode/release/class/SecurityServer/classes

PackageSecurityServer:
      [jar] Building jar: /data/game/s1/dev_control/servercode/release/bin/SecuityServer.jar

cleanFile:
   [delete] Deleting directory /data/game/s1/dev_control/servercode/release/class

release:
     [echo] 释出成功

BUILD SUCCESSFUL
Total time: 8 seconds
游戏服务器启动	[  ok  ]
```


# 3. tagVersion.sh
花了一小时写脚本,2小时测脚本。以后打版本我就不用敲一大堆命令了，这种一劳永逸的事情我最喜欢干了。该脚本的作用就是根据既定要求创建对应的目录结构，然后更新编译生成最新的服务器jar包和配置文件并拷贝到对应的目录等待确认上传交由运维更新游戏版本 。能做的事情也就只有这些啦,哈哈

执行效果如下


```
└── server
    ├── core
    │   └── 1.0.564823.1
    │       ├── LoggerServer.jar
    │       ├── MainServer.jar
    │       └── SecuityServer.jar
    └── data
        ├── gamecfg.dat
        ├── map
        ├── minimap
        ├── sys_store.xlsx
        └── version.dat
```


```
版本号根目录不存在,现在开始创建版本号根目录-------> 0.0 ,(服务端和客户端谁先截版谁先建根目录版本号,版本号为1.0.x.y,x为最终提交的svn版本号,y为截版更新次数)
开始创建server目录
开始创建core目录
开始创建jar目录 0.0
Buildfile: /Users/xiaomo/IdeaProjects/MIR/server/release/build.xml

clean:
     [echo] 初始化项目编译...
    [mkdir] Created dir: /Users/xiaomo/IdeaProjects/MIR/server/release/class/MainServer/classes
    [mkdir] Created dir: /Users/xiaomo/IdeaProjects/MIR/server/release/class/LogServer/classes
    [mkdir] Created dir: /Users/xiaomo/IdeaProjects/MIR/server/release/class/SecurityServer/classes
   [delete] Deleting directory /Users/xiaomo/IdeaProjects/MIR/server/release/bin
    [mkdir] Created dir: /Users/xiaomo/IdeaProjects/MIR/server/release/bin
   [delete] Deleting directory /Users/xiaomo/IdeaProjects/MIR/server/release/lib
    [mkdir] Created dir: /Users/xiaomo/IdeaProjects/MIR/server/release/lib

copyLib:
     [copy] Copying 27 files to /Users/xiaomo/IdeaProjects/MIR/server/release/lib

CompileMainServer:
     [echo] 编译项目MainServer...
    [javac] Warning: rpg/configdata/model/ItemGroup.java modified in the future.
    [javac] Compiling 2769 source files to /Users/xiaomo/IdeaProjects/MIR/server/release/class/MainServer/classes
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:163: 警告: [deprecation] Date中的setHours(int)已过时
    [javac] 				date1.setHours(0);
    [javac] 				     ^
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:164: 警告: [deprecation] Date中的setMinutes(int)已过时
    [javac] 				date1.setMinutes(0);
    [javac] 				     ^
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:165: 警告: [deprecation] Date中的setSeconds(int)已过时
    [javac] 				date1.setSeconds(0);
    [javac] 				     ^
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:169: 警告: [deprecation] Date中的setHours(int)已过时
    [javac] 				date.setHours(0);
    [javac] 				    ^
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:170: 警告: [deprecation] Date中的setMinutes(int)已过时
    [javac] 				date.setMinutes(0);
    [javac] 				    ^
    [javac] /Users/xiaomo/IdeaProjects/MIR/server/MainServer/src/rpg/system/onlinebox/OnlineManager.java:171: 警告: [deprecation] Date中的setSeconds(int)已过时
    [javac] 				date.setSeconds(0);
    [javac] 				    ^
    [javac] 注: 某些输入文件使用了未经检查或不安全的操作。
    [javac] 注: 有关详细信息, 请使用 -Xlint:unchecked 重新编译。
    [javac] 6 个警告

PackageMainServer:
      [jar] Building jar: /Users/xiaomo/IdeaProjects/MIR/server/release/bin/MainServer.jar

CompileLogServer:
     [echo] 编译项目MainServer...
    [javac] Compiling 152 source files to /Users/xiaomo/IdeaProjects/MIR/server/release/class/LogServer/classes
    [javac] 注: /Users/xiaomo/IdeaProjects/MIR/server/LogServer/src/rpg/gmhttp/GameInfoUtil.java使用了未经检查或不安全的操作。
    [javac] 注: 有关详细信息, 请使用 -Xlint:unchecked 重新编译。

PackageLogServer:
      [jar] Building jar: /Users/xiaomo/IdeaProjects/MIR/server/release/bin/LoggerServer.jar

CompileSecurityServer:
     [echo] 编译项目SecurityServer...
    [javac] Compiling 3 source files to /Users/xiaomo/IdeaProjects/MIR/server/release/class/SecurityServer/classes

PackageSecurityServer:
      [jar] Building jar: /Users/xiaomo/IdeaProjects/MIR/server/release/bin/SecuityServer.jar

cleanFile:
   [delete] Deleting directory /Users/xiaomo/IdeaProjects/MIR/server/release/class

release:
     [echo] 释出成功

BUILD SUCCESSFUL
Total time: 15 seconds
 开始拷贝jar包到指定目录
开始创建data目录
Updating '.':
At revision 38773.
开始拉取最新data配置
开始拷贝data配置到version目录
所有任务执行完毕

```