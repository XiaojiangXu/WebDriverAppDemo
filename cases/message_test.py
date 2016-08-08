#coding:utf-8
import os
import HTMLTestRunner
import unittest
from selenium import webdriver
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):    
    def test_(self):    
        desired_caps = {}
        desired_caps['deviceName'] = 'Android Emulator'  #adb devices查到的设备名
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'        
        desired_caps['appPackage'] = 'com.duowan.mobile'  #被测App的包名
        desired_caps['appActivity'] = 'com.yy.mobile.ui.splash.SplashActivity' #启动时的Activity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        el = driver.find_element_by_name(u"广场")
        self.assertIsNotNone(el)
        el.click()        
        yueBang = driver.find_element_by_name(u"关注")
        self.assertIsNotNone(yueBang)
        yueBang.click()        
        driver.quit()
    
if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中    
    filename="./myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试