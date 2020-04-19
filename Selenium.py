from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    time.sleep(1)

    WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_css_selector("[id=\"book\"]")
    button.click()

    button1 = browser.find_element_by_css_selector("[id=\"solve\"]")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button1)
    x_elem = browser.find_element_by_css_selector("[id=\"input_value\"]")
    x = int(x_elem.text)
    y = str(calc(x))
    input1 = browser.find_element_by_css_selector("[id=\"answer\"]")
    input1.send_keys(y)
    # input2 = browser.find_element_by_css_selector("[name=\"lastname\"]")
    # input2.send_keys("last")
    # input3 = browser.find_element_by_css_selector("[name=\"email\"]")
    # input3.send_keys("gfd")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'test.txt')
    # input4 = browser.find_element_by_css_selector("[name=\"file\"]")
    # input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button#solve")
    button.click()


    # input1 = browser.find_element_by_css_selector(".first_block .first")
    # input1.send_keys("Ivan")
    # input3 = browser.find_element_by_css_selector(".first_block .third")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()