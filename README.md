Todo应用简介
- 开发流程
    产品设计 -> 前端 -> 后端 -> 测试

    - 后端开发流程
        需求分析 -> 设计 -> 编码 -> 测试

- 详细设计
    - 架构设计
        客户端 -> 服务器 -> Todo app -> MongoDB

    - 开发技术
        前端： vue.js
        后端： flask
        数据库： MongoDB

    - flask的扩展
        flask-mongoEngine   连接数据库
        flask-script    外部脚本编写
        flask-WTF       表单验证

    - 项目结构

        todu
            app
                static
                    bootstrap.min.css
                    index.css
                templates
                    404.html
                    base.html
                    index.html
                __init__.py
                models.py
                views.py
            etc
            tests
            __init__.py
            config.py
            manage.py
            README
            run.py
    - 数据模型

Todo应用的详细设计
实现查询与保存功能
实现更新与删除功能
改进Todo应用的用户体验
测试
