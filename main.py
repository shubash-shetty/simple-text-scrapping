from selenium import webdriver


def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://en.wikipedia.org/wiki/Subhas_Chandra_Bose")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value = "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[5]")
  return element.text

print(main())
