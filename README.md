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

### 文档

首先请安装 ``apidocjs``:

```bash
npm install apidoc -g
```

然后访问目标地址的 ``/static/api/index.html`` 读取文档，如 ``http://192.168.80.130:8888/static/api/index.html``
