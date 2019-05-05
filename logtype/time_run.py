import datetime
import os
import time
from multiprocessing.dummy import Pool as ThreadPool
import selenium
from selenium import webdriver
import yaml
from PIL import Image
from pyzbar import pyzbar
from selenium.webdriver.chrome.options import Options

def doSth(person):
    # 设定买鞋二维码，修改baidu.png文件名，二维码放在桌面上
    image = "C:\\Users\\admin\\Desktop\\IMG_2362.PNG"
    img = Image.open(image)

    # 识别二维码
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")

    # 读取配置文件
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = curr_dir + os.sep + "env.yaml"
    env = open(filepath, 'r', encoding='utf-8')
    cont = env.read()
    x = yaml.load(cont, Loader=yaml.FullLoader)
    name = x[person]["name"]
    number = x[person]["number"]
    idcard = x[person]["idcard"]
    creditcard = x[person]["creditcard"]
    # print(name,number,idcard,creditcard)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    sel = selenium.webdriver.Chrome(options=options)
    sel.get(barcodeData)

    # 登记操作
    sel.find_element_by_id("q1").send_keys(name)
    sel.find_element_by_id("q2").send_keys(number)
    sel.find_element_by_id("q3").send_keys(idcard)
    sel.find_element_by_id("q4").send_keys(creditcard)
    sel.find_element_by_xpath('//*[@id="ctlNext"]').click()
    print('===========已经登记过啦===========')

def main(h=9, m=0):
    #设定买鞋时间，h表示设定的小时，m为设定的分钟
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m and now.second == 1:
                break
            print("===========未到登记时间===========")
            time.sleep(1)

        #登记人员名单
        items = ['aaa', 'bbb']
        pool = ThreadPool()
        pool.map(doSth, items)
        pool.close()
        pool.join()
        break

main()
