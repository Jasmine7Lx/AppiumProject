# -*- coding: utf-8 -*-
from pytest.testcase.common.base import BaseUse
import pytest.testcase.page.elementConfig as point


class ChannelPage(BaseUse):
    def att_channel_entrance(self):
        # self.find_element(*point.channel['contact_tab']).click()
        self.find_element(*point.channel['att_channel']).click()

    def att_channel(self):
        self.find_element(*point.channel['test_channel_1']).click()

    def channel_movie(self):
        self.find_element(*point.channel['channel_movie']).click()

    def get_debug_info(self):
        debug_info = self.find_element(*point.channel['channel_debug']).text
        return debug_info

    # 向上滑动
    def swipe_up(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.8  # 起点y坐标
        y2 = s['height'] * 0.4  # 终点y坐标
        self.driver.flick(x1, y1, x1, y2)  # flick 甩动；swipe 按住不放再移动

    # 向下滑动
    def swipe_down(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5
        y1 = s['height'] * 0.75
        y2 = s['height'] * 0.25
        self.driver.flick(x1, y1, x1, y2)

    # 向右滑动
    def swipe_right(self):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.25
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.75
        self.driver.flick(x1, y1, x2, y1)

    # 向左滑动
    def swipe_left(self, n=1):
        s = self.driver.get_window_size()
        for i in range(n):
            x1 = s['width'] * 0.9
            y1 = s['height'] * 0.5
            x2 = s['width'] * 0.1
            self.driver.flick(x1, y1, x2, y1)

    # 点击物理返回键
    def return_page(self):
        self.driver.keyevent(4)


