from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time

#---Initialize the webdriver
driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")

#---Wait 3 seconds for the page to fully load
sleep(3)

#---Select English language upon startup
language_eng = driver.find_element(By.ID, "langSelect-EN")
language_eng.click()

#---Consent to cookie policy
cookie_consent = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
driver.execute_script("arguments[0].click();", cookie_consent)

#---Wait 3 seconds for the page to fully load
sleep(3)

#---Initialize "Shopping list" of bought products to track amount
product_counts = {}

#---Buy produts function
def buy_products():
    try:
        products_available = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        product = products_available[-1].text.split()[0]
        # Initialize count if product not seen before
        if product not in product_counts:
            product_counts[product] = 0
        # Don't buy more than 5 of any product
        if product_counts[product] < 5:
            products_available[-1].click()
            product_counts[product] += 1
    except Exception:
        pass

#---Buy upgrades
def buy_upgrades():
    try:
        upgrades_available = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        upgrades_available[-1].click()
    except Exception:
        pass

wait = WebDriverWait(driver, 10)

#---Game logic
def game_logic():
    big_cookie = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
    game_timer = time()
    while time() - game_timer <= 300:
        big_cookie.click()
        try:
            buy_products()
            buy_upgrades()
        except Exception:
            pass
    cps_final = driver.find_element(By.ID, "cookiesPerSecond").text
    print(f"Final score after 5 minutes, clicks {cps_final}")

game_logic()

#---Quit
driver.quit()