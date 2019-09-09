from selenium.webdriver.support.ui import WebDriverWait
import datetime
import os


class CommonUse(object):
    # # 获取时间戳
    # def get_time(self):
    #     tamp = int(time.time())
    #     return tamp

    def get_time(self):
        now = datetime.datetime.now()
        ftime = now.strftime("%Hh%Mm%Ss")
        return ftime

    # 获取屏幕截图
    def get_screenshot(self):
        screen_time = self.get_time()
        filename = '../wrong_screenshot/%s.png' % screen_time
        self.driver.get_screenshot_as_file(filename)

    # 显示等待
    def wait(self, t, ele):
        WebDriverWait(self.driver, t, 1).until(lambda driver: ele)

    # 删除缓存
    def delete_cache(self):
        os.system('adb shell rm -r /sdcard/nerv-cache2/*')
        print('成功删除nerv-cache2')
        os.system('adb shell rm -r sdcard/Android/data/com.imo.android.imoimalpha/cache/*')
        print('成功删除imo-cache')
