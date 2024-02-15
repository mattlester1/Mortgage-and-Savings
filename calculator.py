#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   calculator.py
@Time    :   2024/02/10 07:30:04
@Author  :   Matt Lester 
@Version :   1.0
'''

from UI import *

welcome = UI()

welcome.titleScreen()
user = welcome.introduction()
calculator   = Calculator(user)


calculator.whatCalculator()
calculator.outPut()
anythingE= welcome.anythingElse()

while anythingE.lower() == "y":
    
    calculator.switchCalculator()
    calculator.outPut()
    anythingE = welcome.anythingElse()
    
exit()



