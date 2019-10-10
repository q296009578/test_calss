import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import Displaypage

class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = Displaypage(self.driver)
        

    def test_mobile_display_input(self):
        # 点击显示
        self.display_page.click_display()

        # 点击搜索
        self.display_page.click_search()

        # 输入hello
        self.display_page.input_text_search("hello")

        # 点击返回
        self.display_page.click_back()

