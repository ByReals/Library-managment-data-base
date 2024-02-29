import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk
import qrcode
import csv
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import pandas as pd
from cryptography.fernet import Fernet
import os
import webbrowser
from tkinter import messagebox
from datetime import datetime



def FG():
    
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Aperture Science")
    new_window.geometry("750x500")
    
    def aperture():
        webbrowser.open("https://combineoverwiki.net/wiki/Aperture_Science")

    srgubutton = tk.Button(new_window,background='#1e1e1e', foreground='white',command=aperture,text="Aperture Science hakkında daha fazla öğren",)
    srgubutton.grid(row=4, column=1, padx=10, pady=10)

    onaybutoonu = tk.Label(new_window, text="Aperture Science, Inc. \nsıklıkla Aperture Science veya kısaca Aperture olarak anılır\n Amerika Birleşik Devletleri merkezli bir bilimsel araştırma şirketidir.\nAna tesisi Yukarı Michigan'da bulunan Zenginleştirme Merkezi'dir ve en az bir başka operasyon üssü Cleveland, Ohio'dadır.\n Başlangıçta Aperture Fixtures adında bir duş perdesi üreticisi olan şirket,\n yarım yüzyıl boyunca gelişerek deneysel bir fizik araştırma kurumuna ve Black Mesa'nın amansız bir rakibine dönüştü.\nAperture Laboratories, Aperture Science dba Aperture Laboratories olarak Aperture'un çoğu ürünü için ticari adı olarak da kullanılmaktadır.\n Aperture Science Innovators, 1947'den[10] 1970'lere kadar kullanılan markaydı.")
    onaybutoonu.grid(row=1, column=1, padx=10, pady=10)
    def eyyo():
        open_new_window()
        
    acilçıkış = tk.Button(new_window,text='Geri',command=eyyo)
    acilçıkış.grid(row=3, column=1, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu,srgubutton] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()



true_passwordd = 'admin123'
true_username = 'admin123'

new_window = None  # global değişken





def kelimeyi_bul(csv_dosya, hedef_kelime):
    with open(csv_dosya, newline='', encoding='utf-8') as dosya:
        okuyucu = csv.reader(dosya)
        for satir in okuyucu:
            if hedef_kelime in satir:
                bulunanlar = satir
                print(bulunanlar)
    return bulunanlar

def kelimeyi_bul2(csv_dosya, anahtar_kelime1, anahtar_kelime2):
    with open(csv_dosya, newline='', encoding='utf-8') as dosya:
        okuyucu = csv.reader(dosya)
        for satir in okuyucu:
            if anahtar_kelime1 in satir and anahtar_kelime2 in satir:
                bulunanlar = satir
    return bulunanlar





def qrkodoku23():
        
        data = None
            
        # Webcam'den görüntüyü almak için VideoCapture nesnesini oluşturun
        cap = cv2.VideoCapture(0)

        while True:
            # Her bir frame için görüntü yakalayın
            ret, frame = cap.read()

            # QR kodunu tespit etmek için decode() fonksiyonunu kullanın
            decoded_objects = decode(frame)

            # Her bir QR kodu için döngü
            for obj in decoded_objects:
                # QR kodunun içeriğini alın
                data = obj.data.decode("utf-8")
                # QR kodunun etrafına bir dikdörtgen çizin
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

                print("QR Code Detected:", data)

            cv2.imshow("QR Code Reader", frame)
            key = cv2.waitKey(1)
            if key == 27:  # Esc tuşuna basarak döngüyü sonlandırın
                break
            elif data is not None:  # QR kodu bulunduğunda döngüyü sonlandırın
                break

        # Kamerayı serbest bırakın ve pencereyi kapatın
        cap.release()
        cv2.destroyAllWindows()
        return data







def qr(kitap_kodu):
    # QR kodunda kodlanacak metni belirtin

    metin = kitap_kodu
    # QR kodunu oluşturun
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

    qr.add_data(metin)
    qr.make(fit=True)

        
    img = qr.make_image(fill_color="black", back_color="white")
    print("başarıyla qr kod oluşturuldu")
    img.save(f"{metin}.png")
    img.show()

    

