import os
import time

import pyzbar.pyzbar as pyzbar
import selenium
from PIL import Image,ImageEnhance
from selenium import webdriver
import yaml

#将二维码文件放到桌面上，替换实际文件名
image = "C:\\Users\\admin\\Desktop\\IMG_2362.PNG"
# image = "C:\\Users\\admin\\Desktop\\baidu.png"
#处理二维码图片
img = Image.open(image)
# img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
# img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
# img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
# img = img.convert('L')#灰度化
#识别二维码
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
#读取配置文件
curr_dir = os.path.dirname(os.path.realpath(__file__))
filepath = curr_dir + os.sep + "randomenv.yaml"
env = open(filepath, 'r', encoding='utf-8')
cont = env.read()
x = yaml.load(cont, Loader=yaml.FullLoader)
sel = selenium.webdriver.Chrome()
for i in 'ddy','zds','yyp','wyb':
    name = x[i]["name"]
    number = x[i]["number"]
    idcard = x[i]["idcard"]
    creditcard = x[i]["creditcard"]
    # print(name,number,idcard,creditcard)
    sel.get(barcodeData)
    time.sleep(1)
    #百度网页测试步骤
    # sel.find_element_by_xpath('//*[@id="kw"]').send_keys(i)
    # time.sleep(2)
    # sel.find_element_by_xpath('//*[@id="su"]').click()
    # time.sleep(2)
    #登记操作
    sel.find_element_by_id("q1").send_keys(name)
    sel.find_element_by_id("q2").send_keys(number)
    sel.find_element_by_id("q3").send_keys(idcard)
    sel.find_element_by_id("q4").send_keys(creditcard)
    time.sleep(1)
    sel.find_element_by_xpath('//*[@id="ctlNext"]').click()
    time.sleep(1)
#关闭浏览器
time.sleep(2)
sel.quit()