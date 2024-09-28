import os
os.chdir(os.path.dirname(__file__))

from selenium import webdriver
import pathlib
import time
import vedPublisher

# 基本信息
# 视频存放路径
print("路径查找中")
catalog_mp4 = r"D:\VScode\project\Python\publicVedios\n28ved"

# 视频标题
vedtitle0 = "宝骏云海新车上市，万人交车！第"
# 视频描述
# describe = "9月10日宝骏云海上市, 发布会三小时后突破6000个订单, 现已万人交车!  #宝骏云海 #宝骏云海万人交车 #新车上市 #国产之光"
# describeks = "9月10日宝骏云海上市, 发布会三小时后突破6000个订单, 现已万人交车!  #宝骏云海 #宝骏云海万人交车 #新车上市 #国产之光"
describedy = [
    "宝骏云海:宝骏品牌主流线的全新力作，标志着宝骏品牌回归主流市场!以高智能、长续航为核心亮点，满足用户对于智驾、颜值、续航的需求。", 
    "宝骏云海定位“智能长续航SUV”,是一款拥有超长续航、全系标配高阶智驾的新能源双动力SUV,是宝骏品牌进军主流市场的重磅新品。", 
    "宝骏云海不仅具有卓越的性能，更承载着宝骏品牌不懈创新、勇往直前的精神！（现已上市）",
    "宝骏云海，“直挂云帆济沧海”，如同云中之帆，拥有长风破浪的勇气和力量，将驾驭者带向广阔无垠的沧海。",
    "9月10日宝骏云海上市, 发布会三小时后突破6000个订单, 现已万人交车!",
]
# time.sleep(1)
options = webdriver.EdgeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")

time.sleep(1)
print("配置中")
driver = webdriver.Edge(options = options)
print("配置完成")

path = pathlib.Path(catalog_mp4)

# 视频地址获取 使用第一个.mp4文件
path_mp4 = []
for i in path.iterdir():
    if(".mp4" in str(i)):
        path_mp4.append(str(i))

print(path_mp4)

if(len(path_mp4) != 0):
    print("检查到视频路径：")
else:
    print("未检查到视频路径，程序终止！")
    exit()

print(len(path_mp4))
# exit()

vedtitle1 = [
    "宝骏云海:采用巴斯夫车漆，一线豪华品牌同款。(",
    "宝骏云海:不断优化智驾体验,让用户因智驾而愉悦。(",
    "宝骏云海现已推出：超影灰、玉辉白、腾云蓝、逐日橙(",
    "宝骏首款智能长续航SUV:宝骏云海,宛如腾云的骏马！(",
    "宝骏云海:拥有全新高阶智驾功能,交付即可用!(",
    "宝骏云海:动感优雅完美融合,像骏马俯冲，更年轻更运动(",
    "宝骏云海:满足智驾、颜值、续航、品质的用车需求!(",
]

num = 0
for ioi in range(len(path_mp4)):
    num = ioi + 1
    path_mp4_i = "D:\VScode\project\Python\publicVedios/n28ved/new_vedio_" + str(num) + ".mp4"
    
    # vedtitle = vedtitle0 + " " + str(num) + "篇。 # 宝骏云海 # 宝骏云海万人交车"
    # vpub = vedPublisher.VedPublisher(driver, describe, vedtitle, path_mp4_i)
    # vpub.publish_bilibili()
    # vedtitle = vedtitle1[joj+2]
    # describeks = vedtitle1[joj+2] + " " + str(num) + " 篇。 #宝骏云海 #宝骏云海万人交车 #新车上市 #国产之光"
    # vks = vedPublisher.VedPublisher(driver, describeks, vedtitle, path_mp4_i)
    # vks.publish_kuaishou()
    vedtitle = vedtitle1[ioi//10] + str(ioi%10+1) + ")"
    vks = vedPublisher.VedPublisher(driver, describedy[ioi//14], vedtitle, path_mp4_i)
    vks.publish_douyin()
    time.sleep(5)
