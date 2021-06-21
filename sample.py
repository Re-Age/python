# 必要ライブラリimport
# 実行制御------------------------------------------------------------
import time
import os
#from PIL.ImageOps import grayscale
# selenium関連--------------------------------------------------------
from selenium import webdriver
import chromedriver_binary
# PyAutoGUI-----------------------------------------------------------
import pyautogui as pg
import pyscreeze
import common.pyAutoGuiMovePoint as pagmp
# 画像検索エラーハンドラ
#from pyscreeze import ImageNotFoundException
#pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

# メインロジック-------------------------------------------------------
if __name__ == "__main__":
    button_position = None
    # Chormeを起動し、Googleホームページを表示
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    time.sleep(2)

    # 検索ボックスにテキストを入力
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')

    # 検索ボタン押下
    #search_box.submit()
    try:
        time.sleep(2)
        # button_position = pg.locateCenterOnScreen(os.path.join(os.path.dirname(__file__), 'image\GoogleSearch.png'), grayscale = True, confidence = 0.95)
        button_position = pagmp.getCenterOnScreen(os.path.join(os.path.dirname(__file__), 'image\GoogleSearch.png'), True, 0.95, 10, 0)
        #break
        print(button_position)
        time.sleep(2)
        pg.click(button_position)
        time.sleep(2)
    except pg.ImageNotFoundException: 
        time.sleep(1)
        print('タイムアウト')
        #pg.alert(text='タイムアウト', button='OK')
        #break
    except IOError:
        print('ファイルが読み込めませんでした。')
    driver.quit()