# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBase(object):
    '''
    页面基础类，它封装了所有页面公用的方法
    '''

    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver  # 浏览器驱动
        self.base_url = base_url   # 基本地址
        self.page_title = page_title

    # 通过title断言进入的页面是否正确
    def on_page(self, page_title):
        '''
        打开页面，并且校验页面链接是否加载正确；判断的条件是检查输入的title与获取到的title是否一致
           返回True或False
        '''
        return page_title in self.driver.title

    # 打开页面，并校验页面链接是否加载正确
    def _open(self, url, page_title):  # 下划线表示她不能被外部访问,保证该方法为类私有的方法
        self.driver.get(url)     # 打开浏览器
        # 通过title断言进入的页面是否正确，如果条件不成立，返出断言消息
        assert self.on_page(page_title), u'打开页面失败 %s' % url

    # 定义open方法，调用_open（）进行打开链接
    def open(self):
        self._open(self.base_url, self.page_title)

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*。python存在这种特性，就是将入参放在元组里
            # WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" % (self,loc)

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定位多个元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):  # 再当前窗口，同步执行javascript
        return self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, value, clear_frist, click_frist=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_frist:
                self.find_element(*loc).click()
            if clear_frist:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)