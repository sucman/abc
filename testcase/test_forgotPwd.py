# -*- coding:utf-8 -*-
"""
忘记密码
"""

import time
import unittest
import warnings

from appium import webdriver
from control import config
from control import db


class ForgotPwd(unittest.TestCase):

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
    def test_forgotPwd(self):
        # 跳登录页
        self.driver.find_element_by_id("loginBtn").click()

        # 进忘记密码页
        self.driver.find_element_by_id("forgotPwd").click()

        # 输入要找回的邮箱
        phoneNumberText = self.driver.find_element_by_id("phoneNumberText")
        phoneNumberText.send_keys(config.LOG_MAIL)

        # 获取邮箱验证码
        self.driver.find_element_by_id("downTimerText").click()

        time.sleep(5)

        # 查询并输入邮箱验证码
        verifyCodeText = self.driver.find_element_by_id("verifyCodeText")
        result = db.get_info("CONTENT", "mns.t_notify_msg", "APP_ID", "SMSG", "GMT_CREATE")
        mailcode = result[-6:]
        verifyCodeText.send_keys(mailcode)

        # 下一步
        self.driver.find_element_by_id("nextBtn").click()

        # 输入新密码
        newPwdEdit = self.driver.find_element_by_id("newPwdEdit")
        newPwdEdit.send_keys(config.NEW_PWD)

        # 确认新密码
        newPwdAgainEdit = self.driver.find_element_by_id("newPwdAgainEdit")
        newPwdAgainEdit.send_keys(config.NEW_PWD)

        # 确认修改
        self.driver.find_element_by_id("confirmBtn").click()

        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
