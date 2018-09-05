#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time, datetime
import schedule
from random import randint

def clock_in_job():
    print('Running job')
    print("Running job time: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    randNum = randint(1, 300)
    print('Randomly wait for ' + (str)(randNum) + ' seconds')
    time.sleep(randNum)
    # open browser
    driver = webdriver.Chrome(executable_path="./chromedriver")
    # get to "url_for_clock_in_automatically" website
    driver.get("url_for_clock_in_automatically")
    # similar to jQuery
    # use tag name, class, id to grab the element and manipulate it
    elem_dept = driver.find_element_by_id('dept_input')
    elem_dept.send_keys("Earth")
    elem_name = driver.find_element_by_id('username_input')
    elem_name.send_keys("shawn")
    elem_pwd = driver.find_element_by_id('password_input')
    elem_pwd.send_keys("geek")
    time.sleep(5)
    btn = driver.find_element_by_id('login-button')
    btn.click()
    clock = driver.find_elements_by_css_selector('div.clock_btn_block .row .col-xs-6')
    for clock_content in clock:
        if clock_content.text.strip() == '上班':
            clock_content.click()
            print('Clock in!!!')
            print("Clock in time: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(5)
    # close the browser
    driver.close()
    print("Browser close time: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# add the clock_in_job to the schedule
schedule.every().monday.at("8:00").do(clock_in_job)
schedule.every().tuesday.at("8:00").do(clock_in_job)
schedule.every().wednesday.at("8:00").do(clock_in_job)
schedule.every().thursday.at("8:00").do(clock_in_job)
schedule.every().friday.at("8:00").do(clock_in_job)
# schedule.every().day.at("8:00").do(clock_in_job)
print('Auto Start!')
while True:
    schedule.run_pending()