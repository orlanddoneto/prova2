from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from selenium.webdriver.support.select import Select
from time import sleep


@given('that the user is logged into the course platform')
def given(context):
    context.driver = webdriver.Chrome("C:/Users/Cliente/Documents/chromedriver2/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    sleep(3)
    username_login = context.driver.find_element_by_id("login")
    username_login.send_keys("ORLANDONETOALUNO")

    password_login = context.driver.find_element_by_id("password")
    password_login.send_keys("abcd1234")

    button_login = context.driver.find_element_by_id("login-btn")
    button_login.click()
    sleep(2)

@when('you select the option “My Courses” and choose your course')
def when(context):
    sleep(3)
    button_class = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/nav/ul/div/li[2]/a[1]")
    button_class.click()
    sleep(3)


    chosenCourse_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-courses/app-small-header/div[2]/div/div/button")
    chosenCourse_button.click()
    sleep(2)
@step('choose a lesson')
def step(context):
    sleep(1)
    button_lesson = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-lessons-list/div/app-small-header/div[3]/div[1]/div[1]/div[2]/button")
    button_lesson.click()
    sleep(2)

@then('the user can access the lessons')
def then(context):

    WebDriverWait(context.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"lo-CONTEUDO")))
