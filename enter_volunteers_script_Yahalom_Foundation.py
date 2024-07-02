import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions as ec
import time
import xlwt
import re
from xlwt import Workbook
import openpyxl
import pandas as pd

Yahalom_url = 'https://yahalomfoundation.com/yahalom-member/'

wb = Workbook()
sheet1 = wb.add_sheet('Sheet1')

def set_volunteer_data(url, min_row, max_row):
    ### opening the browser
    src = requests.get(url)
    plain_text = src.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)

    ### getting the excell data using PANDAS
    df = pd.read_excel('excellVolunteers.xlsx')
    done = pd.read_excel

    ### inserting all the data from the excell to the page
    try:
        for row in range(min_row, max_row):
            ### finding the fields in the page
            first_name_field = driver.find_element(By.ID, 'billing_first_name')
            sec_name_field = driver.find_element(By.ID, 'billing_last_name')
            password_field = driver.find_element(By.ID, 'reg_password')
            phone_field = driver.find_element(By.ID, 'billing_phone')
            email_field = driver.find_element(By.ID, 'reg_email')
            register_button = driver.find_element(By.NAME, 'register')

            ### detting the data from the excel
            volunteer_first_name = df.iloc[row,1]
            volunteer_sec_name = df.iloc[row, 2]
            volunteer_email = df.iloc[row, 3]
            volunteer_phone = df.iloc[row, 4]
            volunteer_password = df.iloc[row, 5]

            ### entering the data to the website
            first_name_field.clear()
            first_name_field.send_keys(volunteer_first_name)
            sheet1.write(row,1,volunteer_first_name)
            sec_name_field.clear()
            sec_name_field.send_keys(volunteer_sec_name)
            sheet1.write(row, 2, volunteer_sec_name)
            email_field.clear()
            email_field.send_keys(volunteer_email)
            sheet1.write(row, 3, volunteer_email)
            phone_field.clear()
            phone_field.send_keys(volunteer_phone)
            sheet1.write(row, 4, volunteer_phone)
            password_field.clear()
            password_field.send_keys(volunteer_password)
            sheet1.write(row, 5, volunteer_password)

            ## submitting
            time.sleep(1)
            register_button.click()
            time.sleep(1)
            driver.get(url)
            time.sleep(1)
    finally:
        #saving to the excel
        wb.save('done volunteers.xls')


## testing the function
set_volunteer_data(Yahalom_url,0,100)





