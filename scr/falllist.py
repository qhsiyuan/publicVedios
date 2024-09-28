import os
os.chdir(os.path.dirname(__file__))

import pickle
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By

'''
dpyl before 0925 xh, me over

'''

# 视频编号加载
with open('../dat/webnum_zzl.pkl', 'rb') as f:
    date = pickle.load(f)
    f.close()

nam = "赵正磊"
num = "22400758"
# dday = datetime.now().day
dday = [25, 24, 23]

# 浏览器配置
print("配置中")
options = webdriver.EdgeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")

driver = webdriver.Edge(options = options)
print("配置完成")

times = 0
for ioi in range(len(date)-33 - 97):
    times = ioi + 97
    print(times)

    # 日期判断
    if times <= 66:
        ri = 25
    elif times <= 148:
        ri = 24
    else:
        ri = 23

    # 获取链接
    driver.get("https://sgmw.feishu.cn/share/base/form/shrcn5b4iogJpEyQePJOqP1rYUb")

    # 填写名字
    time.sleep(2)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldN92pmWR"]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]'
                        ).click()

    # time.sleep(1)
    # driver.find_element(By.XPATH, 
    #                     '//*[@id="magicdomid-10"]/div/span/span'
    #                     ).clear()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="magicdomid-10"]/div/span/span'
                        ).send_keys(nam)

    # 填写工号
    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldt10Z1F7"]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]'
                        ).click()

    # time.sleep(1)
    # driver.find_element(By.XPATH, 
    #                     '//*[@id="magicdomid-20"]/div/span/span'
    #                     ).clear()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="magicdomid-20"]/div/span/span'
                        ).send_keys(num)

    # 选择部门
    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fld5u0MiO4"]/div/div[2]/div/div/div/div/div/div/div'
                        ).click()

    time.sleep(1.5)
    driver.find_element(By.XPATH, 
                        '/html/body/div[1]/div/div[1]/div[3]/div/div[3]/form/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/li[4]'
                        ).click()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldBShb5a0"]/div/div[2]/div/div/div/div/div/div/div'
                        ).click()

    time.sleep(1.5)
    driver.find_element(By.XPATH, 
                        '/html/body/div[1]/div/div[1]/div[3]/div/div[3]/form/div[4]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/li[3]'
                        ).click()

    # 填写日期
    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldV7SY8M1"]/div/div[2]/div/div/div/div/div/div'
                        ).click()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldV7SY8M1"]/div/div[2]/div/div/div/div/div/div/div[1]/span/div/input'
                        ).clear()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldV7SY8M1"]/div/div[2]/div/div/div/div/div/div/div[1]/span/div/input'
                        ).send_keys("9-" + str(ri))

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="mainBox"]/div/div[1]/div[3]/div/div[1]'
                        ).click()

    # 选择平台
    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldOZ3IKOR"]/div/div[2]/div/div/div/div/div/div/div'
                        ).click()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldOZ3IKOR"]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/li[1]'
                        ).click()

    # 填写链接
    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="field-item-fldn6x1Tot"]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]'
                        ).click()

    # time.sleep(1)
    # driver.find_element(By.XPATH, 
    #                     '//*[@id="magicdomid-30"]/div/span'
    #                     ).clear()

    time.sleep(1)
    driver.find_element(By.XPATH, 
                        '//*[@id="magicdomid-30"]/div/span'
                        ).send_keys("# 宝骏云海 # 宝骏云海万人交车 # 新车上市 ... https://www.douyin.com/video/" + date[times-1])
    print("# 宝骏云海 # 宝骏云海万人交车 # 新车上市 ... https://www.douyin.com/video/" + date[times-1])

    # 提交
    time.sleep(1.5)
    driver.find_element(By.XPATH, 
                        '//*[@id="mainBox"]/div/div[1]/div[3]/div/div[3]/form/div[8]/div/div/div/button/span'
                        ).click()
    
    time.sleep(3)
