from public.common import basepage
from config import globalparam
import time


class TX304Page(basepage.Page):

    def open304(self):
        """利用js新开窗口打开304账户并切换页面句柄"""
        js = "window.open('https://ad.qq.com/atlas/18034304/report/analytic?')"
        self.dr.open_new_window_js(js)
    def click_button(self):
        """点击转化回传按钮"""
        self.dr.click('xpath->//*[@id="content"]/div/div/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div/button[2]')
    def get_huafei304(self):
        """返回304账户花费"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[2]/div')
    def get_baoguang304(self):
        """返回304账户曝光"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[7]/div')
    def get_dianji304(self):
        """返回304账户点击"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[8]/div')
    def get_zhuce304(self):
        """返回304账户注册"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[3]/div')
    def get_xiadan304(self):
        """返回304账户下单"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[5]/div')
