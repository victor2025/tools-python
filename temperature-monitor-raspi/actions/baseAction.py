# -*- encoding: utf-8 -*-
'''
@File    :   actions.py
@Time    :   2022/10/16 17:00:45
@Author  :   victor2022 
@Version :   1.0
@Desc    :   Base actions while temperature is too high
'''

from log_helper import log

class BaseAction:
    
    def warn(self, msg:str,*args):
        log.warn(msg)
        
    def reboot(self, msg:str, *args):
        log.warn(msg)