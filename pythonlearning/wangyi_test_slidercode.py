import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = '12345667@163.com'
PASSWORD = '123456'
BORDER = 6
INIT_LEFT = 60

url = 'https://dun.163.com/trial/sense'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)



    
def get_geetest_button():
    """
    获取初始验证按钮
    :return:
                 
    """
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="yidun_intelli-tips"]')))
    return button



def get_screenshot():
    """
    获取网页截图
    :return: 截图对象
    """
    screenshot = browser.get_screenshot_as_png()#二进制的
    screenshot = Image.open(BytesIO(screenshot))#打开image
    return screenshot

def get_slider():
    """
    获取滑块
    :return: 滑块对象
    """
    slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
    return slider

def get_position():
    """
    获取验证码位置
    :return: 验证码位置元组
    """
    img = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="yidun_bg-img"]')))
   

    #利用这个类型可以获取

    time.sleep(2)
    location = img.location
    size = img.size
    offset = 100#个别图片位置需要修正，加入修正变量，这里y轴有偏移
    top, bottom, left, right = location['y']-offset, location['y'] + size['height']-offset, location['x'], location['x'] + size['width']
    return (top, bottom, left, right)

def get_geetest_image(name='captcha.png'):
    """
    获取验证码图片
    :return: 图片对象
    """
    #top和bottom是y轴上的两点，left和right是x轴上的亮点
    #左上角(left, top) 右下角（right， bottom）
    top, bottom, left, right = get_position()
    print('验证码位置', top, bottom, left, right)
    screenshot = get_screenshot()
    captcha = screenshot.crop((left, top, right, bottom))#根据坐标裁剪
    captcha.save(name)
    return captcha

def open_web():
    """
    打开网页输入用户名密码
    :return: None
    """

    browser.get(url)
    shfit = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@captcha-type="jigsaw"]')))
    shfit.click()
    # email = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入邮箱"]')))
    # password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    # email.send_keys(EMAIL)
    # time.sleep(2)
    # password.send_keys(PASSWORD)

def get_gap(image1, image2):
    """
    获取缺口偏移量
    :param image1: 不带缺口图片
    :param image2: 带缺口图片
    :return:
    """
    left = 60
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            if not is_pixel_equal(image1, image2, i, j):
                left = i
                return left
    return left

def is_pixel_equal(image1, image2, x, y):
    """
    判断两个像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param x: 位置x
    :param y: 位置y
    :return: 像素是否相同
    """
    # 取两个图片的像素点
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False

def get_track(self, distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track

def move_to_gap(slider, track):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param track: 轨迹
    :return:
    """
    ActionChains(browser).click_and_hold(slider).perform()
    for x in track:
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(browser).release().perform()

def login():
    """
    登录
    :return: None
    """
    submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
    submit.click()
    time.sleep(10)
    print('登录成功')


open_web()
# 点击验证按钮
button = get_geetest_button()
button.click()
# 获取验证码图片
image1 = get_geetest_image('captcha1.png')
# 点按呼出缺口
slider = get_slider()
slider.click()
# 获取带缺口的验证码图片
image2 = get_geetest_image('captcha2.png')
# 获取缺口位置
gap = get_gap(image1, image2)
print('缺口位置', gap)
# 减去缺口位移
gap -= BORDER
# 获取移动轨迹
track = get_track(gap)
print('滑动轨迹', track)
# 拖动滑块
move_to_gap(slider, track)

success = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
print(success)
login()
# 失败后重试






