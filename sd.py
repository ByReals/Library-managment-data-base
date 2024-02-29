import csv

def kelimeyi_bul(csv_dosya, anahtar_kelime1, anahtar_kelime2):
    with open(csv_dosya, newline='', encoding='utf-8') as dosya:
        okuyucu = csv.reader(dosya)
        for satir in okuyucu:
            if anahtar_kelime1 in satir and anahtar_kelime2 in satir:
                bulunanlar = satir
    return bulunanlar

# Örnek kullanım:
bulunanlar = kelimeyi_bul("ödÜnç_alınanlar.csv", "456", "511")
print(bulunanlar)
