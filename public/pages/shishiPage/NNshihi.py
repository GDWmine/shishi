from public.common import basepage
from config import globalparam
import time

EXuser = globalparam.EXuser

class NNshihsiPage(basepage.Page):

    def opennewNNshihsiPage(self):
        # 302/303账户
        """利用js新开窗口打开腾讯文档并切换页面句柄"""
        js = "window.open('https://docs.qq.com/sheet/DU2ZVT3NXcnJuVGJZ?tab=BB08J2')"
        self.dr.open_new_window_js(js)

    def openNNshihsiPage(self):
        # 682/678账户
        """利用js新开窗口打开腾讯文档并切换页面句柄"""
        js = "window.open('https://docs.qq.com/sheet/DU1F6UVF4a2J4ZkdI?tab=bb08j2')"
        self.dr.open_new_window_js(js)
    def click_login_button(self):
        self.dr.click('xpath->//*[@id="blankpage-button-pc"]')
    def switch_to_qqlogin_frame(self):
        self.dr.switch_to_frame('id->login_frame')
    def click_login_(self):
        self.dr.click('id->img_out_{0}'.format(EXuser))
        time.sleep(10)
    def write_number(self,x,y,values):
        self.dr.move_by_offset_double_click(x,y)
        time.sleep(2)
        self.dr.type_and_TAB('xpath->//*[@id="alloy-rich-text-editor"]/span',values)