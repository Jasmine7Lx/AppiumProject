# -*- coding: utf-8 -*-
import time
import csv
# from pytest.testcase.common.driver import Driver
from pytest.testcase.page.feedspage import FeedsPage
from pytest.testcase.common.common import CommonUse


class FeedCover(object):
    # driver = Driver().get_driver()
    # print(driver)
    feedspage = FeedsPage()
    common = CommonUse()

    def get_seconds_data(self):
        data_info = self.feedspage.get_debugs_info()
        print(data_info)
        split_seconds_open = data_info.splitlines()
        print(split_seconds_open)
        post_id = (split_seconds_open[1])[8:]
        open_time = (split_seconds_open[7])[14:]
        print(open_time)
        seconds_data_str = '\'' + post_id + ',' + open_time
        seconds_data_list = seconds_data_str.split(",")
        return seconds_data_list

    def test_repeat_cover(self, n):
        filename = "../result/feeds_cover_data-%s.csv" % self.common.get_time()
        with open(filename, "w", newline="") as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(["post_id", "秒开时间"])
            for i in range(n):
                self.feedspage.feeds_entrance()
                self.feedspage.attention_page()
                self.feedspage.attention_page_video()
                time.sleep(3)
                seconds_data = self.get_seconds_data()
                wr.writerow(seconds_data)
                print(seconds_data)
                self.feedspage.return_page()
                self.common.delete_cache()
                time.sleep(5)
                self.common.reopen_app()
