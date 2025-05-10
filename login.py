from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # --- Buka halaman login ---
    driver.get("https://adminposaja.posindonesia.co.id/development/Login")
    time.sleep(2)  # tunggu render
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.ID, "uLogin"))
    )

    # --- Isi username & password ---
    username_input = driver.find_element(By.ID, "uLogin")
    password_input = driver.find_element(By.ID, "uPassword")

    username_input.send_keys("")
    password_input.send_keys("")
    # code.send_keys("cde3")

    # --- Klik tombol login ---
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
    )
    login_button.click()



    time.sleep(10)

    
    driver.get("https://adminposaja.posindonesia.co.id/development/User")

    time.sleep(5)
    tambah_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary mb-4')]"))
    )
    tambah_button.click()
    time.sleep(5)


    a_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'non')]"))
    )
    a_click.click()
    time.sleep(10)

    iduser_input = driver.find_element(By.ID, "nipposnn")
    nama_input = driver.find_element(By.ID, "namann")

    iduser_input.send_keys("TESTERQA")
    nama_input.send_keys("Agung")

    dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-jabatannn-container")))
    dropdown.click()

    option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'H06 - Admin Pusat')]")))
    option.click()

    pass_input = driver.find_element(By.ID, "passs")
    pass_input.send_keys("AAaa123$")
    Simpan_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'btnSaves')]"))
    )
    Simpan_button.click()

    time.sleep(20)

    # driver.get("https://adminposaja.posindonesia.co.id/development/User")

    # time.sleep(15)
    
    print("Uji AbNormal - Modul login dan Tambah User dengan id user sudah digunakan Berhasil .")



finally:
    driver.quit()
