# -*- coding:utf-8 -*-
'''
注册
'''

import time
import unittest
import warnings

from appium import webdriver
from control import config
from control import db


class Register(unittest.TestCase):
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
    def test_register(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告

        self.driver.find_element_by_id("loginBtn").click()

        # 登录页跳注册
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView").click()

        # 输入注册邮箱
        iptidentityId = self.driver.find_element_by_id("identityId")
        iptidentityId.send_keys(config.REG_MAIL)

        # 发送验证码
        self.driver.find_element_by_id("downTimerText").click()

        time.sleep(3)

        # 输入验证码
        iptverifyCode = self.driver.find_element_by_id("verifyCode")
        result = db.get_code("CONTENT", "mns.t_notify_msg", "APP_ID", "SMSG", "GMT_CREATE")
        mailcode = result[-6:]
        iptverifyCode.send_keys(mailcode)

        # 输入密码
        iptloginPasswd = self.driver.find_element_by_id("loginPasswd")
        iptloginPasswd.send_keys(config.OLD_PWD)

        # 输入昵称
        iptloginName = self.driver.find_element_by_id("loginName")
        iptloginName.send_keys(config.REG_NAME)

        # 输入邀请码
        iptinvitationCode = self.driver.find_element_by_id("invitationCode")
        result = db.get_info("INVITATION_CODE", "member.tm_member", "MEMBER_NAME", "testx", "CREATE_TIME")
        iptinvitationCode.send_keys(result)

        # 点击注册
        self.driver.find_element_by_id("register").click()

        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
