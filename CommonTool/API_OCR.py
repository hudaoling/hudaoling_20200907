from aip import AipOcr
from PIL import Image
import  pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


"""验证码识别基本步骤:
1.预处理
2.灰度化
3.二值化
4.去噪
5.分割
6.识别
"""

#  你的 APPID AK SK
APP_ID = '19840503'
API_KEY = '2XcrBQsUD8TfZs8NgqLx9uqa'
SECRET_KEY = 'akVf2vFg90pz0ZBXmqQ9OixG5HbspTxK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return  fp.read()



# 定义参数变量
options = {
    # 定义图像方向
        'detect_direction' : 'true',
    # 识别语言类型，默认为'CHN_ENG'中英文混合
        'language_type' : 'ENG',
}


#pytesseract处理图片
def make_picture(filePath):
    image = Image.open(filePath)
    # 传入'L'将图片转化为灰度图像
    image = image.convert('L')

    # 传入'1'将图片进行二值化处理
    threshold = 150
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()
    image.save(filePath+"edit_"+name)




if __name__ == '__main__':


   #Google的OCR方法
    filepath='D:/verify_code/'
    name='v2.jpg'

    make_picture(filepath+name)
    gray_image=Image.open(filepath+"edit_"+name)
    gray_image.show()
    code=pytesseract.image_to_string(gray_image)
    print(code)



    #百度OCR调用方法
    baidu_image = get_file_content(filepath+"edit_"+name)

    result = client.basicGeneral(baidu_image,options)

    # 调用通用文字识别接口
    for word in result['words_result']:
        print(word['words'])
