from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys


@given('that the user is logged into the course platform#3')
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

@when('the user selects the “Internal Mail” option')
def when(context):
    button_email = context.driver.find_element_by_id("nav-item-3")
    button_email.click()
    sleep(2)

    button_message = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[1]/app-intern-mail-tabs/ul/li[3]/div")
    button_message.click()
    sleep(2)

@step('fill in the necessary fields to send a message')
def step(context):
    num = randint(1,100)
    from_message = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/app-shorcuts-contacts/div/div[3]/div[1]/span")
    from_message.click()

    message_subject = context.driver.find_element_by_id("messageSubject")
    message_subject.send_keys(Keys.PAGE_DOWN)
    message_subject.send_keys(f"teste{num}")

    text_message = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-intern-mail/div[2]/app-new-intern-message/div/form/div/div[3]/div/app-text-editor/div/form/div[1]/div/div[2]/div[3]/div[2]")
    text_message.send_keys(f"message{num}")
    text_message.send_keys(Keys.PAGE_DOWN)

    button_send = context.driver.find_element_by_id("btn-send")
    button_send.click()

@then('a new message is sent')
def then(context):
    WebDriverWait(context.driver,10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div/app-alert/div/div/div[1]/span[2]"),"Email enviado com sucesso!"))