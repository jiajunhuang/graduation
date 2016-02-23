网上订餐系统的设计与实现
=========================

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
    $ python3 run.py
