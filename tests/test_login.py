from pages.auth_page import AuthPage
from settings import BASE_URL, DIFFERENT_URL, tel, bel_tel, pwd, inv_mail, oversize_login, recovery
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By



def test_login(driver):
    page = AuthPage(driver)
    page.login_user(tel, pwd)
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div[2]/div[1]/div[2]/div[1]/div/span[2]/span")))

def test_user_from_Belarus(driver):
    page = AuthPage(driver)
    page.login_user_from_Belarus(bel_tel, pwd)
    assert EC.invisibility_of_element_located(
        (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]'))
    WDW(driver, timeout=3).until(EC.invisibility_of_element_located(
        (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')))

def test_invalid_mail(driver):
    page = AuthPage(driver)
    page.login_user(inv_mail, pwd)
    # driver.save_screenshot("reg1.png")
    wrong_login = driver.find_element(By.ID, "form-error-message").text
    assert "Неверный логин или пароль" in wrong_login

def test_remember_login(driver):
    page = AuthPage(driver)
    page.login_user(tel, pwd)
    driver.get(DIFFERENT_URL)
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    user_page = driver.find_element(By.XPATH, "//*[@id='app']/main/div/div[2]/div[1]/div[2]/div[1]/div/span[2]/span").text
    assert tel in user_page
    

def test_logout(driver):
    page = AuthPage(driver)
    remember_btn = driver.find_element(By.XPATH, "//*[@class='rt-checkbox__label']")
    remember_btn.click()
    page.login_user(tel, pwd)
    logout_btn = driver.find_element(By.ID, "logout-btn")
    logout_btn.click()
    atuth_main_page = driver.find_element(By.XPATH, "//*[text()='Авторизация']").text
    assert 'Авторизация' in atuth_main_page

def test_name_empty_field(driver):
    page = AuthPage(driver)
    page.login_user('','')
    driver.save_screenshot("login_name_empty.png")
    allert_empty_fields = driver.find_element(By.XPATH, "//*[text()='Введите номер телефона']").text
    assert "Введите номер телефона" in allert_empty_fields

def test_help(driver):
    page = AuthPage(driver)
    page.help_menu()
    WDW(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="faq-modal__content"]')))

def test_empty_telephone_num(driver):
    page = AuthPage(driver)
    page.empty_tel()
    message = driver.find_element(By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/span").text
    assert "Введите номер телефона" in message

def test_wrong_telephone_num(driver):
    page = AuthPage(driver)
    page.wrong_tel("1319")
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span').text
    assert "Неверный формат телефона" in message

def test_captcha(driver):
    page = AuthPage(driver)
    page.empty_tel()
    WDW(driver, timeout=3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '*[alt="Captcha"]')))

def test_forgot_password(driver):
    page = AuthPage(driver)
    page.wrong_tel(tel)
    mail_choice_btn = page.driver.find_element(By.XPATH, '//*[@class="rt-radio__label"]')
    mail_choice_btn.click()
    WDW(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, '//*[class="card-container__title"]')))
    field_num_recovery = driver.find_element(By.ID, 'id="rt-code-0"')
    field_num_recovery.send_keys(recovery)

def test_max_char(driver):
    page = AuthPage(driver)
    page.login_user(oversize_login, pwd)

