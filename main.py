import pyautogui
import keyboard
import time
import pyocr
from PIL import Image, ImageEnhance
import cv2

def get_position():
    print("Enterキーを押して開始地点の座標を取得")
    while True:
        if keyboard.is_pressed('Enter'):  # 'q'キーが押されているかチェック
            print("開始地点の座標取得します")
            break

    start = str(pyautogui.position())

    time.sleep(1.5)

    print("Enterキーを押して終了地点の座標を取得")
    while True:
        if keyboard.is_pressed('Enter'):  # 'q'キーが押されているかチェック
            print("終了地点の座標取得します")
            break

    end = str(pyautogui.position())

    f = open('position.txt', 'w')
    f.write(start.replace('Point(x=', '').replace('y=', '').rstrip(")") + ", ")
    f.write(end.replace('Point(x=', '').replace('y=', '').rstrip(")"))

def screenshot():
    f = open('position.txt', 'r')
    data = f.read()
    f.close

    x1, y1, x2, y2 = map(int, data.split(","))
    img2 = pyautogui.screenshot('image.png', region=(x1, y1, x2-x1, y2-y1))

def auto_typing():
    pyocr.tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    tools = pyocr.get_available_tools()
    tool = tools[0]
    builder = pyocr.builders.TextBuilder(tesseract_layout=1)
    """
    img = Image.open('image.png')
    #画像処理
    
    img_g = img.convert('L') #Gray変換
    enhancer= ImageEnhance.Contrast(img_g) #コントラストを上げる
    img_con = enhancer.enhance(2.0) #コントラストを上げる
    """

    im = cv2.imread('./image.png')
    th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./opencv_th.png', im_th)

    #処理した画像を開く
    img_con = Image.open('opencv_th.png')

    #画像からOCRで日本語を読んで、文字列として取り出す
    txt_pyocr = tool.image_to_string(img_con , lang='eng', builder=builder)
    txt_pyocr = txt_pyocr.replace(' ', '')

    print(txt_pyocr)
    pyautogui.typewrite(txt_pyocr)


#get_position()

while True:
    screenshot()
    auto_typing()