from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

driver.get("https://openlibrary.org/")
wait = WebDriverWait(driver, 20)

try:
    bilimkurgu_filmleri = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='slick-slide91']/a/div/img")))
    driver.execute_script("arguments[0].scrollIntoView();", bilimkurgu_filmleri)
    bilimkurgu_filmleri.click()

    tüm_bilimkurgu_kitapları = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='coversCount']/strong/span/a")))
    driver.execute_script("arguments[0].scrollIntoView();", tüm_bilimkurgu_kitapları)
    tüm_bilimkurgu_kitapları.click()
except Exception as e:
    print(f"Sayfa veya eleman yüklenemedi: {e}")
    driver.quit()

kitap_verileri = []
sayfa_sayisi = 1

while sayfa_sayisi <= 55: 
    try:
        print(f"{sayfa_sayisi}. sayfa işleniyor...")
        kitap_listesi = driver.find_elements(By.XPATH, "//*[@id='searchResults']/ul/li")
        toplam_kitap = len(kitap_listesi)
        print(f"Sayfa {sayfa_sayisi}: {toplam_kitap} kitap bulundu.")

        for i in range(1, toplam_kitap + 1):
            kitap_xpath = f"//*[@id='searchResults']/ul/li[{i}]/div/div[1]/div/h3/a"
            try:
                kitap = driver.find_element(By.XPATH, kitap_xpath)
                driver.execute_script("arguments[0].scrollIntoView();", kitap)
                driver.execute_script("arguments[0].click();", kitap) 

                try:
                    kitap_adi = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[2]/span/h1"))).text.strip()
                except:
                    kitap_adi = "Kitap adı yok"

                try:
                    yazar = driver.find_element(By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[2]/span/h2").text.strip()
                except:
                    yazar = "Yazar bilgisi yok"

                try:
                    okumak_isteyenler_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[2]/span/ul/li[2]/span[1]")))
                    okumak_isteyenler = okumak_isteyenler_element.text.strip()
                except:
                    okumak_isteyenler = "0"

                try:
                    su_anda_okuyanlar_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[2]/span/ul/li[3]/span[1]")))
                    su_anda_okuyanlar = su_anda_okuyanlar_element.text.strip()
                except:
                    su_anda_okuyanlar = "0"

                try:
                    okumus_olanlar_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[2]/span/ul/li[4]/span[1]")))
                    okumus_olanlar = okumus_olanlar_element.text.strip()
                except:
                    okumus_olanlar = "0"
                    
                try:
                    zaman = driver.find_element(By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[5]/div/div[1]").text.strip().replace("Publish Date\n", "")
                except:
                    zaman = "Zaman bilgisi yok"

                try:
                    dil = driver.find_element(By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[5]/div/div[3]").text.strip().replace("Dil\n", "")
                except:
                    dil = "Dil bilgisi yok"

                try:
                    sayfa_sayisi_kitap = driver.find_element(By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[5]/div/div[4]").text.strip().replace("Pages\n", "")
                except:
                    sayfa_sayisi_kitap = "Sayfa sayısı bilgisi yok"

                try:
                    yayinci = driver.find_element(By.XPATH, "//*[@id='contentBody']/div[1]/div[3]/div[5]/div/div[2]").text.strip().replace("Yayıncı\n", "")
                except:
                    yayinci = "Yayıncı bilgisi yok"

                kitap_verileri.append({
                    "Kitap Adı": kitap_adi,
                    "Yazar": yazar,
                    "Okumak İsteyenler": int(okumak_isteyenler.replace(",", "")),
                    "Şu Anda Okuyanlar": int(su_anda_okuyanlar.replace(",", "")),
                    "Okumuş Olanlar": int(okumus_olanlar.replace(",", "")),
                    "Zaman": zaman,
                    "Dil": dil,
                    "Sayfa Sayısı": sayfa_sayisi_kitap,
                    "Yayıncı": yayinci
                })

                print(f"{i}. kitap işlendi.")

                driver.back()  
                time.sleep(1)

            except Exception as e:
                print(f"{i}. kitap işlenirken hata oluştu: {e}")
                continue

        try:
            ileri_xpath = f"//*[@id='searchResults']/div[2]/a[last()]"
            ileri_button = wait.until(EC.element_to_be_clickable((By.XPATH, ileri_xpath)))
            driver.execute_script("arguments[0].scrollIntoView();", ileri_button)
            ileri_button.click()
            time.sleep(2) 
            sayfa_sayisi += 1

        except Exception as e:
            print(f"Sonraki sayfa yüklenemedi: {e}")
            break

    except Exception as e:
        print(f"Hata oluştu: {e}")
        break

df = pd.DataFrame(kitap_verileri)

output_file = "bilim_kurgu_kitaplari.csv"
df.to_csv(output_file, index=False, encoding="utf-8")
driver.quit()

print(f"CSV dosyası '{output_file}' olarak kaydedildi.")
print("Toplam kitap sayısı:", len(kitap_verileri))