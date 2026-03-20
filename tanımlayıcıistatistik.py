import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bilim_kurgu_kitaplari.csv")

df.columns = df.columns.str.strip()

numeric_columns = ["Okumak İsteyenler", "Şu Anda Okuyanlar", "Okumuş Olanlar", "Sayfa Sayısı"]
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.dropna(subset=numeric_columns)

istatistikler = []

for column in numeric_columns:
    ortalama = df[column].mean()
    medyan = df[column].median()
    mod = df[column].mode()[0] if not df[column].mode().empty else None
    std_sapma = df[column].std()
    varyans = df[column].var()
    istatistikler.append({
        "Sütun": column,
        "Ortalama": ortalama,
        "Medyan": medyan,
        "Mod": mod,
        "Standart Sapma": std_sapma,
        "Varyans": varyans
    })

istatistikler_df = pd.DataFrame(istatistikler)

istatistikler_df.to_csv("istatistikler.csv", index=False)

for column in numeric_columns:
    plt.figure()
    plt.hist(df[column], bins=20, alpha=0.7, edgecolor="black")
    plt.title(f"{column} Dağılımı")
    plt.xlabel(column)
    plt.ylabel("Frekans")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(f"{column}_dagilimi.png")
    plt.show()

print("İstatistikler CSV dosyasına kaydedildi ve sütunlar görselleştirildi.")
