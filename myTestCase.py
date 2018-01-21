#把 setup方法和teardown方法,从测试用例类中分离出来

#以后创建测试用例类时,就不需要重新写setUp和tearDown方法

#原来的测试用例类继承了unittest.TestCase这个类,所以需要重写setUp和tearDown方法

#我们自己写一个类也继承uniitest.Testase类,并且重写setUp和tearDown方法
#以后所有的测试用例类只需要继承这个我们定义的这个类

import  unittest

import time
from selenium import webdriver

#导包快捷键 alt+enter
class MyTestCase(unittest.TestCase):
    # 3.重写父类的setUp和tearDown方法
    # setUp==beforeMethod, tearDown=afterMethod
    # setup方法和setupClass方法的区别
    # setup是每次测试用例都要重新执行一遍
    # setup--->登录--->teardown--->setUp---->修改会员信息--->teardown
    # setupclass是在类中所有测试用例之前只执行一遍
    # setUPClass--->登录--->修改会员信息---->tearDownClass
    # 测试用例之间的执行顺序是按照字母的顺序执行的,denglu是d开头,那么就比member_update是m开头的先执行
    @classmethod
    def setUpClass(self):
        print("这个方法类似于java中的beforeMethod")
        self.driver = webdriver.Chrome()
        # 隐式等待的
        # 优点: 会自动判断网页是否加载好, 一旦网页加载好, 就会执行下面的语句
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("这个方法类似于java中的afterMethod")
        time.sleep(15)
        self.driver.quit()

    # 4.声明一个测试用例方法, 需要以test作为方法名的开头
    def test_member_updating(self):
        print("这是一个测试用例方法, 这个方法用于修改会员信息的测试")
        driver = self.driver
        # 1.账号设置
        driver.find_element_by_link_text("账号设置").click()
        # 2.个人资料
        driver.find_element_by_partial_link_text("个人资料").click()
        # 3.修改具体信息
        # xpath中//表示相对路径
        # * 表示任意元素
        # []表示属性
        # @id id属性
        # driver.find_element_by_xpath("//*[@id=\"true_name\"]")
        # xpath的缺点: 定位速度很慢
        #  cssSelector优点: 快, 定位简单,准确
        driver.find_element_by_css_selector("#true_name").clear()
        driver.find_element_by_css_selector("#true_name").send_keys("张三")
        # 在css selector的定位方式中, 想用什么属性定位都可以, 只需要在两边加上一对中括号
        driver.find_element_by_css_selector("[value=\"2\"]").click()
        # selenium不能删除页面元素的属性, 只能通过javascript来实现
        # document.getElementById("date").removeAttribute("readonly")
        driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("1970-11-12")
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys("24325346")
        # 4.保存
        # css 中id属性前面加井号#
        # class 属性前面加小数点
        # 其他属性就加一对中括号
        driver.find_element_by_css_selector(".btn4").click()
        # 对弹出窗的操作
        # 在处理弹出框操作前,一定要加一个固定锝时间等待
        time.sleep(3)
        driver.switch_to.alert.accept()

        # driver.switch_to.alert.dismiss()

    def test_denglu(self):
        print("这是登录的测试用例")
        driver = self.driver
        # 1. 打开登录页面
        # http://localhost/index.php?m=user&c=public&a=login
        # 接口测试: 请求最重要的一个请求方式get, url地址, 有了这两部分,就可以构造请求,接收响应了
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 2. 输入用户名
        # 分为两部分, 找到用户名输入框, 对输入框输入文字
        # 元素的定位顺序: id---> name----> class
        driver.find_element_by_id("username").send_keys("yongwy")
        # 接下来手工主测一个账号, 写代码实现输入用户名和密码,点击登录按钮
        # 3.输入密码
        driver.find_element_by_name("password").send_keys("123456")
        # 4.点击登录
        driver.find_element_by_class_name("login_btn").click()

