#coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam

# 测试报告的路径
imageName = globalparam.image_Name
reportPath = globalparam.report_path
imgPath = globalparam.img_path
logger = Log()
# 配置收发件人
recvaddress = ['1456904332@qq.com','2850069566@qq.com']
# 163的用户名和密码
sendaddr_name = '13644763126@163.com'
sendaddr_pswd = '2850069566nn#'
sendaddr_pass = 'RJUNSTDKWDMYWRLB'

class SendMail:
	def __init__(self,recver=None):
		"""接收邮件的人：list or tuple"""
		if recver is None:
			self.sendTo = recvaddress
		else:
			self.sendTo = recver

	def __get_report(self):
		"""获取最新测试报告"""
		dirs = os.listdir(reportPath)
		dirs.sort()
		newreportname = dirs[-1]
		print('The new report name: {0}'.format(newreportname))
		return newreportname
	def __get_image(self):
		"""获取最新截图"""
		dirs = os.listdir(imgPath)
		dirs.sort()
		newimagename = dirs[-1]
		print('The new image name: {0}'.format(newimagename))
		return newimagename


	def __take_messages(self):
		"""生成邮件的内容，和html报告附件"""
		newreport = self.__get_report()
		newimage = self.__get_image()
		self.msg = MIMEMultipart()
		self.msg['Subject'] = '运行状况'
		self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

		with open(os.path.join(reportPath,newreport), 'rb') as f:
			mailbody = f.read()
		html = MIMEText(mailbody,_subtype='html',_charset='utf-8')
		self.msg.attach(html)
		
		# html附件
		att1 = MIMEText(mailbody, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="runLog.html"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
		self.msg.attach(att1)

		with open(os.path.join(imgPath,newimage), 'rb') as f:
			mailbody = f.read()
		html = MIMEText(mailbody,_subtype='image',_charset='png')
		self.msg.attach(html)
		
		# image附件
		att1 = MIMEText(mailbody, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename={0}'.format(imageName)#这里的filename可以任意写，写什么名字，邮件中显示什么名字
		self.msg.attach(att1)


	def send(self):
		"""发送邮件"""
		self.__take_messages()
		self.msg['from'] = sendaddr_name
		try:
			smtp = smtplib.SMTP('smtp.163.com',25)
			# smtpObj.login(mail_user,mail_pass)
			smtp.login(sendaddr_name,sendaddr_pass)
			smtp.sendmail(self.msg['from'], self.sendTo,self.msg.as_string())
			smtp.close()
			logger.info("发送邮件成功")
		except Exception:
			logger.error('发送邮件失败')
			raise

if __name__ == '__main__':
	sendMail = SendMail()
	sendMail.send()

        
