#coding=utf-8

from public.common import mytest
from public.pages.shishiPage import TXguanggaologin,TX682,TX678,NNshihi,TX302,TX303
import time
from public.common.publicfunction import get_img
from config import globalparam

imageName = globalparam.image_Name

class test_nn_shishi(mytest.MyTest):
    """楠楠实时"""

    def _TXguanggaologin(self):
        """封装广告页面QQ快捷登录"""
        TXguanggaologinPage = TXguanggaologin.TXguanggaologinPage(self.dr)
        TXguanggaologinPage.into_TX_page()
        TXguanggaologinPage.click_login_button()
        TXguanggaologinPage.click_login_()

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

    def _TX302(self):
        """封装打开302账户并获取数据"""
        TXguanggao302Page = TX302.TX302Page(self.dr)
        TXguanggao302Page.open302()
        TXguanggao302Page.click_button()
        global gb_huafei302
        # time.sleep(1000)
        gb_huafei302 = TXguanggao302Page.get_huafei302()
        global gb_baoguang302
        gb_baoguang302 = TXguanggao302Page.get_baoguang302()
        global gb_dianji302
        gb_dianji302 = TXguanggao302Page.get_dianji302()
        global gb_zhuce302
        gb_zhuce302= TXguanggao302Page.get_zhuce302()
        global gb_xiadan302
        gb_xiadan302= TXguanggao302Page.get_xiadan302()

    def _TX303(self):
        """封装打开303账户并获取数据"""
        TXguanggao303Page = TX303.TX303Page(self.dr)
        TXguanggao303Page.open303()
        TXguanggao303Page.click_button()
        global gb_huafei303
        gb_huafei303 = TXguanggao303Page.get_huafei303()
        global gb_baoguang303
        gb_baoguang303 = TXguanggao303Page.get_baoguang303()
        global gb_dianji303
        gb_dianji303 = TXguanggao303Page.get_dianji303()
        global gb_zhuce303
        gb_zhuce303= TXguanggao303Page.get_zhuce303()
        global gb_xiadan303
        gb_xiadan303= TXguanggao303Page.get_xiadan303()

    def _NNshihsiPage(self):
        riqi = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # shijianduan = "00:00~{}:00".format(time.localtime().tm_hour)
        if int(time.localtime().tm_min) >= 30:
            shijianduan = "{}:30".format(time.localtime().tm_hour)
        else:
            shijianduan = "{}:00".format(time.localtime().tm_hour)
        NNshihsiPage = NNshihi.NNshihsiPage(self.dr)
        # 302/303账户
        NNshihsiPage.opennewNNshihsiPage()
        NNshihsiPage.click_login_button()
        NNshihsiPage.switch_to_qqlogin_frame()
        NNshihsiPage.click_login_()
        """
        682/678账户
        
        NNshihsiPage.write_number(440,187,riqi)
        NNshihsiPage.write_number(40,0,shijianduan)
        # 682账户
        NNshihsiPage.write_number(100,0,gb_huafei682)
        NNshihsiPage.write_number(100,0,gb_baoguang682)
        NNshihsiPage.write_number(90,0,gb_dianji682)
        NNshihsiPage.write_number(160,0,gb_zhuce682)
        NNshihsiPage.write_number(70,0,gb_xiadan682)
        # 682账户
        NNshihsiPage.write_number(-440,20,gb_huafei678)
        NNshihsiPage.write_number(100,0,gb_baoguang678)
        NNshihsiPage.write_number(90,0,gb_dianji678)
        NNshihsiPage.write_number(160,0,gb_zhuce678)
        NNshihsiPage.write_number(70,0,gb_xiadan678)
        time.sleep(5)
        """
        # 302账户
        NNshihsiPage.write_number(60,320,riqi)
        NNshihsiPage.write_number(90,0,shijianduan)
        NNshihsiPage.write_number(90,0,gb_huafei302)
        NNshihsiPage.write_number(90,0,gb_zhuce302)
        NNshihsiPage.write_number(90,0,gb_xiadan302)
        NNshihsiPage.write_number(90,0,gb_baoguang302)
        NNshihsiPage.write_number(90,0,gb_dianji302)
        # 303账户
        NNshihsiPage.write_number(-360,30,gb_huafei303)
        NNshihsiPage.write_number(90,0,gb_zhuce303)
        NNshihsiPage.write_number(90,0,gb_xiadan303)
        NNshihsiPage.write_number(90,0,gb_baoguang303)
        NNshihsiPage.write_number(90,0,gb_dianji303)

        get_img(NNshihsiPage.dr,imageName)
        time.sleep(1)


    def test_01_open_TXguanggaologinPage(self):
        self._TXguanggaologin()
        # self._TX682()
        # self._TX678()
        self._TX302()
        self._TX303()
        self._NNshihsiPage()