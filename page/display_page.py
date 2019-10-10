from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Displaypage(BaseAction):
    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    #     self.driver = driver

    # 点击显示
    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)
    # 点击搜索
    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)
    # 输入文字
    def input_text_search(self, text):
    #     # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
    #     self.find_element(self.input_text_view,text).click()
        self.input(self.input_text_view, text)
    # 点击返回
    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
