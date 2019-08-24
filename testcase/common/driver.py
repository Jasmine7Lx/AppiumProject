from appium import webdriver
dr = webdriver.Remote


class Driver(object):
    def __init__(self):
        self.desired_caps ={}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '7.0'
        self.desired_caps['deviceName'] = '5200b567eebb549b'
        self.desired_caps['appPackage'] = 'com.imo.android.imoimalpha'
        self.desired_caps['appActivity'] = 'com.imo.android.imoim.activities.Home'
        self.desired_caps['autoAcceptAlerts'] = True
        self.desired_caps['noReset'] = True

    def connect(self):
        url = 'http://127.0.0.1:4723/wd/hub'
        global dr
        dr = webdriver.Remote(url, self.desired_caps)

    def get_driver(self):
        return dr
