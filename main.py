from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://aleph.bcucluj.ro:8991/F/?func=option-update-lng&file_name=find-b&F2=pc-latin&P_CON_LNG=RUM")


def auth():
    auth_btn = driver.find_element(by=By.LINK_TEXT, value='Autentificare')
    auth_btn.click()

    barcode = driver.find_element(by=By.NAME, value='bor_id')
    barcode.send_keys("BCU202405533")

    parola = driver.find_element(by=By.NAME, value='bor_verification')
    parola.send_keys("BCU202405533")

    conectare_btn = driver.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr[4]/td/input')
    conectare_btn.click()


def get_loc(i) -> str:
    xpath = "/html/body/p[2]/table[1]/tbody/tr["
    xpath += str(i)
    xpath += "]/td[2]"
    return xpath

def reserve(i):
    rezerva = driver.find_element(by=By.XPATH, value=f"/html/body/p[2]/table[1]/tbody/tr[{i}]/td[1]/a")
    rezerva.click()
    confirm = driver.find_element(by=By.XPATH, value="/html/body/form/table/tbody/tr[6]/td/input")
    confirm.click()
    finalizare = driver.find_element(by=By.XPATH, value="/html/body/form/table/tbody/tr[5]/td/input")
    finalizare.click()

auth()

locuri_lnk = driver.find_element(by=By.LINK_TEXT, value='Locuri')
locuri_lnk.click()

driver.implicitly_wait(0.5)

# /html/body/p[2]/table[2]/tbody/tr/th[2]/a
# /html/body/p[2]/table[2]/tbody/tr/th[2]/a
# /html/body/p[2]/table[2]/tbody/tr/th[2]/a
pag = 1
while pag != 5:

    print("pagina", pag)

    i = 2
    while i != 102:
        loc_xpath = get_loc(i)
        loc = driver.find_element(by=By.XPATH, value=loc_xpath)
        loc_int = int(loc.text[3:])

        if loc_int == 316:
            break

        if i == 23: # placeholder - aici vine logica daca locul e cu priza
            reserve(i)

        print(loc_int)
        i += 1

    try:
        pagina_urm = driver.find_element(by=By.XPATH, value="/html/body/table[8]/tbody/tr/th[2]/a")
        pagina_urm.click()
        pag += 1
    except NoSuchElementException:
        break

# print(loc.text)

# pagina 1 -----------------
# /html/body/p[2]/table[1]/tbody/tr[2]/td[1]/a
# /html/body/p[2]/table[1]/tbody/tr[2]/td[2]
# /html/body/p[2]/table[1]/tbody/tr[3]/td[1]/a

# /html/body/p[2]/table[1]/tbody/tr[2]/td[1]/a

# /html/body/p[2]/table[1]/tbody/tr[101]/td[1]/a
# /html/body/p[2]/table[1]/tbody/tr[101]/td[2]

# pagina 2 -----------------
# /html/body/p[2]/table[1]/tbody/tr[101]/td[2]

# pagina 3 ----------------
# /html/body/p[2]/table[1]/tbody/tr[101]/td[2]

# pagina 4 ---------------
# /html/body/p[2]/table[1]/tbody/tr[39]/td[2]

driver.quit()
