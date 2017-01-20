
***
alliance
openapi based on flask_restful
openapi-py opl怎么用可以看openapipy/cmds/shell.py
huskar  配置管理
***
parser 参数校检
resources url入口
handler 具体逻辑实现
serializer->BaseSerializer->do_serialize->fillup 数据序列化（包装？
model: permission
rpc 数据库接口
***
tests
confest.py 测试上下文
mock->thrift_file 看thrift_file 可以清楚你要mock的函数的返回值
***
+ oid/id oid是假的id，为了防止暴露id而存在的。或者说是对外展示的id
+ url 前后的 ／ ，否则sig可能不对
+ app与consumer_key应该是one_to_one的关系
+ 起alliance的服务用make server 不是python manage.py
+ 起openapi的服务用ves serve [--wsgi] 更多的参数看zeus_core doc
+ huskar的配置
+ pr 小一点好，容易看
***
+ [业务接口说明](http://openapi.eleme.io/v2/quickstart.html)
+ [huskar](http://soa-zk.alpha.elenet.me/application/base.openapi/config)
+ [zeus_core](https://t.elenet.me/zeus_core_doc/)
***
+ IPython/Jupter
+ vitrualenvwrapper
