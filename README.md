# Commentbox

一个可以实现工厂智能化管理的系统

1、生产系统：（1）项目计划
             （2）今日生产安排
			 （3）生产报表（生产实时数据、生产过程曲线）
2、设备检修	（1）检修日记
			（2）检修工单
			（3）故障数据记录

3、系统用户管理	（1）专业人员
				（2）生产主管
				（3）监工账号

### 使用技术

1. 后端： Flask + Mongoengine + Mako + requests + Redis + lxml + concurrent.futures

2. 前端：React + Mobx + Fetch + Material-UI + ES6 + Webpack + Babel

### Getting Started

#### 虚拟环境和安装应用依赖

```
❯ git clone https://github.com/dongweiming/commentbox
❯ cd commentbox
❯ virtualenv venv
❯ source venv/bin/activate
❯ pip install -r requirements.txt
❯ cp local_settings.py.tmpl local_settings.py  # 然后修改其中的配置(如Redis，MongoDB)
```

#### 爬虫篇

1. 抓取之前可以添加一些代理地址到local_settings.py中，否则会影响爬取速度。
2. 修改run.py中max_workers的数量，建议选择服务器CPU核数作为这个值。 然后启动`python run.py`就开始抓取了。

#### 前端开发篇

先安装：

```
❯ cd assets
❯ npm install  # 推荐使用cnpm, 要不然有点慢
```

开发：

开发时可以先修改server.js里面的主机和端口号，然后启动

```
❯ make dev
```

目前默认后端使用8100端口，开发模式使用3000端口。

部署：

```
 ❯ make build
```

执行完毕就会在生成新的static/js/dist/index.bundle.js*文件了。

Enjoy it!
