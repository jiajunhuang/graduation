网上订餐系统的设计与实现
=========================

介绍 & 安装
-------------

该系统要求能够在线餐饮信息浏览，在线订餐，
在线订单处理以及信息更新和删除等功能。

结构介绍:

- templates/: 属于MVC中的view

- controllers/: 属于MVC中的controller

- model/: 属于MVC中的model

运行方式:

- 安装python3,MySQL,redis

    - ArchLinux: sudo pacman -S python mariadb redis
    - Debian/Ubuntu: sudo apt-get install python3 mysql-server redis-server redis-cli
    - Centos: http://stackoverflow.com/questions/8087184/installing-python3-on-rhel
    - Mac OS X: https://docs.python.org/3/using/mac.html

- 安装依赖的包::

    sudo pip install sqlalchemy tornado mysqlclient hiredis

- 运行::

    $ cd <source code path>
    $ mysql -u root < sql/create_db.sql
    $ python init_test.py
    $ python3 run.py

API
-----

通用
~~~~~

对于所有的请求，一定会包含以下字段::

    {
        "status": 0,  // 请求状态，0为成功，1为失败
        "msg": "success",  // 对请求的描述或所发生错误的描述
    }

文件操作
~~~~~~~~~~

- ``/upload`` 上传文件到 ``static/img`` 下(POST):

    详见 ``file_upload.html``

登录登出
~~~~~~~~~

- ``/login/?`` 获取登录页面(GET)

- ``/login/?`` 使用电话号码和密码进行登录(POST):

  - phone: 注册用的电话号码
  - passwd: 注册的密码

- ``/logout/?`` 注销当前登录用户

用户
~~~~~~

- ``/user/([0-9]+)/?`` 获取用户信息，分为详细版（用户已登录）和简略版（未登录）(GET)::

    {
        "name": "路人甲",
        "register_at": "1456317626",
        "addresses": [],
        "phone": "99999",
        "avatar": ""
    }


- ``/user/new/?`` 创建新用户(POST):

  - phone，手机号，必填
  - passwd，密码，必填
  - level，用户等级，0为买家，1为卖家，2为管理员，选填，默认为0
  - name，用户名，选填，默认为手机号

- ``/user/([0-9]+)/?`` 修改用户信息(PUT):

    avatar,level,passwd,phone,name,address 选填

- ``/user/([0-9]+)/?`` 删除用户(DELETE):

    无需参数

食品
~~~~~

- ``/user/([0-9]+)/foods/?`` 获取该用户名下的所有食品列表，按创建时间由近及远排序(GET)::

    {
    "foods": [
        {
            "fid": 4,
            "price": 0,
            "create_at": "1456317627",
            "seller": 11,
            "name": "炸酱面",
            "image": ""
        },
        ...
    ],
    }

- ``/user/([0-9]+)/foods/?`` 新建食品，该API要求所给uid存在且等级为1(POST):

  - name：食品名，必填
  - image：图片路径，选填，默认为""
  - price：价格，选填，默认为0.0

- ``/user/([0-9]+)/foods/?`` 修改食品(PUT):

  - fid 食品id 必填
  - image,name,seller,price 选填

- ``/user/([0-9]+)/foods/?`` 删除食品(DELETE):

  - fid 必填

交易
~~~~~

- ``/user/([0-9]+)/deals/?`` 获取该用户所达成的所有交易(GET)::

    {
        "deals": [
            {
            "phone": "10086",
            "seller": {
                "addresses": [],
                "register_at": "1456317626",
                "name": "99999",
                "phone": "99999",
                "avatar": ""
            },
            "buyer": {
                "addresses": [],
                "register_at": "1456317626",
                "name": "99999",
                "phone": "99999",
                "avatar": ""
            },
            "food": {
                "fid": 5,
                "price": 1.11,
                "create_at": "1456317627",
                "seller": 11,
                "name": "好吃的",
                "image": ""
            },
            "sell_at": "1456317627",
            "address": "USA",
            "did": 10
            }
        ],
    }

- ``/user/([0-9]+)/deals/?`` 提交新的订单(POST):

  - seller 卖的人, 必填
  - fid 商品id，必填
  - address 配送地址，必填
  - phone 手机号码，必填

- ``/user/([0-9]+)/deals/?`` 删除订单(DELETE):

  - did 订单id
