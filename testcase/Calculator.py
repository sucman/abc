# -*- coding:utf-8 -*-
import time
import unittest

from appium import webdriver


class Calculator(unittest.TestCase):
    @classmethod
    def setUp(self):
        cal = {
            "platformName": "Android",  # 设备平台
            "deviceName": "emulator-5554",  # 设备名称
            "platformVersion": "9",  # 设备系统版本
            "appPackage": "com.android.calculator2",  # 包名
            "appActivity": ".Calculator",  # 启动项
            # "app":"C:\\Users\\shuchengxiang\\Desktop\\shoujibaidu_25580288.apk",#apk包路径
            "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
            "resetKeyboard": True  # 运行完成后重置软键盘的状态　
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', cal)  # 启动app
        time.sleep(3)

    @classmethod
    def test_calculation(self):
        self.driver.find_element_by_id("digit_1").click()
        self.driver.find_element_by_id("op_add").click()
        self.driver.find_element_by_id("digit_9").click()
        self.driver.find_element_by_id("eq").click()

        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
