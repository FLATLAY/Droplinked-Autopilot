import logger
from logger import get_colored_text
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

def check_cart(driver,expected_cart):
    subtotal = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div/div[3]/p[2]").text[1:]
    if (float(subtotal) == float(expected_cart["total_price"])):
        logger.Log.success(f"Cart is {get_colored_text(expected_cart['total_price'], logger.bcolors.BOLD)} as expected!")
    else:
        logger.Log.error(f"Cart is {get_colored_text(subtotal, logger.bcolors.BOLD)} but expected {get_colored_text(expected_cart['total_price'], logger.bcolors.BOLD)}")
    
def change_url(driver,url):
    try:
        driver.get(url)
        logger.Log.success(f"Changed Url to {get_colored_text(url, logger.bcolors.BOLD)}")
    except:
        logger.Log.error(f"Couldn't change Url to {get_colored_text(url, logger.bcolors.BOLD)}, timedout.")

def type_text(driver,value):
    xpath = value["xpath"]
    text = value["text"]
    try:
        driver.find_element(by=By.XPATH, value=xpath).send_keys(text)
        logger.Log.success(f"Typed {get_colored_text(text, logger.bcolors.BOLD)} in {get_colored_text(xpath, logger.bcolors.BOLD)}")
    except:
        logger.Log.error(f"Couldn't type {get_colored_text(text, logger.bcolors.BOLD)} in {get_colored_text(xpath, logger.bcolors.BOLD)}")

def click(driver : WebDriver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath).click()
    except:
        logger.Log.error(f"Couldn't click on {get_colored_text(xpath, logger.bcolors.BOLD)}")

actions_map = {
    "ChangeUrl" : change_url,
    "Click" : click,
    "CheckCart" : check_cart,
    "type" : type_text
}