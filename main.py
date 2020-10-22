from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.webdriver.chrome import ChromeOptions
from selenium.webdriver.common.by import By


def simple_test():
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://localhost:3000")
    a = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/code").text
    passed = "Test Automation" in a
    print("Test passed") if passed else print("Test failed")
    driver.quit()


if __name__ == "__main__":
    simple_test()
