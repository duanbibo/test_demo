from appium import webdriver
from time import sleep
desired_caps = {
                'platformName': 'Android',
                'deviceName': '30d4e606',
                'platformVersion': '4.4.2',
                # apk包名
                'appPackage': 'com.taobao.taobao',
                # apk的launcherActivity
                'appActivity': 'com.taobao.tao.welcome.Welcome'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

if __name__ == "__main__":
    print(driver.get_window_size())
    sleep(5)
    swipLeft(driver, n=2)
    sleep(2)
    swipRight(driver, n=2)