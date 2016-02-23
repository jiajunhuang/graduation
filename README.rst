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

- 安装python3

    - ArchLinux: sudo pacman -S python
    - Debian/Ubuntu: sudo apt-get install python3
    - Centos: http://stackoverflow.com/questions/8087184/installing-python3-on-rhel
    - Mac OS X: https://docs.python.org/3/using/mac.html

- 安装依赖的包::

    sudo pip install sqlalchemy tornado mysqlclient

- 运行::

    $ cd <source code path>
    $ mysql -u root < sql/create_db.sql
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

用户
~~~~~~

- ``/user/([0-9]+)/?`` 获取用户信息，分为详细版（用户已登录）和简略版（未登录）(GET)::

    {
        "register_at": "1456225721",  // 注册时间戳
        "address": ["address A", "address B"],  // 配送地址
        "avatar": "",  // 头像url
        "name": "10086",  // 用户名
        "phone": "10086",  // 手机号码
    }


- ``/user/new/?`` 创建新用户(POST):

  - level，用户等级，0为买家，1为卖家，2为管理员，选填，默认为0
  - phone，手机号，注册时必填
  - passwd，密码，必填
  - name，用户名，选填，默认为手机号
