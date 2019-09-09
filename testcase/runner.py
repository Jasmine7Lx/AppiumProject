# -*- coding: utf-8 -*-
from pytest.testcase.feeds.feeds_slide import FeedsSlide
# from pytest.testcase.feeds.feeds_cover import FeedCover

if __name__ == '__main__':
    feeds_slide = FeedsSlide()     # 记录上下滑秒开
    feeds_slide.test_slide(5)

    # feeds_cover = FeedCover()     # 记录上下滑秒开
    # feeds_cover.test_repeat_cover(5)
