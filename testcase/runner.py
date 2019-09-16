# -*- coding: utf-8 -*-
# from pytest.testcase.feeds.feeds_slide import FeedsSlide
# from pytest.testcase.feeds.feeds_cover import FeedCover
from pytest.testcase.channel_movie.channel_seconds_open import ChannelSecondsOpen

if __name__ == '__main__':
    # feeds_slide = FeedsSlide()     # 记录上下滑秒开
    # feeds_slide.test_slide(105)

    # feeds_cover = FeedCover()     # 记录从封面进入秒开
    # feeds_cover.test_repeat_cover(105)

    channel = ChannelSecondsOpen()      # 长视频秒开
    channel.test_channel_seconds_open(5)

