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
# welcome.gui()

# myApp = App()
# myApp.master.title(welcome.titleScreen())
# myApp.master.maxsize(1000,400)
# myApp.mainloop()
welcome.titleScreen()
user = welcome.introduction()
calculator   = Calculator(user)
# welcome.moreInfo(user)


calculator.whatCalculator()
calculator.outPut()
welcome.anythingElse()

# print(HouseBudget, financed, monthly)


