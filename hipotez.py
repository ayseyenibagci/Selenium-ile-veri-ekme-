import pandas as pd
import numpy as np

df = pd.read_csv("bilim_kurgu_kitaplari.csv")

df.columns = df.columns.str.strip()
df["Okumak İsteyenler"] = pd.to_numeric(df["Okumak İsteyenler"], errors="coerce")
df["Şu Anda Okuyanlar"] = pd.to_numeric(df["Şu Anda Okuyanlar"], errors="coerce")
df["Okumuş Olanlar"] = pd.to_numeric(df["Okumuş Olanlar"], errors="coerce")
df["Sayfa Sayısı"] = pd.to_numeric(df["Sayfa Sayısı"], errors="coerce")

df = df.dropna(subset=["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"])

def t_testi_hesapla(grup1, grup2):
    ort1, ort2 = np.mean(grup1), np.mean(grup2)
    var1, var2 = np.var(grup1, ddof=1), np.var(grup2, ddof=1)
    n1, n2 = len(grup1), len(grup2)
    t_istatistigi = (ort1 - ort2) / np.sqrt(var1 / n1 + var2 / n2)
    return t_istatistigi

t_sonuc = t_testi_hesapla(df["Okumak İsteyenler"], df["Şu Anda Okuyanlar"])
print("t-Testi Sonuçları:")
print(f"t İstatistiği: {t_sonuc}")
print("-" * 18)

df["Kategori"] = ["Kategori 1" if x % 2 == 0 else "Kategori 2" for x in range(len(df))]
cizelge = pd.crosstab(df["Kategori"], df["Okumuş Olanlar"] > df["Okumuş Olanlar"].mean())
ki_kare_istatistigi = np.sum((cizelge - cizelge.mean(axis=0))**2 / cizelge.mean(axis=0))
print("Ki-Kare Testi Sonuçları:")
print(f"Ki-Kare İstatistiği: {ki_kare_istatistigi}")
print("-" * 18)

df["Sayfa Sayısı Gruplar"] = pd.cut(df["Sayfa Sayısı"], bins=3, labels=["Az", "Orta", "Çok"])

def anova_f_hesapla(gruplar):
    genel_ortalama = np.mean([deger for grup in gruplar for deger in grup])
    ss_arasi = sum([len(grup) * (np.mean(grup) - genel_ortalama)**2 for grup in gruplar])
    ss_ici = sum([sum((deger - np.mean(grup))**2 for deger in grup) for grup in gruplar])
    df_arasi = len(gruplar) - 1
    df_ici = sum([len(grup) for grup in gruplar]) - len(gruplar)
    f_istatistigi = (ss_arasi / df_arasi) / (ss_ici / df_ici)
    return f_istatistigi

anova_gruplar = [grup["Okumuş Olanlar"].dropna() for ad, grup in df.groupby("Sayfa Sayısı Gruplar", observed=True)]
f_sonuc = anova_f_hesapla(anova_gruplar)
print("ANOVA Sonuçları:")
print(f"F İstatistiği: {f_sonuc}")
print("-" * 18)

