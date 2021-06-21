#----------------------------------------------------------------------
# インポート
#----------------------------------------------------------------------
import pyautogui as pag
import pyscreeze
import random

def getCenterOnScreen(strFileName, booGrayScale, floConfidence, intMoveX, intMoveY):
    """
    指定ファイルを画面上から検索し、画像の中心の座標を取得する。
    座標をランダムにずらす範囲をパラメータで指定する。

    Args:
        strFileName  : 検索ファイル名(フルパス)
        booGrayScale : グレースケール検索の有無
        floConfidence: 検索精度
        intMoveX     : x座標のずらす範囲
        intMoveY     : y座標のずらす範囲

    Returns:
        tuple(x座標, y座標)

    Raises:
        ImageNotFoundException: 指定画像が画面内で検出されない場合
        IOError               : 指定ファイルが開けない場合
    """
    
    tupReturn = None
    tupButtonPosition = None
    intX = 0
    intY = 0

    # 座標取得実行
    try:
        tupButtonPosition = pag.locateCenterOnScreen(strFileName, grayscale = booGrayScale, confidence = floConfidence)
        intX = random.randint(0, intMoveX)
        intY = random.randint(0, intMoveY)        
        tupReturn = (tupButtonPosition[0] + intX, tupButtonPosition[1] + intY)

    except pag.ImageNotFoundException: 
        print('画像が検出されませんでした。')

    except IOError:
        print('ファイルが読み込めませんでした。')

    return tupReturn
