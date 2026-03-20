import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bilim_kurgu_kitaplari.csv")

df.columns = df.columns.str.strip()

df["Okumak İsteyenler"] = pd.to_numeric(df["Okumak İsteyenler"], errors="coerce")
df["Şu Anda Okuyanlar"] = pd.to_numeric(df["Şu Anda Okuyanlar"], errors="coerce")
df["Okumuş Olanlar"] = pd.to_numeric(df["Okumuş Olanlar"], errors="coerce")
df["Sayfa Sayısı"] = pd.to_numeric(df["Sayfa Sayısı"], errors="coerce")

df = df.dropna(subset=["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"])

df.hist(column=["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"], bins=10 , figsize=(12, 8))
plt.suptitle("Veri Dağılımı - Histogramlar", fontsize=16)
plt.savefig("tum_histogramlar.png")  
plt.show()

df[["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"]].plot(kind="box", figsize=(10, 6))
plt.title("Kutu Grafikleri (Box Plot)")
plt.savefig("tum_kutu_grafigi.png")  
plt.show()

sayisal_sutunlar = ["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"]

for x_sutun in sayisal_sutunlar:
    for y_sutun in sayisal_sutunlar:
        if x_sutun != y_sutun: 
            plt.figure(figsize=(8, 6))
            plt.scatter(df[x_sutun], df[y_sutun], alpha=0.7, edgecolor='k')
            plt.title(f"{x_sutun} vs {y_sutun}", fontsize=14)
            plt.xlabel(x_sutun)
            plt.ylabel(y_sutun)
            plt.savefig(f"scatter_plot_{x_sutun}_vs_{y_sutun}.png")  
            plt.show()

ortalama_veriler = {
    "Şu Anda Okuyanlar": df["Şu Anda Okuyanlar"].mean(),
    "Okumuş Olanlar": df["Okumuş Olanlar"].mean(),
    "Okumak İsteyenler": df["Okumak İsteyenler"].mean(),
    "Sayfa Sayısı": df["Sayfa Sayısı"].mean()
}

plt.bar(ortalama_veriler.keys(), ortalama_veriler.values(), color=['skyblue', 'orange', 'green', 'purple'])
plt.title("Şu Anda Okuyanlar, Okumuş Olanlar, Okumak İsteyenler ve Sayfa Sayısı Ortalamaları", fontsize=14)
plt.ylabel("Ortalama Değer")
plt.xticks(rotation=45)
plt.savefig("tum_bar_chart.png")  
plt.show()

print("Tüm grafikler tamamlandı ve kaydedildi.")


