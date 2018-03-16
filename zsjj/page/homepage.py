# coding:utf-8
from selenium import webdriver
from common.base import BasePage

homepage_url='https://direct.cmfchina.com/ECApp/ECHome/applicationGroups.jsp?mainCatId=ACCOUNT_INFO&thirdCatId=ACCOUNT_INFO_HOME'

class HomePage(BasePage):
    name_loc=('id','header_username')
    def click_name_loc(self):
        self.click(self.name_loc)


