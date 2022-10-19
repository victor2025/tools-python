# -*- encoding: utf-8 -*-
'''
@File    :   tempHandler.py
@Time    :   2022/10/16 00:29:19
@Author  :   victor2022 
@Version :   1.0
@Desc    :   None
'''

class TemperHandler:
    
    __file_name = "/sys/class/thermal/thermal_zone0/temp"
    
    def getCurrentTemp(self):
        with open(TemperHandler.__file_name,'r') as f:
            temp = int(f.read())
            return temp/1000.0