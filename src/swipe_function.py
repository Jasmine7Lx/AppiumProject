# 向上滑动
def swipe_up():
    s = driver.get_window_size()
    x1 = s['width'] * 0.5   # x坐标
    y1 = s['height'] * 0.8     # 起点y坐标
    y2 = s['height'] * 0.4     # 终点y坐标
    driver.swipe(x1, y1, x1, y2)


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
