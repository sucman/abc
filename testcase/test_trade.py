# -*- coding:utf-8 -*-
"""
购买usdt
"""

import logging
import random
import time
import unittest
import warnings

from appium import webdriver
from control import config


class Trade(unittest.TestCase):

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

        try:
            self.driver.find_element_by_id("loginBtn").click()
            time.sleep(20)
        except TimeoutError as err:
            logging.error("登录超时 %s", err)
            self.driver.quit()

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout").click()
        time.sleep(5)

        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        time.sleep(10)

        self.driver.find_element_by_xpath('//android.view.View[@content-desc="全部买入"]').click()

        self.driver.find_element_by_xpath('//android.view.View[@content-desc="最多可购买4000000.00"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="删除"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="删除"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="删除"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="删除"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="删除"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="1"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="2"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="完成"]').click()
        time.sleep(3)

        a = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="取消"]').click()
        b = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="下单"]').click()
        c = (a, b)
        if random.choice(c) == a:
            print("取消下单！")
            time.sleep(3)
            self.driver.quit()
        else:
            self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="下单"]').click()
            self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="去付款"]"]').click()
            self.driver.find_element_by_xpath('// android.widget.Button[ @ content - desc = "已完成付款"]').click()
            logging.info("付款完成，等待放币。")

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
