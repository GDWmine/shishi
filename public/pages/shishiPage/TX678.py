from public.common import basepage
from config import globalparam
import time


class TX678Page(basepage.Page):

    def open678(self):
        """利用js新开窗口打开678账户并切换页面句柄"""
        js = "window.open('https://ad.qq.com/atlas/17567678/report/analytic?')"
        self.dr.open_new_window_js(js)
    def click_button(self):
        """点击转化回传按钮"""
        self.dr.click('xpath->//*[@id="content"]/div/div/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div/button[2]')
    def get_huafei678(self):
        """返回678账户花费"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[2]/div')
    def get_baoguang678(self):
        """返回678账户曝光"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[7]/div')
    def get_dianji678(self):
        """返回678账户点击"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[8]/div')
    def get_zhuce678(self):
        """返回678账户注册"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[3]/div')
    def get_xiadan678(self):
        """返回678账户下单"""
        return self.dr.get_text('xpath->//*[@id="table-id"]/div[2]/div/table/tfoot/tr/td[5]/div')
