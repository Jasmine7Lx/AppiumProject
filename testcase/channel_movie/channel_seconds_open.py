# -*- coding: utf-8 -*-
from pytest.testcase.page.channelpage import ChannelPage
from pytest.testcase.common.common import CommonUse
import time
import csv


class ChannelSecondsOpen(object):
    channelpage = ChannelPage()
    common = CommonUse()

    def get_seconds_data(self):
        data_info = self.channelpage.get_debug_info()
        split_seconds_open = data_info.splitlines()
        sdk_time = (split_seconds_open[5])[26:]
        callback_time = (split_seconds_open[6])[13:]
        print("sdk_time = " + sdk_time, "callback_time = " + callback_time)
        seconds_data_str = sdk_time + ',' + callback_time
        seconds_data_list = seconds_data_str.split(",")
        return seconds_data_list

    def test_channel_seconds_open(self, n):
        filename = "../result/channel_reopen_data-%s.csv" % self.common.get_time()
        with open(filename, "w", newline="") as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(["post_id", "秒开时间"])
            for i in range(n):
                self.channelpage.swipe_left(2)
                self.channelpage.att_channel_entrance()
                self.channelpage.att_channel()
                self.channelpage.channel_movie()
                time.sleep(3)
                seconds_data = self.get_seconds_data()
                wr.writerow(seconds_data)
                print(seconds_data)
                self.channelpage.return_page()
                self.common.delete_cache()
                time.sleep(5)
                self.common.reopen_app()
                time.sleep(1)
