# -*- encoding: utf-8 -*-
'''
@File    :   mailHander.py
@Time    :   2022/10/15 23:23:51
@Author  :   victor2022 
@Version :   1.0
@Desc    :   email sender
'''
import sys
import email.message
from email.mime.text import MIMEText
import smtplib
from .propHandler import  SenderLoader,ReceiverLoader
from log_helper import log

# mailSender class
class __MainSender:
    def __init__(self, configpath):
        # set configpath
        if(configpath==None):
            configpath = sys.path[0]
        # load config
        self.senderLoader = SenderLoader(configpath)
        self.receiverLoader = ReceiverLoader(configpath)
        # create client
        self.smtpClient = self.createClient()
        log.info("SMTP client has been created...")
        
    def createClient(self) -> smtplib.SMTP:
        # create smtp client
        client = smtplib.SMTP_SSL(self.senderLoader.host,self.senderLoader.port)
        client.login(self.senderLoader.username,self.senderLoader.password)
        return client
    
    def sendMail(self, content, subject="DEFAULT TITLE", fromaddr=None, toaddrs=[]):
        # load addrs from config
        if(fromaddr==None):
            fromaddr = self.senderLoader.username
        if(len(toaddrs)==0):
            toaddrs = self.receiverLoader.toaddrs
        # create mail message
        msg = email.message.EmailMessage()
        msg.set_content(content)
        msg["subject"] = subject
        msg["from"] = fromaddr
        msg["to"] = toaddrs
        # send mail with client
        self.smtpClient.sendmail(fromaddr,toaddrs,msg.as_string())
        log.info("Mail has been sent successfully from {}".format(fromaddr))

# singleton mailSender
def getMailSender(configpath) -> __MainSender:
    sender = __MainSender(configpath)
    return sender