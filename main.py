# -*- coding:utf-8 -*-
"""
"""
import HTMLTestRunner
import time
import unittest

from control import new_file
from control import send_email

if __name__ == '__main__':
    print('=====AutoTest Start======')
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    #    test_dir='./test_case'
    # Windows的cmd执行：python "D:\system files\workspace\selenium\test_project\runtest_htmltestrunner_autosendemail.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    test_dir = 'E:\\Python 3.0\\PycharmProjects\\abc\\testcase'
    # 知道测试报告的路径
    test_report_dir = 'E:\\Python 3.0\\PycharmProjects\\abc\\report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    # 需屏蔽fp中的中文文字说明。否则在windows下执行会报：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 553: ordinal not in range(128)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(discover)
    # 注意：调用函数一定要加括号，一个括号害死个人，哎，查了几天的问题，才发现导致html文件始终显示空白，就是因为close函数调用不正确，漏了括号。
    fp.close()

    # 2.取最新测试报告
    new_report = new_file.new_file(test_report_dir)
    # 调试用的
    #    print new_report

    # 3.发送邮件，发送最新测试报告html
    send_email.send_email(new_report)
    print('=====AutoTest Over======')
