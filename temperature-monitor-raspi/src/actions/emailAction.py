# -*- encoding: utf-8 -*-
'''
@File    :   emailActions.py
@Time    :   2022/10/16 17:11:46
@Author  :   victor2022 
@Version :   1.0
@Desc    :   Action for sending email
'''
import os
import time
from actions.baseAction import BaseAction
from email_sender.handlers import mailHander
from log_helper import log
from datetime import datetime

class EmailAction(BaseAction):
    def __init__(self, configpath):
        self.sender = mailHander.getMailSender(configpath)
        # last email time
        self.last = 0
    
    def warn(self, msg: str, *args):
        super().warn(msg,*args)
        # if time has past 1min, send another email
        currTime = time.time()
        if(currTime-self.last>60):
            self.last = currTime
            log.warn("HIGH TEMPERATURE!!! Sending email...")
            msg = "WARN: {}\n Time: {}".format(msg,datetime.now())
            identity = os.environ.get("USER")
            self.sender.sendMail(content=msg,subject="HIGH TEMPERATURE ON: {}".format(identity))

    def reboot(self, msg: str, *args):
        super().reboot(msg, *args)
        log.warn("HIGH TEMPERATURE REBOOT LEVEL!!! Rebooting...")
        try:
            os.system("sudo reboot")
        except:
            log.error("REBOOT FAILED!!!")