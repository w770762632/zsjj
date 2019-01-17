# coding:utf-8
from selenium import webdriver
from common.base import BasePage

login_url='https://direct.******.com/ECService/ECLogin/login.jsp'
class LoginPage(BasePage):
    user_loc=('id','loginNo')
    psw_loc=('xpath','.//div[@class="loginContTwoBox"]/input[2]')
    log_but=('id','loginBtn')
    reg_but=('link text','免费注册')
    forpsw_but=('link text','忘记密码')
    def input_user(self,user):
        #输入用户名
        self.send_keys(self.user_loc,user)
    def input_psw(self,psw):
        #输入密码框
        self.driver.find_element('xpath', './/div[@class="loginContTwoBox"]/input[2]').send_keys(psw)
        #self.send_keys(self.psw_loc,psw)
    def click_log_but(self):
        self.click(self.log_but)
if __name__=="__main__":
    driver=webdriver.Firefox()
    a=LoginPage(driver)
    a.open("https://direct.******.com/ECService/ECLogin/login.jsp")
    a.input_user('**********')
    a.input_psw('********')
    a.click_log_but()

