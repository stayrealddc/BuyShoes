import datetime
import time
from multiprocessing.dummy import Pool as ThreadPool
# from pathos.multiprocessing import ProcessingPool as newPool
import yaml
from PIL import Image
import pyzbar.pyzbar as pyzbar
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_env():
    '''
        获取人员个人信息
    '''
    # 读取配置文件获取人个信息
    env_fire = open("env.yaml", 'r', encoding='utf-8').read()
    # 解析yaml文件
    env = yaml.load(env_fire, Loader=yaml.FullLoader)
    return env

# 抢鞋登记
def BuyShoe(person):

    '''
        公众号截取二维码放置项目目录中
        参数png表示二维码截图文件名称
    '''
    img = Image.open('baidu.png')
    # img.show()
    # 解析图片，识别二维码
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        url = barcode.data.decode("utf-8")
    # 登记人员信息
    env = get_env()
    # options = Options()
    # options.add_argument('--headless')
    # sel = selenium.webdriver.Chrome(options=options)
    # sel.get(url)
    name = env[person]["name"]
    number = env[person]["number"]
    idcard = env[person]["idcard"]
    creditcard = env[person]["creditcard"]
    print(name, number, idcard, creditcard)

    # 元素定位模拟登记
    # sel.find_element_by_id("q1").send_keys(name)
    # sel.find_element_by_id("q2").send_keys(number)
    # sel.find_element_by_id("q3").send_keys(idcard)
    # sel.find_element_by_id("q4").send_keys(creditcard)
    # sel.find_element_by_xpath('//*[@id="ctlNext"]').click()
    print('===========已经登记过啦===========')

def run_time(h,m):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m and now.second == 1:
                break
            print("===========未到登记时间===========")
            time.sleep(1)
        break


if __name__ == "__main__":
    env =get_env()
    # 登记人员列表
    person_list = []
    for i in env.keys():
        person_list.append(i)
    # 设定买鞋时间，h表示设定的小时，m为设定的分钟
    run_time(h=0, m=0)
    # 创建多线程并行登记
    pool = ThreadPool(len(person_list))
    pool.map(BuyShoe, person_list)
    pool.close()
    pool.join()