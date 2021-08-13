# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:15:06 2021

@author: BornaMarkovic
"""

import pyautogui as auto
import time


while auto.position(1806,14):
    auto.moveTo(610, 1053, 1)
    auto.click()
    auto.moveTo(1000, 400, 1)
    auto.scroll(-1000)
    time.sleep(30)
if auto.position(1000, 400):
    auto.moveTo(1806,14, 1)
    auto.click()
    time.sleep(30)
