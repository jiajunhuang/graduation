# 网上订餐系统的设计与实现

## 介绍 & 安装

该系统要求能够在线餐饮信息浏览，在线订餐，
在线订单处理以及信息更新和删除等功能。

    本项目采用前后端分离的开发方式，其中API和admin由@jiajunhuang完成，
    前端由@zzuieliyaoli完成。(由于没有把项目文件分开，故目录看起来有点乱)

### 结构介绍:

```bash
# tree -d -L 2
.
├── controllers  # 控制层
├── models # 模型层
├── sql
├── static  # 静态文件
│   ├── css
│   ├── img
│   └── js
├── templates # 视图层
│   └── admin # 后台的模板
└── utils
```

### Front End

**vue-webpack-boilerplate**

#### Usage

``` bash
$ cd graduation
$ npm install
$ npm run dev
```

#### Folder Structure

``` bash
.
├── package.js              # build scripts and dependencies
├── .babelrc                  # babel configuration
├── .eslintrc.js              # eslint configuration
├── build
│   ├── dev-server.js         # development server script
│   ├── karma.conf.js         # unit testing config
│   ├── webpack.base.conf.js  # shared base webpack config
│   ├── webpack.dev.conf.js   # development webpack config
│   └── webpack.prod.conf.js  # production webpack config
├── src
│   ├── index.html            # main html file
│   ├── main.js               # app entry file
│   ├── App.vue               # main app component
│   ├── components            # ui components
│   │   └── ...
│   └── assets                # static assets
│       └── ...
└── test
│   └── unit                  # unit tests
│       ├── index.js          # unit test entry file
│       └── ...
└── dist                      # built static files
```

#### What's Included

- `npm run dev`: first-in-class development experience.
  - Webpack + `vue-loader` for single file Vue components.
  - State preserving hot-reload
  - State preserving compilation error overlay
  - Lint-on-save with ESLint
  - Source maps

- `npm run build`: Production ready build.
  - JavaScript minified with [UglifyJS](https://github.com/mishoo/UglifyJS2).
  - HTML minified with [html-minifier](https://github.com/kangax/html-minifier).
  - CSS across all components extracted into a single file and minified with [cssnano](https://github.com/ben-eb/cssnano).
  - All static assets compiled with version hashes for efficient long-term caching, and a production `index.html` is auto-generated with proper URLs to these generated assets.
  - **To serve built files, run an HTTP server inside `/dist`**.

- `npm test`: Unit tests run in PhantomJS with Karma + karma-jasmine + karma-webpack.
  - Supports ES2015 in test files.
  - Supports all webpack loaders.
  - Easy [mock injection](http://vuejs.github.io/vue-loader/workflow/testing-with-mocks.html).

For detailed explanation on how things work, consult the [docs for vue-loader](http://vuejs.github.io/vue-loader).


### API运行方式:

- 安装python3,MySQL,Redis

    - ArchLinux: sudo pacman -S python mariadb redis
    - Debian/Ubuntu: sudo apt-get install python3 mysql-server redis-server

- 安装依赖的包

```bash
sudo pip3 install sqlalchemy tornado mysqlclient redis
```

- 运行

```bash
$ cd <source code path>
$ mysql -u root < sql/create_db.sql
$ python3 init_test.py
$ ./start.sh  # 这是debug模式
```

## API

### 通用

```js
对于所有的请求，一定会包含以下字段
{
    "status": 0,  // 请求状态，0为成功，1为失败
    "msg": "success",  // 对请求的描述或所发生错误的描述
    "sid": "xxxxxxxxxx", // 类似cookie，从服务端保存用户信息
}
```

### 文件操作


- `/upload` 上传文件到 `static/img` 下(POST):

    > 详见 `file_upload.html`

### 登录登出


- `/login/?` 获取登录页面(GET)

- `/login/?` 使用电话号码和密码进行登录(POST):

  - phone: 注册用的电话号码
  - passwd: 注册的密码

- `/logout/?` 注销当前登录用户

### 用户

- `/user/new/?` 注册新用户(POST)

  - level 用户等级，0为买家，1为卖家, 默认为0
  - phone 手机号
  - passwd 密码
  - name 名字，如不填，则为手机号

- `/user/([0-9]+)/?` 获取用户信息，分为详细版（用户已登录）和简略版（未登录）(GET)

```js
{
    "name": "路人甲",
    "register_at": "1456317626",
    "addresses": [],
    "phone": "99999",
    "avatar": ""
}
```

- `/user/new/?` 创建新用户(POST):

  - phone，手机号，必填
  - passwd，密码，必填
  - level，用户等级，0为买家，1为卖家，2为管理员，选填，默认为0
  - name，用户名，选填，默认为手机号

- `/user/([0-9]+)/?` 修改用户信息(PUT):

    > avatar,level,passwd,phone,name,address 选填

- `/user/([0-9]+)/?` 删除用户(DELETE):

    > 无需参数

### 食品

- `/user/([0-9]+)/foods/?` 获取该用户名下的所有食品列表，按创建时间由近及远排序(GET)

```js
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
```

- `/user/([0-9]+)/foods/?` 新建食品，该API要求所给uid存在且等级为1(POST):

  - name：食品名，必填
  - image：图片路径，选填，默认为""
  - price：价格，选填，默认为0.0

- `/user/([0-9]+)/foods/?` 修改食品(PUT):

  - fid 食品id 必填
  - image,name,seller,price 选填

- `/user/([0-9]+)/foods/?` 删除食品(DELETE):

  - fid 必填

### 交易


- `/user/([0-9]+)/deals/?` 获取该用户所达成的所有交易(GET)

```js
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
```

- `/user/([0-9]+)/deals/?` 提交新的订单(POST):

  - seller 卖家, 必填
  - fid 商品id，必填
  - address 配送地址，必填
  - phone 手机号码，必填

- `/user/([0-9]+)/deals/?` 删除订单(DELETE):

  - did 订单id
