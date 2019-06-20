# -*- coding:utf-8 -*-
"""
转账
"""

import time
import unittest
import warnings

from appium import webdriver
from control import config


class Transfer(unittest.TestCase):

    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告

        cal = {
            "platformName": "Android",  # 设备平台
            "deviceName": "b43d2c1",  # 设备名称
            "platformVersion": "6.0.1",  # 设备系统版本
            "appPackage": "com.viausd.pay",  # 包名
            "appActivity": "com.viausd.activity.MainActivity",  # 启动项
            # "app":"C:\\Users\\shuchengxiang\\Desktop\\shoujibaidu_25580288.apk",#apk包路径
            "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
            "resetKeyboard": True  # 运行完成后重置软键盘的状态　
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', cal)  # 启动app
        time.sleep(5)

    @classmethod
    def test_something(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告

        self.driver.find_element_by_id("loginBtn").click()

        iptmail = self.driver.find_element_by_id("identityId")
        iptmail.send_keys(config.LOG_MAIL)

        iptpwd = self.driver.find_element_by_id("password")
        iptpwd.send_keys(config.OLD_PWD)

        self.driver.find_element_by_id("loginBtn").click()

        time.sleep(10)

        self.driver.find_element_by_id("mainItem2").click()
        time.sleep(3)

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout").click()

        time.sleep(3)

        self.driver.find_element_by_id("allBtn").click()

        moneyEdit = self.driver.find_element_by_id("moneyEdit")
        moneyEdit.send_keys("12345")

        self.driver.find_element_by_id("addInfoText").click()

        addInfoEdit = self.driver.find_element_by_id("addInfoEdit")
        addInfoEdit.send_keys("转账测试")

        self.driver.find_element_by_id("nextBtn").click()

        googleCodeEdit = self.driver.find_element_by_id("googleCodeEdit")
        googleCodeEdit.send_keys("123456")

        self.driver.find_element_by_id("confirmBtn").click()

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
