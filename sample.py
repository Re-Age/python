# 必要ライブラリimport
# 実行制御------------------------------------------------------------
import time
import os
# selenium関連--------------------------------------------------------
from selenium import webdriver
import chromedriver_binary
# PyAutoGUI-----------------------------------------------------------
import pyautogui as pg
import pyscreeze
import common.pyAutoGuiMovePoint as pagmp

# メインロジック-------------------------------------------------------
if __name__ == "__main__":
    button_position = None
    # Chormeを起動し、Googleホームページを表示
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    driver.set_window_size(945, 1020)
    time.sleep(2)

    # 検索ボックスにテキストを入力
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')

    # 検索ボタン押下
    try:
        time.sleep(2)
        button_position = pagmp.getCenterOnScreen(os.path.join(os.path.dirname(__file__), 'image\GoogleSearch.png'), True, 0.95, 10, 0)
        print(driver.get_window_size())
        time.sleep(2)
        # pg.click(button_position)
        pagmp.clickWithReturn(button_position)
        time.sleep(2)
    except pg.ImageNotFoundException: 
        time.sleep(1)
        print('タイムアウト')
    except IOError:
        print('ファイルが読み込めませんでした。')
    driver.quit()