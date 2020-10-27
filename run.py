#coding=utf-8

import time
import unittest

import HTMLTestRunner

from config import globalparam
from public.common import sendmail


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    # reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='脚本运行状况',
            description='如果运行状态为通过，说明脚本正常运行，可点击URL或附件截图进行实时数据的查看，如果为不通过需要手动填写实时数据（附实时查看URL："https://docs.qq.com/sheet/DU2ZVT3NXcnJuVGJZ?tab=BB08J2"）'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()
    

if __name__=='__main__':
    run()


