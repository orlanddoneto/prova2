from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('2that the user is logged into the course platform#2')
def given(context):
    context.driver = webdriver.Chrome("C:/Users/Cliente/Documents/chromedriver2/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    sleep(2)
    username_login = context.driver.find_element_by_id("login")
    username_login.send_keys("ORLANDONETOALUNO")

    password_login = context.driver.find_element_by_id("password")
    password_login.send_keys("abcd1234")

    button_login = context.driver.find_element_by_id("login-btn")
    button_login.click()
    sleep(2)

@when('select the “Glossary” option and write the term you want')
def when(context):
    button_glossary = context.driver.find_element_by_id("nav-item-6")
    button_glossary.click()
    sleep(2)

    search_field = context.driver.find_element_by_id("search")
    search_field.send_keys("framework")

    button_search = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-glossary/div/app-small-header/div[2]/div[1]/div/button")
    button_search.click()

@then('information about the chosen word is provided')
def then(context):
    sleep(1)
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/app-sidebar-layout/div/div/app-glossary/div/app-small-header/div[2]/div[5]/h2"),"Framework"))




