# -*- coding:utf-8 -*-
"""
邀请好友
"""

import time
import unittest
import warnings

from appium import webdriver
from control import config


class FrameLayout(unittest.TestCase):

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

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView").click()

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()

        edittext = self.driver.find_element_by_id("search")
        edittext.send_keys(config.LOG_MAIL)
        time.sleep(3)

        self.driver.find_element_by_id("search").click()
        # self.driver.keyevent(66)
        # self.driver.press_keycode(66)
        self.driver.tap([(660, 1214), (660, 1214)], 200)
        time.sleep(3)

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout").click()

        self.driver.find_element_by_id("addContactsBtn").click()

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageButton").click()

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()

        if self.driver.find_element_by_text("xybtest2@tf.com"):
            print("添加联系人成功！")
        else:
            print("已添加联系人或添加联系人失败")

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
