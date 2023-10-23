#########################################################################
# 作者:李宁（蒙娜丽宁），UnityMarvel创始人
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'hello world'

@app.route('/register', methods=['POST'])
def register():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return '注册成功'

if __name__ == '__main__':
    app.run()
