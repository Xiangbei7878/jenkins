from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# 配置 Linux 容器专用 Chrome 启动参数
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

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://automationintesting.online/")
driver.maximize_window()
wait=WebDriverWait(driver,10)    #初始化等待对象，driver 最大等待秒数
#格式 wait.until(EC.条件( (定位方式,定位值) ))
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Admin"))).click()
wait.until(EC.element_to_be_clickable((By.ID,"username"))).send_keys("admin")
driver.find_element(By.ID,"password").send_keys("password")
driver.find_element(By.ID,value="doLogin").click()
time.sleep(3)

driver.find_element(By.ID,value="frontPageLink").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/section[2]/div/div[2]/div[2]/div/div[3]/a").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,300)")
time.sleep(3)
# driver.find_element(by=By.ID,value="doReservation").click()
wait.until(EC.element_to_be_clickable((By.ID,"doReservation"))).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-300)")
time.sleep(3)
driver.find_element(By.NAME,"firstname").send_keys("bob")
driver.find_element(By.NAME,"lastname").send_keys("baby")
driver.find_element(By.NAME,"email").send_keys("12234567@qq.com")
driver.find_element(By.NAME,"phone").send_keys("13954035861")
driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary.w-100.mb-3").click()
driver.find_element(By.LINK_TEXT,"Admin").click()
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Messages").click()
input(...)
#学到了实在不行用XPATh,Class只能用一个class定位，value name就是NAME，复合类可以用css，中间用 . 连接,要连接全部,如果文本会变就用PARTIAL_LINK_TEXT

