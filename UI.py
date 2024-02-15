#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   UI.py
@Time    :   2024/02/10 07:19:32
@Author  :   Matt Lester 
@Version :   1.0
'''

import numpy as np
from tkinter import *
# import tkinter as tk
from tkinter import ttk


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
    
    
class Calculator:
    
    def __init__(self, user, interestRate = .0435, numYears = 15):
        
        self.interestRate = interestRate
        self.numYears = numYears
        self.user = user
        self.houseBudget = 0
        self.financed = 0
        self.monthly = 0
        self.savingsGoal = 0
        self.savingsMonths = 0
        self.initialDeposit = 0
        self.monthlyAmount = 0
        
    def moreInfo(self):
    
        print("\nGreat!! I can help you calculate how much house you can afford. Let's get some more info form you.\n")
    
        self.user.income = int(input("\nWhat is you monthly income after taxes? "))
        self.user.downPayment = int(input("\nDo you plan to put down a down payment? If so, how much? "))
             
            
    def savingsGoalInfo(self):
        
        print("\nGreat! Lets get a little more info from you so we can determine how much you need to save each month to reach your goal.\n")
        
        self.savingsGoal = int(input("How much would you like to save? "))
        self.savingsMonths = int(input("How fast do you want to save this amount? Please enter a number of months: "))
        self.initialDeposit =int(input("Do you have a initial deposit? Please enter a numerical value: ")) 
        
        
    def whatCalculator(self):
        
        if self.user.selection == 1:
            self.moreInfo()
            return self.davesRecommend()

        else:
            self.savingsGoalInfo()
            return self.savingsCalculator()
        
        
    def switchCalculator(self):
        
        if self.user.selection == 1: self.user.selection = 2 
            
        else: self.user.selection = 1
        
        
        if self.user.selection == 1:
           
           self.moreInfo()
           return self.davesRecommend()

        else:
            self.savingsGoalInfo()
            return self.savingsCalculator()
            
            
        
    def davesRecommend(self):
        
        one4th = self.user.income * .25
        numMonths = self.numYears * 12
        monthInterst = self.interestRate / 12
        
        p = (one4th * (((1 + monthInterst)** numMonths) -1)) / (monthInterst * (1 + monthInterst)** numMonths)
        self.financed = int(p)
        
        total = p + self.user.downPayment
        self.houseBudget = int(total)
        
        monthPay = (monthInterst * p * (1 + monthInterst)**numMonths) / (((1 + monthInterst)**numMonths)-1)
        self.monthly = int(monthPay)
        
        
    def savingsCalculator(self):
        
        
        monthlyIR = self.interestRate / 12
        self.monthlyAmount = ((((self.savingsGoal - self.initialDeposit * (1 + monthlyIR)** self.savingsMonths))) * monthlyIR) / ((1+ monthlyIR)** self.savingsMonths - 1)
        self.monthlyAmount = int(self.monthlyAmount)
        
        return self.monthlyAmount
        
    def outPut(self):
        
        
        if self.user.selection == 1:
            
            print(f"""Based on what you have given: 
            You can afford a {self.houseBudget} house.
            This includes your {self.user.downPayment} down payment and a financed amount of {self.financed}.
            This leads to a monthly payment of {self.monthly}, which is 25% of your take home pay.""")
        
        else:
            
            print(f"\nIn order to reach your savings goal of {self.savingsGoal} in {self.savingsMonths} months (at an annual interest rate of 4.35%) you need to contribute")
            print(f"{self.monthlyAmount} each month.")
    
        

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
        
        user.selection = int(input(f"\nHi {user.name} how can we help today? Please select: 1 For mortgage calculator based on Dave's rules, and 2 for Savings goals: "))
        
 

        while True:    
            
            try:
                if user.selection != 1 and user.selection != 2:
                    raise ValueError("Please enter either 1 or 2: ")
                else:
                    break
            

            except ValueError as e:
                user.selection = int(input(e))
                if user.selection == 1 or user.selection == 2:
                    break
                
                
                

        return user
    
    def anythingElse(self):
        
        
        return input("Is there anything else? Y or N: ")
    
