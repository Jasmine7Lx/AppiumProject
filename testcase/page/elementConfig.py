# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

system = {
    "access": (By.XPATH, "//*[@text='允许']")
}
login = {
    'phone_number': (By.ID, "com.imo.android.imoimalpha:id/phone"),
    'login_button': (By.ID, "com.imo.android.imoimalpha:id/get_started_button")
}
homepage = {
    "chat_list": {
        'chat_list_container': (By.ID, "com.imo.android.imoimalpha:id/chats_list"),
        'chat': (By.CLASS_NAME, "android.widget.LinearLayout")
    }
}
feeds = {
    'entrance': (By.ID, "com.imo.android.imoimalpha:id/tv_title"),
    'att_tap': (By.ID, "com.imo.android.imoimalpha.Trending:id/tab_text"),
    'att_name': (By.ID, "com.imo.android.imoimalpha.Trending:id/tv_nickname"),
    'att_first_video': (By.ID, "com.imo.android.imoimalpha.Trending:id/iv_cover"),
    'hot_first_video': (By.ID, "com.imo.android.imoimalpha.Trending:id/tv_cover_text"),
    'debug': (By.XPATH, "//*[@text='debug']"),
    'debug_info': (By.ID, "com.imo.android.imoimalpha.Trending:id/tv_video_debug_info")
}
channel = {
    'contact_tab': (By.ID, "com.imo.android.imoimalpha:id/tv_tab_text"),
    'att_channel': (By.XPATH, "//*[@text='关注']"),
    'test_channel_1': (By.XPATH, "//*[@text='test_channel_1']"),
    'channel_movie': (By.ID, "com.imo.android.imoimalpha:id/title_tv"),
    'channel_debug': (By.CLASS_NAME, "android.widget.TextView"),
}
