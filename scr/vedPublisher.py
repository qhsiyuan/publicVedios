
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pyautogui

class VedPublisher:

    def __init__(self, driver, describe, vedtitle, path_mp4):
        self.driver = driver
        self.describe = describe
        self.path_mp4 = path_mp4
        self.vedtitle = vedtitle

    def publish_bilibili(self):
        '''
        作用: 发布b站视频
        '''
        
        # 进入创作者页面，并上传视频
        self.driver.get("https://member.bilibili.com/platform/upload/video/frame?spm_id_from=333.1007.top_bar.upload")
        time.sleep(5)
        self.driver.find_element(By.XPATH, 
                            '//*[@id="video-up-app"]/div[1]/div[2]/div/div[1]/div/div/div/div[2]').click()
        print(self.path_mp4)
        self.driver.find_element(By.XPATH, '//input[@type="file" and contains(@accept,"mp4")]').send_keys(self.path_mp4)
        
        # 等待视频上传完成
        while True:
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, '//*[text()="上传完成"]')
                break
            except Exception as e:
                print("视频还在上传中···")
        
        print("视频已上传完成！")
        
        
        time.sleep(5)
        # 输入标题
        self.driver.find_element(By.XPATH, 
                                 '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/input').clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[2]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/input').send_keys(
                                     self.vedtitle)

        # 选择分类
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[contains(@class,"select-item-cont")]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[2]/div/div[2]/div[1]/div[11]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@class="item-main" and text()="购车攻略"]').click()
        
        # 选择标签
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys("宝骏云海")
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys("宝骏云海万人交车")
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys("新车上市")
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys("国产之光")
        self.driver.find_element(By.XPATH, '//input[@placeholder="按回车键Enter创建标签"]').send_keys(Keys.ENTER)
        time.sleep(1)
        
        # 输入描述
        self.driver.find_element(By.XPATH, '//*[@editor_id="desc_at_editor"]//br').send_keys(self.describe)
        
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[8]/div/div[2]/div').click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH, '').click()

        # 刚开始可以先注释掉发布，人工进行检查内容是否有问题
        time.sleep(1)
        # 点击发布
        self.driver.find_element(By.XPATH, 
                            '/html/body/div/div[3]/div[4]/div[2]/div/div/div/micro-app/micro-app-body/div[1]/div[2]/div[1]/div[2]/div[17]/div/div').click()
        

    def publish_kuaishou(self):
        '''
        作用: 发布快手视频
        '''
        
        # 进入创作者页面，并上传视频
        self.driver.get("https://cp.kuaishou.com/article/publish/video?origin=www.kuaishou.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH, 
                            '//*[@id="joyride-wrapper"]/section/div[2]/div[1]').click()
        print(self.path_mp4)
        self.driver.find_element(By.XPATH, '//input[@type="file" and contains(@accept,"mp4")]').send_keys(self.path_mp4)
        
        # 等待视频上传完成
        while True:
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, '//*[text()="上传成功"]')
                break
            except Exception as e:
                print("视频还在上传中···")
        
        print("视频已上传完成！")
        
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="joyride-wrapper"]/div[4]/div[2]/div[4]/div[2]/div[4]/div/div[1]/div').send_keys(
                                     self.describe)

        # 刚开始可以先注释掉发布，人工进行检查内容是否有问题
        time.sleep(3)
        # 点击发布
        self.driver.find_element(By.XPATH, 
                            '//*[@id="joyride-wrapper"]/div[4]/div[2]/div[4]/div[2]/div[13]/button[1]').click()
        

    def publish_douyin(self):
        '''
        作用: 发布抖音视频
        '''
        
        # 进入创作者页面，并上传视频
        self.driver.get("https://creator.douyin.com/creator-micro/content/upload?enter_from=dou_web")

        time.sleep(7)
        self.driver.find_element(By.XPATH, 
                            '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div[1]').click()
        
        time.sleep(1)
        print(self.path_mp4)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div[1]/input'
                                 ).send_keys(self.path_mp4)
        
        time.sleep(0.5)
        pyautogui.keyDown('esc')    # 按下
        time.sleep(0.1)
        pyautogui.keyUp('esc')   # 释放
        
        Keys.ESCAPE
        
        # 等待视频上传完成
        while True:
            time.sleep(2)
            try:
                self.driver.find_element(By.XPATH, '//*[text()="作品描述"]')
                break
            except Exception as e:
                print("视频还在上传中···")
        
        print("视频已上传完成！")
        
        # 输入title
        time.sleep(5)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/input'
                                 ).click()
        
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/input').send_keys(
                                     self.vedtitle)
        
        # 输入describe
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).click()
        
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/span'
                                 ).clear()
        
        # 添加话题
        # #宝骏云海 #宝骏云海万人交车 #新车上市 #国产之光
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(" ")
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys("#宝骏云海")
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys("#宝骏云海万人交车")
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys("#新车上市")
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys("#国产车之光")
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(Keys.SPACE)
        
        time.sleep(1)
        self.driver.find_element(By.XPATH, 
                                 '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div'
                                 ).send_keys(self.describe)
        
        # 刚开始可以先注释掉发布，人工进行检查内容是否有问题
        time.sleep(1)
        # 点击发布
        self.driver.find_element(By.XPATH, 
                            '//*[@id="root"]/div/div/div[2]/div[1]/div[15]/button[1]').click()
        
    