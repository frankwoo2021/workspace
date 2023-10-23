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

import sys
import Login
from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt6.QtCore import QCoreApplication
if __name__ == '__main__':
    def usr_login():
        usr_name = ui.lineEditUserName.text()
        usr_pwd = ui.lineEditPassword.text()
        if usr_name == 'geekori' and usr_pwd == '1234':
            QMessageBox.information(MainWindow, '消息',
            "登录成功")

        else:
            QMessageBox.warning(MainWindow, '消息',
            "用户名或密码错误")      
        print()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Login.Ui_MainWindow()
    # 调用setupUi方法动态创建控件
    ui.setupUi(MainWindow)
    ui.pushButtonOK.clicked[bool].connect(usr_login)
    ui.pushButtonCancel.clicked.connect(QCoreApplication.instance().quit)
    # 显示窗口
    MainWindow.show()
   
    # 当窗口关闭后会退出程序
    sys.exit(app.exec())
    