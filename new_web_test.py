from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager

# ===================== 容器专用 Chrome 配置（优化加载）=====================
chrome_options = Options()
# 无头模式（无界面运行，容器必备）
chrome_options.add_argument("--headless=new")
# 容器必备：绕过沙箱限制
chrome_options.add_argument("--no-sandbox")
# 容器必备：解决/dev/shm内存不足导致崩溃
chrome_options.add_argument("--disable-dev-shm-usage")
# 解决 DevToolsActivePort 报错的核心参数
chrome_options.add_argument("--remote-debugging-port=9222")
# 禁用GPU加速（容器无显卡，必加）
chrome_options.add_argument("--disable-gpu")
# 禁用扩展，避免干扰
chrome_options.add_argument("--disable-extensions")
# 禁用弹窗，避免阻塞
chrome_options.add_argument("--disable-popup-blocking")
# 禁用沙箱相关安全限制，容器必加
chrome_options.add_argument("--disable-setuid-sandbox")
# 指定用户数据目录，避免权限问题
chrome_options.add_argument(f"--user-data-dir=/tmp/chrome_profile_{os.getpid()}")
# 优化页面加载，无头模式必加
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--no-cache")
# 窗口大小固定，避免元素定位偏移
chrome_options.add_argument("--window-size=1920,1080")

# 用 webdriver-manager 自动下载匹配驱动
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ===================== 优化后的测试逻辑（解决超时）=====================
# 页面加载超时设置，避免无限等待
driver.set_page_load_timeout(30)
driver.get("https://automationintesting.online/")

# 先等待页面完全加载，再操作元素
time.sleep(5)
# 延长等待时间到20秒，适配无头模式加载速度
wait = WebDriverWait(driver, 20)

# 显式等待Admin元素，确保可点击
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
# 等待用户名输入框加载完成
wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("admin")
# 等待密码输入框加载完成
wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("password")
# 等待登录按钮可点击
wait.until(EC.element_to_be_clickable((By.ID, "doLogin"))).click()
time.sleep(3)

# 等待首页链接可点击
wait.until(EC.element_to_be_clickable((By.ID, "frontPageLink"))).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(3)
# 等待预约入口元素加载
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section[2]/div/div[2]/div[2]/div/div[3]/a"))).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,300)")
time.sleep(3)

# 等待预约按钮可点击
wait.until(EC.element_to_be_clickable((By.ID, "doReservation"))).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-300)")
time.sleep(3)

# 等待表单元素加载
wait.until(EC.element_to_be_clickable((By.NAME, "firstname"))).send_keys("bob")
wait.until(EC.element_to_be_clickable((By.NAME, "lastname"))).send_keys("baby")
wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("12234567@qq.com")
wait.until(EC.element_to_be_clickable((By.NAME, "phone"))).send_keys("13954035861")
# 等待提交按钮可点击
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.w-100.mb-3"))).click()

# 等待Admin链接可点击
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
time.sleep(5)
# 等待Messages链接可点击
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Messages"))).click()

# 最后关闭浏览器
time.sleep(3)
driver.quit()
