import pytest
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys

# EXPECTED_NUM_OF_BTTNS = 10

# def test_verify_title(driver, pass_url):
#         driver.get(pass_url)
#         driver.find_elements(By.XPATH, "//a[text()='Gift Cards']")[0].click()
#         expected_title = "Barnes & Noble Gift Cards and eGift Cards | Barnes & Noble®"
#         title = driver.title
#         assert title == expected_title, f"Expected title: {expected_title} is not matching actual: {title}"


# def test_verify_num_of_bttns_in_nav_panel(driver, pass_url):
#         driver.get(pass_url)
#         nav_panel_bttns = driver.find_elements(By.XPATH, "//div[@id='navbarSupportedContent']//ul[@class='navbar-nav rhf-navbar-nav booksNav mobile-hide']//a[@class='rhf-nav-link nav-link rhf_border_right']")
#         assert len(nav_panel_bttns) == EXPECTED_NUM_OF_BTTNS, f"Expected number of buttons: {EXPECTED_NUM_OF_BTTNS} is not matching actual: {len(nav_panel_bttns)}"


# def just_to_try():
#     chrome_options = Options()
#     # chrome_options.add_argument('--headless')
#     chrome_options.add_experimental_option(name="detach", value=True)  # Chrome browser will not be closed when the ChromeDriver object is destroyed
#     chrome_options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get("https://www.barnesandnoble.com/")
#     navigation_bar_bttns = driver.find_elements(By.XPATH, "//div[@id='navbarSupportedContent']//ul[@class='navbar-nav rhf-navbar-nav booksNav mobile-hide']//a[@class='rhf-nav-link nav-link rhf_border_right']")
#     for bttn in navigation_bar_bttns:
#         print(bttn.text)
#     print(len(navigation_bar_bttns))
#     driver.close()
#     print("Browser is closed.")
#     driver.quit()
#     print("Driver is quited.")

# just_to_try()

def test_1():
    a = 1
    b = 2
    assert a == b, f"'{a}' is not equal to '{b}'."

def test_2():
    a = 1
    b = 2
    assert a != b, f"'{a}' is equal to '{b}'."

def test_3():
    a = 1
    b = 2
    assert a < b, f"'{a}' higher than '{b}'."