# -*- encoding: utf-8 -*-
'''
@File    :   temperMonitor
@Time    :   2022/10/16 17:35:51
@Author  :   victor2022 
@Version :   1.0
@Desc    :   monitor of temperature
'''

import time
import sys
from handlers.propHandler import TemperLoader
from handlers.temperHandler import TemperHandler
from actions.emailAction import EmailAction
from actions.baseAction import BaseAction
from log_helper import log

class TemperMonitor:
    def __init__(self, action: str, peroid = 1):
        self.peroid = peroid
        # temper handler
        self.temperHandler = TemperHandler()
        # load config
        temperLoader = TemperLoader(sys.path[0])
        self.warn = temperLoader.level_warn
        self.reboot = temperLoader.level_reboot
        # set action
        self.action = BaseAction()
        if(not action=="base"):
            if(action=="email"):
                self.action = EmailAction(sys.path[0])
            else:
                log.info("Action name error, use base action!")
    
    def startMonitor(self):
        while(True):
            # get temperature
            temp = self.temperHandler.getCurrentTemp()
            # compare and do actions
            if(temp>=self.warn):
                msg = "The temperature of device ({:.2f}°C) is higher than".format(temp,self.warn)
                # reboot level
                if(temp>=self.reboot):
                    msg = msg+" {:.2f}°C !!!".format(self.reboot)
                    self.action.reboot(msg)
                # warn level
                msg = msg+" {:.2f}°C !!!".format(self.warn) 
                self.action.warn(msg)
            # sleep
            time.sleep(self.peroid)
                