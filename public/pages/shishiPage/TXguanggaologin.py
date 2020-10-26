from public.common import basepage
from config import globalparam
import time

url = globalparam.project_url
TXuser = globalparam.TXuser

class TXguanggaologinPage(basepage.Page):

    def into_TX_page(self):
        """打开腾讯广告页"""
        self.dr.open('https://e.qq.com/')
    def click_login_button(self):
        """点击登录按钮"""
        self.dr.click('id->mlogin')
        time.sleep(10)
        self.dr.switch_to_frame('id->qqLoginFrame')
        time.sleep(1)
        self.dr.switch_to_frame('id->ptlogin_iframe')
    def click_login_(self):
        self.dr.click('id->img_out_{0}'.format(TXuser))
        time.sleep(5)