def deşifreleme():
    

    # Sabit anahtar
    STATIC_KEY = b'YOUR_STATIC_KEY_GOES_HERE' 

    # Anahtarı yükleme
    def load_key():
        if os.path.exists("secret.key"):
            return open("secret.key", "rb").read()
        else:
            return STATIC_KEY

    

    # Dosyayı çözme
    def decrypt_file(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data = f.read()
            decrypted_data = cipher.decrypt(data)
        with open(filename, "wb") as f:
            f.write(decrypted_data)
            print('artıkşifrelideğil')


    def decrypt_file2(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data2 = f.read()
            decrypted_data2 = cipher.decrypt(data2)
        with open(filename, "wb") as f:
            f.write(decrypted_data2)
            print('artıkşifrelideğil')

    def decrypt_file3(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data3 = f.read()
            decrypted_data3 = cipher.decrypt(data3)
        with open(filename, "wb") as f:
            f.write(decrypted_data3)
            print('artıkşifrelideğil')

    # Anahtar üretme
    def generate_key():
        if not os.path.exists("secret.key"):
            with open("secret.key", "wb") as key_file:
                key_file.write(STATIC_KEY)

    # Anahtar üretme
    generate_key()

    # Anahtarı yükleme
    key = load_key()


    
    decrypt_file("kitaplar.csv", key) 
    decrypt_file2("ödÜnç_alınanlar.csv", key) 
    decrypt_file3("getirenler.csv", key)


def şifreleme():
    

    # Sabit anahtar
    STATIC_KEY = b'YOUR_STATIC_KEY_GOES_HERE' 

    # Anahtarı yükleme
    def load_key():
        if os.path.exists("secret.key"):
            return open("secret.key", "rb").read()
        else:
            return STATIC_KEY

    # Dosyayı şifreleme
    def encrypt_file(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data = f.read()
            encrypted_data = cipher.encrypt(data)
        with open(filename, "wb") as f:
            f.write(encrypted_data)
            print('bilgişifrelendi')

    def encrypt_file2(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data = f.read()
            encrypted_data = cipher.encrypt(data)
        with open(filename, "wb") as f:
            f.write(encrypted_data)
            print('bilgişifrelendi')

    def encrypt_file3(filename, key):
        cipher = Fernet(key)
        with open(filename, "rb") as f:
            data = f.read()
            encrypted_data = cipher.encrypt(data)
        with open(filename, "wb") as f:
            f.write(encrypted_data)
            print('bilgişifrelendi')


    # Anahtar üretme
    def generate_key():
        if not os.path.exists("secret.key"):
            with open("secret.key", "wb") as key_file:
                key_file.write(STATIC_KEY)

    # Anahtar üretme
    generate_key()

    # Anahtarı yükleme
    key = load_key()


    encrypt_file("kitaplar.csv", key)
    encrypt_file2("ödÜnç_alınanlar.csv", key)
    encrypt_file3("getirenler.csv", key)

    

def kitap_bilgisi_ekle(x,kitap_kodubutmorehot ,kitap_kodu, kitap_adi, sayfa_sayisi, yazar):
    if kitap_kodubutmorehot == 1:
        qr(x)
        print("çekme başarılı")

    with open('kitaplar.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([x,kitap_kodu, kitap_adi, sayfa_sayisi, yazar])
    


def ödnçalmabilgiekle(a,kitap_kodu2, kitap_adi2, sayfa_sayisi2, yazar2,b):
    with open('ödÜnç_alınanlar.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([a,kitap_kodu2, kitap_adi2, sayfa_sayisi2, yazar2,b])

def getirdi(kitap_kodu2, kitap_adi2,şey1,şey2,şey3,şey4,şey5):
    with open('getirenler.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([kitap_kodu2, kitap_adi2,şey1,şey2,şey3,şey4,şey5])

def login():
    username = username_entry.get()
    password = password_entry.get()
    try:
        deşifreleme()
    except:
        
        messagebox.showinfo("Hata", "Şifre zaten şifrelenmiş halde")
    if password == true_passwordd and username == true_username:
        root.destroy() 
        open_new_window() 

def open_new_window_but_more_dope():
    
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Kitap Kayıt")
    new_window.geometry("720x500")
    patates = tk.IntVar()
    label1 = tk.Label(new_window, text="kitabın numarası",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Kitabın adı",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="Şair/Yazar/Çevirmen",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="Yayınevi",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    label5 = tk.Label(new_window, text="Sayfa Sayısı",background='#1e1e1e', foreground='white')
    label5.grid(row=4, column=0, padx=10, pady=10)

    entry5 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry5.grid(row=4, column=1, padx=10, pady=10)
    
    checkmark = tk.Checkbutton(new_window, background='#1e1e1e', foreground='black' ,variable=patates,onvalue=1,offvalue=0)
    checkmark.grid(row=0, column=2, padx=10, pady=10)
    

    onaybutoonu = tk.Button(new_window, text="Kitabı Kaydet" ,command=lambda: kitap_bilgisi_ekle(entry1.get(),patates.get(),entry5.get(), entry2.get(), entry3.get(), entry4.get()))
    onaybutoonu.grid(row=5, column=1, padx=10, pady=10)

    label5 = tk.Label(new_window, text="QR kod üretilsin mi? ",background="#1e1e1e",foreground="white")
    label5.grid(row=0, column=3, padx=1, pady=10)
    
    

    

    def eyyo():
        open_new_window()
        
    acilçıkış = tk.Button(new_window,text='Geri',command=eyyo)
    acilçıkış.grid(row=2, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu,onaybutoonu] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()

    

def öğrenci_kitabı_getirdi():
    
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Kitap teslim kaydı")
    new_window.geometry("720x700")
    
    def otodoldur():

        def sorgu():
            
            
            önemlihocam = qrkodoku23()
            bulunanlar = kelimeyi_bul2("ödÜnç_alınanlar.csv", srgu.get(), önemlihocam)
            entry1.insert(tk.END,bulunanlar[0])
            entry3.insert(tk.END,bulunanlar[2])
            entry2.insert(tk.END,bulunanlar[1])
            entry4.insert(tk.END,bulunanlar[3])
            entry5.insert(tk.END,bulunanlar[4])
            entry6.insert(tk.END,bulunanlar[5])
            now = datetime.now()
            now = now.strftime("%d-%m-%Y")
            entry7.insert(tk.END, now)
            gecici_pencere.destroy()
        
        
        gecici_pencere = tk.Tk()
        gecici_pencere.title("ek-1")

        #   Geçici pencerenin içeriğini oluştur
        etiket = tk.Label(gecici_pencere, text="Öğrencinin adını giriniz")
        etiket.pack(padx=20, pady=20)
        srgu = tk.Entry(gecici_pencere)
        srgu.pack(padx=20, pady=20)
        
        sorgubuton = tk.Button(gecici_pencere, command=sorgu,text="Sorgu yap")
        sorgubuton.pack()

        
        

    label1 = tk.Label(new_window, text="Kitap Numarası",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Kitap Adı",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="Sınıf",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="No",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    label5 = tk.Label(new_window, text="Ad Soyad",background='#1e1e1e', foreground='white')
    label5.grid(row=4, column=0, padx=10, pady=10)

    entry5 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry5.grid(row=4, column=1, padx=10, pady=10)

    label6 = tk.Label(new_window, text="Verildiği Tarih",background='#1e1e1e', foreground='white')
    label6.grid(row=5, column=0, padx=10, pady=10)

    entry6 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry6.grid(row=5, column=1, padx=10, pady=10)

    label7 = tk.Label(new_window, text="İade Tarihi",background='#1e1e1e', foreground='white')
    label7.grid(row=6, column=0, padx=10, pady=10)

    entry7 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry7.grid(row=6, column=1, padx=10, pady=10)

    srgubutton = tk.Button(new_window,background='#1e1e1e', foreground='white',command=otodoldur,text="Otomatik doldur")
    srgubutton.grid(row=6, column=2, padx=10, pady=10)

    onaybutoonu = tk.Button(new_window, text="Teslimi Kaydet" ,command=lambda: getirdi(entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get(),entry6.get(),entry7.get()))
    onaybutoonu.grid(row=7, column=1, padx=10, pady=10)
    def eyyo():
        open_new_window()
        
    acilçıkış = tk.Button(new_window,text='Geri',command=eyyo)
    acilçıkış.grid(row=3, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu,srgubutton] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()

def herşeyisil():
    
    
    cevap = messagebox.askquestion("Emin misiniz?", "Devam etmek istiyor musunuz?")
    if cevap == 'yes':
        def dosya_icerigini_sil(dosya_yolu):
            with open(dosya_yolu, 'w') as dosya:
                dosya.write('')
            print(f"{dosya_yolu} dosyasının içeriği silindi.")

        def main():
            # Sileceğiniz CSV dosyalarının listesi
            dosya_listesi = ["ödÜnç_alınanlar.csv", "kitaplar.csv", "getirenler.csv"]

            # Her dosya için içeriğin silinmesi
            for dosya in dosya_listesi:
                try:
                    dosya_icerigini_sil(dosya)
                except FileNotFoundError:
                    print(f"{dosya} adında bir dosya bulunamadı.")
        main()
        şifreleme()
        new_window.destroy()
    else:
        open_new_window()






def bişeyler():

    global new_window
    
    if new_window:
        new_window.destroy()
    
    

    def read_csv(file_path):
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    
    def karşılaştır(file1, file2, keyword, keyword2):
        data1 = read_csv(file1)
        data2 = read_csv(file2)

        matches = []
        for row1 in data1:
            if keyword and keyword2 in row1:
                for row2 in data2:
                    if keyword and keyword2 in row2:
                        matches.append((row1, row2))

        return matches

    def qrkodoku():
        
        data = None
            
        # Webcam'den görüntüyü almak için VideoCapture nesnesini oluşturun
        cap = cv2.VideoCapture(0)

        while True:
            # Her bir frame için görüntü yakalayın
            ret, frame = cap.read()

            # QR kodunu tespit etmek için decode() fonksiyonunu kullanın
            decoded_objects = decode(frame)

            # Her bir QR kodu için döngü
            for obj in decoded_objects:
                # QR kodunun içeriğini alın
                data = obj.data.decode("utf-8")
                # QR kodunun etrafına bir dikdörtgen çizin
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

                print("QR Code Detected:", data)

            cv2.imshow("QR Code Reader", frame)
            
            key = cv2.waitKey(1)
            if key == 27:  # Esc tuşuna basarak döngüyü sonlandırın
                break
            elif data is not None:  # QR kodu bulunduğunda döngüyü sonlandırın
                break

        # Kamerayı serbest bırakın ve pencereyi kapatın
        cap.release()
        cv2.destroyAllWindows()
        kitaptara(data)
    

    
        
    


    def ödunçalınanlariçindeara(file_path, name):
        data = read_csv(file_path)
        filtered_data = [row for row in data if name in row]        
        
        if filtered_data:
            for idx, row in enumerate(filtered_data, start=1):
                result_text.delete('1.0',tk.END)
                result_text.insert(tk.END, f"{name} içeren veri {idx}: {row}\n")
        else:
            result_text.delete('1.0',tk.END)
            result_text.insert(tk.END, f"{name} içeren veri bulunamadı.\n")

    def kitaptara(name):
        data = read_csv("kitaplar.csv")
        filtered_data = [row for row in data if name in row]

        
        if filtered_data:
            for idx, row in enumerate(filtered_data, start=1):
                result_text.delete('1.0',tk.END)
                result_text.insert(tk.END, f"{name} içeren veri {idx}: {row}\n")
                
        else:
            result_text.delete('1.0',tk.END)
            result_text.insert(tk.END, f"{name} içeren veri bulunamadı.\n")
            
    
    def siliciek(csv_dosya,hedef_kelime):
        yeni_satirlar = []
        with open(csv_dosya, 'r', newline='') as dosya:
            okuyucu = csv.reader(dosya)
            for satir in okuyucu:
                if hedef_kelime not in satir:
                    yeni_satirlar.append(satir)

        with open(csv_dosya, 'w', newline='') as dosya:
            yazici = csv.writer(dosya)
            yazici.writerows(yeni_satirlar) 
            print("silindi")


    def widgetiçindegöster():
        file1_path = "ödÜnç_alınanlar.csv"
        file2_path = "getirenler.csv"
        keyword = keyword_entry.get() 
        keyword2 = keyword_entry2.get()
        matches = karşılaştır(file1_path, file2_path, keyword, keyword2) 

        if matches:
            result_text.delete('1.0',tk.END)
            result_text.insert(tk.END, f"{keyword} numaralı öğrenci bulundu:\n")
            for idx, (row1, row2) in enumerate(matches):
                text = f"Ödünç Alınanlar: {row1}\nGetirenler: {row2}\n"
                result_text.insert(tk.END, text)
        else:
            result_text.delete('1.0',tk.END)
            result_text.insert(tk.END, f"{keyword} numaralı öğrenci getirmemiş.\n")

    def eyyo():
        open_new_window()
        

        
    new_window = tk.Tk()
    new_window.title("Kitap ödünç kaydı alma")
    new_window.geometry("1120x700")
    
    new_window.config (bg="#26242f")
    
    title_label = tk.Label(new_window, text="Sorgulama Paneli", background='#26242f', foreground='white')
    title_label.pack(pady=10)

  
    keyword_entry = tk.Entry(new_window, background='#26242f', foreground='white') 
    keyword_entry.pack(pady=5) 

    keyword_entry2 = tk.Entry(new_window, background='#26242f', foreground='white') 
    keyword_entry2.pack(pady=5)

    
    search_button = tk.Button(new_window, text="İsim Arama", command=lambda: ödunçalınanlariçindeara("ödÜnç_alınanlar.csv", keyword_entry.get()))
    search_button.pack(pady=5)
    
    search_button2 = tk.Button(new_window, text="İsme göre kitap ara", command=lambda: kitaptara(keyword_entry.get()))
    search_button2.pack(pady=5)

    
    compare_name_button = tk.Button(new_window, text="Sadece İsim İçeren Verileri Karşılaştır", command=widgetiçindegöster)
    compare_name_button.pack(pady=5)

    silici2 = tk.Button(new_window, text="Seçilen satırı sil", command=lambda: siliciek("kitaplar.csv",keyword_entry.get()))
    silici2.pack(pady=5)

    QRkodeyaratıcısı = tk.Button(new_window, text="QR kod tara", command=qrkodoku)
    QRkodeyaratıcısı.pack(pady=5)


  
    result_text = tk.Text(new_window, wrap=tk.WORD, bg='#26242f', fg='white', insertbackground='white', selectbackground='#444444')
    result_text.pack(fill=tk.BOTH, expand=True)

    acilçıkış = tk.Button(new_window, text="Geri",command=eyyo)
    acilçıkış.pack()

    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, search_button,compare_name_button,search_button2,QRkodeyaratıcısı,silici2] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()
    

def easter():
    
    cevap1 = messagebox.askyesno("???","????????")
    if cevap1:
        cevap2 = messagebox.askyesno("Rebot","GLaDOS'u yeniden başlat?")
        if cevap2:
            import subprocess
            subprocess.Popen("pıst.mp4", shell=True)

def ödnçalmaşeyi():
    
    global new_window
    if new_window:
        new_window.destroy()  
    new_window = tk.Tk()
    new_window.title("Kitap ödünç kaydı alma")
    new_window.geometry("720x500")


    def otodoldur():
        now = datetime.now()
        now = now.strftime("%d-%m-%Y")
        entry5.insert(tk.END, now)
        önemlihocam = qrkodoku23()
        xd = kelimeyi_bul("kitaplar.csv",önemlihocam)
        entry6.insert(tk.END,xd[0])
        entry1.insert(tk.END,xd[2])


    label1 = tk.Label(new_window, text="Kitabın Adı",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Sınıfı",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="Öğrenci No",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="Ad Soyad",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    label5 = tk.Label(new_window, text="Verildiği Tarih",background='#1e1e1e', foreground='white')
    label5.grid(row=4, column=0, padx=10, pady=10)

    entry5 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry5.grid(row=4, column=1, padx=10, pady=10)

    label6 = tk.Label(new_window, text="Kitabın Kodu",background='#1e1e1e', foreground='white')
    label6.grid(row=5, column=0, padx=10, pady=10)

    entry6 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry6.grid(row=5, column=1, padx=10, pady=10)

    onaybutoonu = tk.Button(new_window, text="Ödünç Kaydet" ,command=lambda: ödnçalmabilgiekle(entry6.get(),entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get()))
    onaybutoonu.grid(row=6, column=1, padx=10, pady=10)
    onaybutoonu2 = tk.Button(new_window, text="Otomatik doldur" ,command=otodoldur)
    onaybutoonu2.grid(row=5, column=2, padx=10, pady=10)
    def eyyo():
        open_new_window()

    acilçıkış = tk.Button(new_window,text='Geri',command=eyyo)
    acilçıkış.grid(row=3, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu,onaybutoonu2] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()

def open_new_window():

    def deyyo():
        şifreleme()
        new_window.destroy()
        
    global new_window
    if new_window:
        new_window.destroy()
    new_window = tk.Tk()
    new_window.title("Seçim Ekranı")
    new_window.geometry("400x200")
    label = tk.Label(new_window, text="Veriler Deşifre Edildi\n Ne yapmak istersiniz?", foreground='white', background='#1e1e1e')
    label.grid(row=1, column=0, padx=5, pady=5)
    seçim_butonu1 = tk.Button(new_window, text='Kitap Kaydı yap', command=open_new_window_but_more_dope)
    seçim_butonu1.grid(row=1, column=1, padx=5, pady=5)
    aperture = tk.Button(new_window, text='Aperture Science', command=FG)
    aperture.grid(row=5, column=1, padx=2, pady=5)
    seçim_butonu2 = tk.Button(new_window, text='Ödünç verilenler', command=ödnçalmaşeyi)
    seçim_butonu2.grid(row=1, column=2, padx=5, pady=5)
    seçim_butonu3 = tk.Button(new_window, text='Sorgulama Paneli', command=bişeyler)
    seçim_butonu3.grid(row=2, column=1, padx=5, pady=5)
    seçim_butonu4 = tk.Button(new_window, text='Kitabı Getirenler', command=öğrenci_kitabı_getirdi)
    seçim_butonu4.grid(row=2, column=2, padx=5, pady=5)
    seçim_butonu5 = tk.Button(new_window, text='Tüm verileri sil', command=herşeyisil)
    seçim_butonu5.grid(row=5, column=2)
    easter_egg = tk.Button(new_window, text='????', command=easter)
    easter_egg.grid(row=5, column=3)
    
        
    acilçıkış = tk.Button(new_window,text='Çıkar ve şifreler',command=deyyo)
    acilçıkış.grid(row=5, column=0, padx=5, pady=78)

    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [seçim_butonu1 , seçim_butonu2, seçim_butonu3, seçim_butonu4 ,acilçıkış,seçim_butonu5,easter_egg,aperture]:
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    
    new_window.mainloop()

   

def linkaç(event=None):
    
    webbrowser.open('https://github.com/ByReals/Library-managment-data-base/tree/main')

root = tk.Tk()
root.title("Giriş Ekranı")
root.geometry("700x350")


username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Şifre:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

infopamel = tk.Label(root, text="HCEFL KÜTÜPHANE YÖNETİMİ\nVeriler Fernet ile şifrelenmiştir\n")
infopamel.grid(row=0, column=4, padx=5, pady=5, )

infopamel2 = tk.Label(root, text="Admin girişi")
infopamel2.grid(row=1, column=4, padx=5, pady=5, )

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)


img = Image.open("17145447_LOGO-2006.png")  
img = img.resize((150, 150), Image.ADAPTIVE) 
photo = ImageTk.PhotoImage(img)


photo_label = tk.Label(root, image=photo)
photo_label.grid(row=0, column=5, rowspan=2, padx=78, pady=10 )


login_button = tk.Button(root, text="Giriş Yap", width=10, command=login)
login_button.grid(row=2, column=1, padx=12, pady=10)


root.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')

reklam = tk.Label(root, text="Ekrem Emre tarafından Yapıldı\nGithub linkim için tıklayın")
reklam.grid(row=4, column=5, padx=13, pady=80)
reklam.config(cursor='hand2')
reklam.bind("<Button-1>", linkaç)


root.mainloop()
