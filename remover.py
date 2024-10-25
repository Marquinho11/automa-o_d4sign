from selenium import webdriver
from selenium.webdriver.common.by import By
from urls import vault_urls
from time import sleep

driver = webdriver.Chrome()
driver.get("https://secure.d4sign.com.br/login.html?r=/desk/cofres/171414/4ad8ddae-6231-463c-a0eb-f72bf5facc86.html?")

sleep(0.1)
email_user = driver.find_element(By.XPATH, "//input[@id='Email']")
email_user.send_keys('ti@cooperemb.com.br')

password_user = driver.find_element(By.XPATH, "//input[@id='Passwd']")
password_user.send_keys('Cooper@74')

button = driver.find_element(By.XPATH, "//button[@class='btn-control-lg btn block full-width m-b btn_entrar']")
button.click()
sleep(10)
for vault_url in vault_urls:
    driver.get(f"https://secure.d4sign.com.br{vault_url}")
    sleep(1)
    button_op = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-sm btn-outline dropdown-toggle popover-vault-custom']")
    button_op.click()

    link_compart = driver.find_element(By.XPATH, "//a[contains(@href, \"eModalO('/desk/shareCofre\")]")
    link_compart.click()
    sleep(2)
    percorre_caixa = driver.find_element(By.XPATH, "//div[@class='col-lg-12']")
    elementos = driver.find_element(By.XPATH, '//tr')
    print(elementos)
    
