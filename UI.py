#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   UI.py
@Time    :   2024/02/10 07:19:32
@Author  :   Matt Lester 
@Version :   1.0
'''

import numpy as np

class User:
    
    def __init__(self, name, income = 0, savings = 0, downPayment = 0, budget = 0) -> None:
        
        self.name = name
        self.income = income
        self.savings = savings
        self.downPayment = downPayment
        self.selection = 0
        self.budget = budget
        
        
    def getName(self):
        return self.name
    
    def getSavings(self):
        return self.savings
    
    def getIncome(self):
        return self.income
    
    
class MortgageCal:
    
    def __init__(self, interestRate = .05, numYears = 30):
        
        self.interestRate = interestRate
        self.numYears = numYears
        
    def davesRecommend(self, income, downPayment):
        
        one4th = income * .25
        numMonths = self.numYears * 12
        monthInterst = self.interestRate / 12
        
        p = (one4th * (((1 + monthInterst)** numMonths) -1)) / (monthInterst * (1 + monthInterst)** numMonths)
        roundedP = int(p)
        return roundedP
        
    
    
        

class UI:
    
    def __init__(self) -> None:
        pass
    
    def titleScreen(self):
        
        print("""
        WW         WWW         WW    EEEEEEEE    LL         CCCCCCCC     OOOOOOOOO       MMM       MMM     EEEEEEEE
         WW       WW WW       WW     EE          LL         CC           OO     OO       MMMM     MMMM     EE
          WW     WW   WW     WW      EEEEEE      LL         CC           OO     OO       MM  MM MM  MM     EEEEEE 
           WW   WW     WW   WW       EEEEEE      LL         CC           OO     OO       MM   MMM   MM     EEEEEE
            WW WW       WW WW        EE          LL         CC           OO     OO       MM         MM     EE
             WWW         WWW         EEEEEEEE    LLLLLLLL   CCCCCCCC     OOOOOOOOO       MM         MM     EEEEEEEE
            
            
                                                TTTTTTTTTT       OOOOOOOO
                                                    TT           OO    OO
                                                    TT           OO    OO
                                                    TT           OO    OO
                                                    TT           OO    OO
                                                    TT           OOOOOOOO
                                                    
                                                    
                                                    
                         MMM       MMM        AAA       TTTTTTTTTT     TTTTTTTTTTT   ''''   SSSSSSS
                         MMMM     MMMM       AA AA          TT             TT         ''    SSS
                         MM  MM MM  MM      AA   AA         TT             TT               SSSSSSS 
                         MM   MMM   MM     AAAAAAAAA        TT             TT                   SSS
                         MM         MM    AA       AA       TT             TT                    SS   
                         MM         MM   AA         AA      TT             TT               SSSSSSS
                         
                         
                         
            MMM       MMM    OOOOOOOO     RRRRRRRR    TTTTTTTTTT    GGGGGGGG         AAA        GGGGGGGG    EEEEEEEE                
            MMMM     MMMM    OO    OO     RR    RR        TT        GG              AA AA       GG          EE                             
            MM  MM MM  MM    OO    OO     RRRRRRRR        TT        GG             AA   AA      GG          EEEEEE                             
            MM   MMM   MM    OO    OO     RR  RR          TT        GG  GGGG      AAAAAAAAA     GG  GGGG    EEEEEE                                   
            MM         MM    OO    OO     RR   RR         TT        GG    GG     AA       AA    GG    GG    EE                                 
            MM         MM    OOOOOOOO     RR    RR        TT        GGGGGGGG    AA         AA   GGGGGGGG    EEEEEEEE      
            
            
            
    CCCCCCCC       AAA        LL         CCCCCCCC    UU    UU     LL             AAA       TTTTTTTTTT   OOOOOOOO     RRRRRRRR
    CC            AA AA       LL         CC          UU    UU     LL            AA AA          TT       OO    OO     RR    RR
    CC           AA   AA      LL         CC          UU    UU     LL           AA   AA         TT       OO    OO     RRRRRRRR    
    CC          AAAAAAAAA     LL         CC          UU    UU     LL          AAAAAAAAA        TT       OO    OO     RR  RR    
    CC         AA       AA    LL         CC          UU    UU     LL         AA       AA       TT       OO    OO     RR   RR  
    CCCCCCCC  AA         AA   LLLLLLLL   CCCCCCCC    UUUUUUUU     LLLLLLLL  AA         AA      TT       OOOOOOOO     RR    RR              
        """)
        
    def introduction(self):
        
        user = User(input("What is your name: "))
        
        user.selection = input(f"\nHi {user.name} how can we help today? Please select: 1 For mortgage calculator based on Dave's rules, and 2 for Savings goals: ")
        return user
    
    def moreInfo(self, user):
        
        print("Great!! Let's get some more info form you.\n")
        user.income = int(input("\nWhat is you monthly income after taxes? "))
        user.budget = int(input("\nDo you have a house budget? If so, what is that amount? "))
        user.downPayment = int(input("\nDo you plan to put down a down payment? If so, how much? "))
        
                               
        
        