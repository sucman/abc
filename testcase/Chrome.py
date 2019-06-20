# -*- coding:utf-8 -*-
import time
import unittest

from appium import webdriver


class Chrome(unittest.TestCase):
    @classmethod
    def setUp(self):
        chr = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "platformVersion": "9",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main",
            # "app":"C:\\Users\\shuchengxiang\\Desktop\\shoujibaidu_25580288.apk",
            "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
            "resetKeyboard": True  # 运行完成后重置软键盘的状态　
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", chr)  # 启动app
        time.sleep(3)

    @classmethod
    def test_search(self):
        self.driver.find_element_by_id("terms_accept").click()
        self.driver.find_element_by_id("negative_button").click()
        self.driver.find_element_by_id("search_box_text").click()
        time.sleep(1)

        self.driver.tap([(983, 1841), (983, 1841)], 200)
        time.sleep(3)

        self.driver.tap([(172, 962), (172, 962)], 200)
        time.sleep(3)

        ipt = self.driver.find_element_by_id("url_bar")
        ipt.send_keys("appium")

        self.driver.tap([(988, 1698), (989, 1699)], 100)  # 坐标点和按压时间（毫秒）

        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
