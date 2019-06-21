# -*- coding:utf-8 -*-
'''

'''
from control import getRandom

"""
用户
"""
LOG_MAIL = "xybtest7@tf.com"

a = getRandom.ranstr(9)
REG_MAIL = a + "@tf.com"

REG_NAME = a

OLD_PWD = "qweqwe123"
NEW_PWD = "qweqwe1234"

'''
DB
'''
DB_HOST = "192.168.9.168"
DB_USER = "reader"
DB_PWD = "reader"
DB_DATABASE = ""
DB_TABLE = ""
DB_PORT = 3306

'''
mail
'''
MAIL_HOST = "smtp.exmail.qq.com"  # 设置服务器
MAIL_USER = "xiangyb@tigerft.com"
MAIL_PWD = "Tiger123"
MAIL_SENDER = "xiangyb@tigerft.com"
MAIL_RECEIVERS = ["920100886@qq.com"]