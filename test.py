from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

'''需要的命令
1. 要是手机 adb devices -l没有反应，则运行
  adb kill-server
  adb start-server
  adb devices -l
2. 需要启动app package
  adb shell dumpsys activity recents | find "intent={"
  cmp=tv.danmaku.bili/.MainActivityV2
  app package: tv.danmaku.bili
3. 需要启动Activity名称
  adb shell dumpsys activity recents | find "intent={"
  cmp=tv.danmaku.bili/.MainActivityV2
  app activity: .MainActivityV2
4. noreset 永远选择true
'''
desired_caps={
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.weaver.custom7', # 启动APP Package名称 
  'appActivity': 'weaver.fw.com.WelcomeActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'    
}
# 连接Appium Server，初始化自动化环境
# 配置信息
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 

# 设置缺省等待时间
driver.implicitly_wait(5)

# # 如果有`青少年保护`界面，点击`我知道了`
# iknow = driver.find_elements(By.ID, "cener_image")
# if iknow:
#     iknow.click()

# # 根据id定位搜索位置框，点击
# driver.find_element(By.ID, 'expand_search').click()

# # 根据id定位搜索输入框，点击
# sbox = driver.find_element(By.ID, 'search_src_text')
# sbox.send_keys('白月黑羽')
# # 输入回车键，确定搜索
# driver.press_keycode(AndroidKey.ENTER)

# # 选择（定位）所有视频标题
# eles = driver.find_elements(By.ID, 'title')

# for ele in eles:
#     # 打印标题
#     print(ele.text)

# input('**** Press to quit..')

driver.find_element(By.ID, 'cener_image').click()
driver.find_element(By.ID,'iv_back').click()
driver.quit()