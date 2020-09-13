### flask-web

------


【娱乐项目】

初衷：自动获得每天更新的番或者剧

【使用】
1. export FLASK_ENV=development
2. export FLASK_APP=manage.py
3. flask run --host 0.0.0.0 --no-reload (no-reload参数可以 解决Flask-SocketIO引起的signal only works in main thread问题)

#### 豆瓣源
```
https://pypi.douban.com/simple/

```

#### 更新ubuntu源
- 1. 备份
```
cp /etc/apt/sources.list sources.list.bck
```

- 2. 查看操作系统版本
```
cat /etc/lsb-release
```

- 3. 去[镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)中选择对应版本的镜像，并替换原有sources.list
```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
```

#### celery以及beat启动
- celery worker -l INFO -c 5 -A manage.celery
- celery worker -l INFO -c 5 -A manage.celery --beat

#### 安装pandoc
- 1. 安装Haskell平台
```
sudo apt-get install haskell-platform
```
- 2. 安装pandoc
```
cabal update              #获取Haskell包信息
cabal install pandoc      #通过cabal安装pandoc
(或cabal install pandoc --force-reinstalls )
```

#### [另一种安装pandoc方式](https://zhaozhiyuan.org/post/install-pandoc/)
- 1. 下载安装包并安装
```
wget https://github.com/jgm/pandoc/releases/download/2.10.1/pandoc-2.10.1-linux-amd64.tar.gz && sudo tar xvzf pandoc-2.10.1-linux-amd64.tar.gz --strip-components 1 -C /usr
```

- 2. 安装依赖
```
pip install pandocfilters
```

- 3. 安装texlive
```
sudo apt-get install texlive-full
```

| etst | asda|
| --- | --- |
| da| zh中文|
