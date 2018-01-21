from DengLuPage import LoginPage
from myTestCase import MyTestCase


class DengLuTest(MyTestCase):

    def test_login(self):
        loginPage=LoginPage(self.driver)
        loginPage.login("yongwy","123456")

if __name__ == '__main__':
    dic={"123","234"}
    print(*dic)

    # dl=DengLuTest(MyTestCase)
    # dl.test_login()