# -*- coding: utf-8 -*-
from pytest.testcase.common.base import BaseUse
import pytest.testcase.page.elementConfig as point
import time


class FeedsPage(BaseUse):
    def feeds_entrance(self):
        self.find_element(*point.feeds['entrance']).click()

    def attention_page(self):
        self.find_element(*point.feeds['att_tap']).click()
        time.sleep(1)
        self.find_element(*point.feeds['att_name']).click()         # Jas的关注人

    def attention_page_video(self):
        self.find_element(*point.feeds['att_first_video']).click()

    def hot_video(self):
        self.find_element(*point.feeds['hot_first_video']).click()

    def click_debug_info(self):  # 点击debug面板
        self.find_element(*point.feeds['debug']).click()

    def get_debugs_info(self):
        debug_info = self.find_element(*point.feeds['debug_info']).text
        return debug_info

    # 向上滑动
    def swipe_up(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.8  # 起点y坐标
        y2 = s['height'] * 0.4  # 终点y坐标
        self.driver.flick(x1, y1, x1, y2)       # flick 甩动；swipe 按住不放再移动

    # 向下滑动
    def swipe_down(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5
        y1 = s['height'] * 0.75
        y2 = s['height'] * 0.25
        self.driver.swipe(x1, y1, x1, y2)

    # 向右滑动
    def swipe_right(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.25
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.75
        self.driver.swipe(x1, y1, x2, y1)

    # 向左滑动
    def swipe_left(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.9
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.1
        self.driver.swipe(x1, y1, x2, y1)

    # 点击物理返回键
    def return_page(self):
        self.driver.keyevent(4)


