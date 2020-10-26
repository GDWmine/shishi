import uiautomator2 as u2 
from time import sleep

d = u2.connect()
d.app_start("com.taobao.taobao")
sleep(5)
d(description="主互动").click()
sleep(5)
if d(textContains="喵币点击领取").exists:
    d(textContains="喵币点击领取").click()
    sleep(3)

# d(text="赚喵币").click()
d(text="赚喵币")[0].click()

sleep(3)
if d(text="每日签到喵币(0/1)").exists:
    d(text="每日签到喵币(0/1)").click()
    sleep(3)
while(d(text="去浏览").exists or d(text="去搜索").exists or d(text="逛一逛").exists or len(d(text="去完成"))>2):
    if d(text="去浏览").exists:
        d(text="去浏览")[0].click()
    elif d(text="去搜索").exists:
        d(text="去搜索")[0].click()
    elif d(text="逛一逛").exists:
        d(text="逛一逛")[0].click()
    elif len(d(text="去完成"))>2:
        d(text="去完成")[1].click()
    sleep(18)
    d(text="任务完成").exists(timeout=3.0)
    d.press("back")
    sleep(3)
while(d(text="领取奖励").exists):
    d(text="领取奖励").click()
    sleep(5)


#跳支付宝领喵币
d(text="去支付宝领更多喵币").click()
sleep(10)
if not d.wait_activity("com.alipay.mobile.nebulax.integration.mpaas.activity.NebulaActivityMain",timeout=10):
    raise Exception("未启动到支付宝领喵币界面")
if d(text="好的，我知道了").exists:
    d(text="好的，我知道了").click()
    sleep(3)
d(text="赚喵币").click()
sleep(3)
if d(text="签到").exists:
    d(text="签到").click()
    sleep(3)
    d(text="好的，我知道了").click()
    sleep(3)
while(d(text="逛一逛").exists):
    if d(text="逛一逛").exists:
        d(text="逛一逛")[0].click()
        sleep(5)
        d.press("back")
        sleep(3)
        d(text="好的，我知道了").click()
        sleep(3)
d(text="关闭任务弹窗").click()
sleep(3)

