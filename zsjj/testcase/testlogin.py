# coding:utf-8
import ddt
from selenium import webdriver
import unittest
from page.loginpage import LoginPage,login_url
from common.readExcel import ExcelUtil
# testdata1 = {'user':'13068702992','psw':'1111112','exp':u'吴泽敏'}
# testdata2 = {'user':'13068702992','psw':'111112','exp':''}
# data =  [
#         {'user':'13068702992','psw':'1111112','exp':u'吴泽敏'},
#         {'user':'13068702992','psw':'111112','exp':''}
#         ]
data = ExcelUtil("E:\\zsjj\\common\\testdata.xls")
testdata = data.dict_data()
print testdata


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.logindriver=LoginPage(cls.driver)
    def setUp(self):
        self.logindriver.open(login_url)
    def login(self,user,psw,exp):
        self.logindriver.input_user(user) #输入账号
        self.logindriver.input_psw(psw)#输入密码
        self.logindriver.click_log_but()#点击登录
        name_loc = ('id', 'header_username')
        result =self.logindriver.get_text(name_loc)
        print result
        return result==exp
    @ddt.data(*testdata)
    def test_login_success(self,data):
        ''' 登录成功'''
        print data
        result = self.login(**data)
        print result
        print type(result)
        # exp=u'吴泽敏'
        # print type(exp)
        #断言
        self.assertTrue(result)

    # def test_login_fail(self):
    #     ''' 登录失败'''
    #     result=self.login(**testdata2)
    #     # name_loc = ('id', 'header_username')
    #     # text = self.logindriver.get_text(name_loc)
    #     # print text
    #     # print type(text)
    #     # exp = ''
    #     # print type(exp)
    #     # 断言
    #     print result
    #     self.assertTrue(result)
    def tearDown(self):
        self.driver.delete_all_cookies()
if __name__=='__main__':
    unittest.main()