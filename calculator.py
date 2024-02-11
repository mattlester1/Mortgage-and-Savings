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
calculator   = MortgageCal()

welcome.titleScreen()
user = welcome.introduction()
welcome.moreInfo(user)

HouseBudget = calculator.davesRecommend(user.income, user.downPayment)

print(HouseBudget)

