# -*- coding:utf-8 -*-
"""
dirver配置
"""

import unittest
import warnings

from appium import webdriver


class driver_configure(unittest.TestCase):
    @classmethod
    def get_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        try:
            dri = {
                "platformName": "Android",  # 设备平台
                "deviceName": "b43d2c1",  # 设备名称
                "platformVersion": "6.0.1",  # 设备系统版本
                "appPackage": "com.viausd.pay",  # 包名
                "appActivity": "com.viausd.activity.MainActivity",  # 启动项
                # "app":"C:\\Users\\shuchengxiang\\Desktop\\shoujibaidu_25580288.apk",#apk包路径
                "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
                "resetKeyboard": True  # 运行完成后重置软键盘的状态　
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', dri)  # 启动app
            return self.driver
        except Exception as e:
            raise e
