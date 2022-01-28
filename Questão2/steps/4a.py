from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys

@given('that the user is logged into the course platform#4')
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

@when('the user clicks on your profile and the option to “edit profile”')
def when(context):
    button_profile = context.driver.find_element_by_id("avatar")
    button_profile.click()

    button_edit = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/button")
    button_edit.click()
    sleep(2)

@step('makes changes to the “marital status” field')
def step(context):
    button_marital = Select(context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[2]/div[2]/div[2]/div[3]/ng-select/div/div/div[3]/input"))
    button_marital.select_by_value("a90975f6d757-5")
    email_field = context.driver.find_element_by_id("email")
    email_field.send_keys(Keys.PAGE_DOWN)

    button_save = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[11]/button")
    button_save.click()

@then('the changes are saved')
def then(context):
    WebDriverWait(context.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"PROFILE.MESSAGESUCCESSDATA")))
