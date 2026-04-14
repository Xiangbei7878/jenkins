from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager

# ===================== 容器专用 Chrome 配置（绝对不崩溃）=====================
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument(f"--user-data-dir=/tmp/chrome_profile_{os.getpid()}")

# 关键：用 webdriver-manager 自动下载匹配的驱动，彻底解决版本不匹配
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ===================== 你的测试逻辑（完全保留）=====================
driver.get("https://automationintesting.online/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("admin")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "doLogin").click()
time.sleep(3)

driver.find_element(By.ID, "frontPageLink").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/section[2]/div/div[2]/div[2]/div/div[3]/a").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,300)")
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.ID, "doReservation"))).click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,-300)")
time.sleep(3)

driver.find_element(By.NAME, "firstname").send_keys("bob")
driver.find_element(By.NAME, "lastname").send_keys("baby")
driver.find_element(By.NAME, "email").send_keys("12234567@qq.com")
driver.find_element(By.NAME, "phone").send_keys("13954035861")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.w-100.mb-3").click()

driver.find_element(By.LINK_TEXT, "Admin").click()
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "Messages").click()

# 最后关闭浏览器（规范写法）
time.sleep(3)
driver.quit()
