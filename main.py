from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.webdriver.chrome import ChromeOptions


def simple_test():
    platforms = ['WINDOWS', 'MAC', 'LINUX']
    for platform in platforms:
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://localhost:3000")
        a = driver.find_element_by_class_name("App-header").text
        passed = "Test Automation" in a
        print("Test passed") if passed else print("Test failed")
        driver.quit()


if __name__ == "__main__":
    simple_test()
