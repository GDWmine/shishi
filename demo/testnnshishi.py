#coding=utf-8

from public.common import mytest
from public.pages.shishiPage import TXguanggaologin,TX682,TX678,NNshihi
import time
from public.common.publicfunction import get_img
from config import globalparam

imageName = globalparam.image_Name

class test_nn_shishi(mytest.MyTest):
    """楠楠实时"""

    def _TXguanggaologin(self):
        """封装广告页面QQ1456快捷登录"""
        TXguanggaologinPage = TXguanggaologin.TXguanggaologinPage(self.dr)
        TXguanggaologinPage.into_TX_page()
        TXguanggaologinPage.click_login_button()
        TXguanggaologinPage.click_login_1456()

    def _TX682(self):
        """封装打开682账户并获取数据"""
        TXguanggao682Page = TX682.TX682Page(self.dr)
        TXguanggao682Page.open682()
        TXguanggao682Page.click_button()
        global gb_huafei682
        gb_huafei682 = TXguanggao682Page.get_huafei682()
        global gb_baoguang682
        gb_baoguang682 = TXguanggao682Page.get_baoguang682()
        global gb_dianji682
        gb_dianji682 = TXguanggao682Page.get_dianji682()
        global gb_zhuce682
        gb_zhuce682= TXguanggao682Page.get_zhuce682()
        global gb_xiadan682
        gb_xiadan682= TXguanggao682Page.get_xiadan682()

    def _TX678(self):
        """封装打开678账户并获取数据"""
        TXguanggao678Page = TX678.TX678Page(self.dr)
        TXguanggao678Page.open678()
        TXguanggao678Page.click_button()
        global gb_huafei678
        gb_huafei678 = TXguanggao678Page.get_huafei678()
        global gb_baoguang678
        gb_baoguang678 = TXguanggao678Page.get_baoguang678()
        global gb_dianji678
        gb_dianji678 = TXguanggao678Page.get_dianji678()
        global gb_zhuce678
        gb_zhuce678= TXguanggao678Page.get_zhuce678()
        global gb_xiadan678
        gb_xiadan678= TXguanggao678Page.get_xiadan678()

    def _NNshihsiPage(self):
        riqi = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        shijianduan = "00:00~{}:00".format(time.localtime().tm_hour)
        NNshihsiPage = NNshihi.NNshihsiPage(self.dr)
        NNshihsiPage.openNNshihsiPage()
        NNshihsiPage.click_login_button()
        NNshihsiPage.switch_to_qqlogin_frame()
        NNshihsiPage.click_login_1456()

        # NNshihsiPage.write_number(440,187,riqi)
        # NNshihsiPage.write_number(40,0,shijianduan)

        # NNshihsiPage.write_number(100,0,gb_huafei682)
        # NNshihsiPage.write_number(100,0,gb_baoguang682)
        # NNshihsiPage.write_number(90,0,gb_dianji682)
        # NNshihsiPage.write_number(160,0,gb_zhuce682)
        # NNshihsiPage.write_number(70,0,gb_xiadan682)

        # NNshihsiPage.write_number(-440,20,gb_huafei678)
        # NNshihsiPage.write_number(100,0,gb_baoguang678)
        # NNshihsiPage.write_number(90,0,gb_dianji678)
        # NNshihsiPage.write_number(160,0,gb_zhuce678)
        # NNshihsiPage.write_number(70,0,gb_xiadan678)
        # time.sleep(5)
        
        get_img(NNshihsiPage.dr,imageName)
        time.sleep(1)


    def test_01_open_TXguanggaologinPage(self):
        # self._TXguanggaologin()
        # self._TX682()
        # self._TX678()
        self._NNshihsiPage()
        # self.my_print("花费：{0} 曝光：{1} 点击：{2} 注册：{3} 下单：{4}".format(gb_huafei682, gb_baoguang682, gb_dianji682, gb_zhuce682, gb_xiadan682))
        # self.my_print("花费：{0} 曝光：{1} 点击：{2} 注册：{3} 下单：{4}".format(gb_huafei678, gb_baoguang678, gb_dianji678, gb_zhuce678, gb_xiadan678))