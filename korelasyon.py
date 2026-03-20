import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv('bilim_kurgu_kitaplari.csv')  

veri = veri.dropna()  
veri['Zaman'] = pd.to_datetime(veri['Zaman'], errors='coerce').dt.year  

en_cok_okunanlar = veri.sort_values(by='Okumuş Olanlar', ascending=False).head(10)
print("En Çok Okunan Kitaplar:")
print(en_cok_okunanlar[['Kitap Adı', 'Yazar', 'Okumuş Olanlar', 'Yayıncı']])

yayin_siralamasi = veri.groupby('Yayıncı')['Okumuş Olanlar'].sum().sort_values(ascending=False)
print("\nYayıncılara Göre Toplam Okuyan Sayısı:")
print(yayin_siralamasi.head(10))

son_yillar_kitaplari = veri[veri['Zaman'] >= 2020]
print("\n2020 ve Sonrası Yayınlanan Kitaplar:")
print(son_yillar_kitaplari[['Kitap Adı', 'Yazar', 'Zaman']].head(10))

plt.figure(figsize=(10, 6))
veri['Dil'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Dillere Göre Kitap Dağılımı')
plt.xlabel('Dil')
plt.ylabel('Kitap Sayısı')
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(veri['Okumuş Olanlar'], veri['Okumak İsteyenler'], alpha=0.7, color='purple')
plt.title('Okuyanlar ve Okumak İsteyenler İlişkisi')
plt.xlabel('Okumuş Olanlar')
plt.ylabel('Okumak İsteyenler')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(veri['Sayfa Sayısı'], bins=30, alpha=0.7, color='orange', edgecolor='black')
plt.title('Kitapların Sayfa Sayısı Dağılımı')
plt.xlabel('Sayfa Sayısı')
plt.ylabel('Kitap Sayısı')
plt.show()
