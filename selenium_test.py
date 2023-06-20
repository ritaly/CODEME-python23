from selenium import webdriver
from selenium.webdriver.common.by import By


def przegladanie_wydarzen(lokalizacja, temat):
    # Inicjalizacja przeglądarki
    driver = webdriver.Chrome()  # Wymaga zainstalowania przeglądarki Chrome oraz ChromeDriver

    # Otwarcie strony Meetup.com
    driver.get("https://www.meetup.com")

    # Wyszukiwanie wydarzeń w określonej lokalizacji i na podstawie tematu
    lokalizacja_input = driver.find_element(By.ID, "locationInput")
    lokalizacja_input.clear()
    lokalizacja_input.send_keys(lokalizacja)

    temat_input = driver.find_element(By.ID, "topicInput")
    temat_input.clear()
    temat_input.send_keys(temat)

    szukaj_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Szukaj')]")
    szukaj_button.click()

    # Przeglądanie wyników
    wydarzenia = driver.find_elements(By.XPATH, "//div[@class='eventCard eventCard--hasPhoto']")

    for wydarzenie in wydarzenia:
        nazwa = wydarzenie.find_element(By.XPATH, ".//h3/a").text
        data = wydarzenie.find_element(By.XPATH, ".//time").get_attribute("datetime")
        miejsce = wydarzenie.find_element(By.XPATH, ".//address").text

        print("Nazwa: ", nazwa)
        print("Data: ", data)
        print("Miejsce: ", miejsce)
        print("--------------------")

    # Zamknięcie przeglądarki
    driver.quit()

# Przykładowe użycie funkcji przegladanie_wydarzen
lokalizacja = "Warszawa"
temat = "Python"

przegladanie_wydarzen(lokalizacja, temat)
