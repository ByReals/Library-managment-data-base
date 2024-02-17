import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sys
import csv
from tkinter import ttk


true_passwordd = 'admin123'
true_username = 'admin123'

new_window = None  # global değişken

sys.stdout.reconfigure(encoding='utf-8')


def şifreleme():
    import pandas as pd
    from cryptography.fernet import Fernet
    import os

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
            data = f.read()
            decrypted_data = cipher.decrypt(data)
        with open(filename, "wb") as f:
            f.write(decrypted_data)
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


    encrypt_file("kitaplar.csv", key)
    encrypt_file2("ödÜnç_alınanlar.csv", key)
    encrypt_file3("getirenler.csv", key)

    # Dosyayı çözme
    #   decrypt_file("kitaplar.csv", key) 
    #decrypt_file2("ödÜnç_alınanlar.csv", key) 

def kitap_bilgisi_ekle(kitap_kodu, kitap_adi, sayfa_sayisi, yazar):
    with open('kitaplar.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([kitap_kodu, kitap_adi, sayfa_sayisi, yazar])

def ödnçalmabilgiekle(kitap_kodu2, kitap_adi2, sayfa_sayisi2, yazar2):
    with open('ödÜnç_alınanlar.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([kitap_kodu2, kitap_adi2, sayfa_sayisi2, yazar2])

def getirdi(kitap_kodu2, kitap_adi2,şey1,şey2):
    with open('getirenler.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([kitap_kodu2, kitap_adi2,şey1,şey2])

def login():
    username = username_entry.get()
    password = password_entry.get()
    if password == true_passwordd and username == true_username:
        root.destroy() 
        open_new_window() 

def open_new_window_but_more_dope():
    
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Kitap ÖDÜNÇ kaydı alma")
    new_window.geometry("720x500")

    label1 = tk.Label(new_window, text="Öğrencinin Adını giriniz",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Kitabın numarasını giriniz",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="ÖDÜNÇ alma tarihini giriniz",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="Geri getirme zamanını giriniz",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    onaybutoonu = tk.Button(new_window, text="ÖDÜNÇLÜĞÜ KAYDET" ,command=lambda: kitap_bilgisi_ekle(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    onaybutoonu.grid(row=4, column=1, padx=10, pady=10)
    def eyyo():
        open_new_window()
        new_window.destroy()
    acilçıkış = tk.Button(new_window,text='Çıkar ve şifreler',command=eyyo)
    acilçıkış.grid(row=3, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu] :
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
    new_window.title("Kitap ÖDÜNÇ kaydı alma")
    new_window.geometry("720x500")

    label1 = tk.Label(new_window, text="Öğrencinin Adını giriniz",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Kitabın numarasını giriniz",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="ÖDÜNÇ alma tarihini giriniz",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="Geri getirme zamanını giriniz",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    onaybutoonu = tk.Button(new_window, text="ÖDÜNÇLÜĞÜ KAYDET" ,command=lambda: getirdi(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    onaybutoonu.grid(row=4, column=1, padx=10, pady=10)
    def eyyo():
        open_new_window()
        new_window.destroy()
    acilçıkış = tk.Button(new_window,text='Çıkar ve şifreler',command=eyyo)
    acilçıkış.grid(row=3, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()

def bişeyler():
    
    global new_window
    if new_window:
        new_window.destroy()
    
    import tkinter as tk
    from tkinter import ttk
    import csv

    def read_csv(file_path):
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    def compare_csv(file1, file2):
        data1 = read_csv(file1)
        data2 = read_csv(file2)

        diff = []
        for row1, row2 in zip(data1, data2):
            if row1 != row2:
                diff.append((row1, row2))

        return diff

    def display_filtered_data(file_path, name):
        data = read_csv(file_path)
        filtered_data = [row for row in data if name in row[0]]

        result_text.delete('1.0', tk.END)  # Temizle
        if filtered_data:
            for idx, row in enumerate(filtered_data, start=1):
                result_text.insert(tk.END, f"{name} içeren veri {idx}: {row}\n")
        else:
            result_text.insert(tk.END, f"{name} içeren veri bulunamadı.\n")

    def display_differences():
        file1_path = "ödÜnç_alınanlar.csv"
        file2_path = "getirenler.csv"

        differences = compare_csv(file1_path, file2_path)

        if differences:
            result_text.delete('1.0', tk.END)  # Temizle
            result_text.insert(tk.END, "Farklılık Bulundu:\n")
            for idx, (row1, row2) in enumerate(differences):
                text = f"Farklılık {idx+1}: {row1} != {row2}\n"
                result_text.insert(tk.END, text)
        else:
            result_text.delete('1.0', tk.END)  # Temizle
            result_text.insert(tk.END, "Herkes Getirmiştir.\n")

    new_window = tk.Tk()
    new_window.title("Sorgulama Ekranı")
    new_window.geometry("940x620")
    new_window.configure(bg='#1e1e1e')  # Dark mode tema

    # Başlık etiketi
    title_label = ttk.Label(new_window, text="Sorgulama Paneli", background='#1e1e1e', foreground='white')
    title_label.pack(pady=10)

    # İsim giriş kutusu
    name_entry = ttk.Entry(new_window)
    name_entry.pack(pady=5)

    # Veri Tabanından İsim Arama Butonu
    search_button = ttk.Button(new_window, text="İsim Arama", command=lambda: display_filtered_data("ödÜnç_alınanlar.csv", name_entry.get()))
    search_button.pack(pady=5)

    # Sadece İsim içeren Verileri Karşılaştırma Butonu
    compare_name_button = ttk.Button(new_window, text="Sadece İsim İçeren Verileri Karşılaştır", command=display_differences)
    compare_name_button.pack(pady=5)

    # Sonuç text widget'ı
    result_text = tk.Text(new_window, wrap=tk.WORD, bg='#1e1e1e', fg='white', insertbackground='white', selectbackground='#444444')
    result_text.pack(fill=tk.BOTH, expand=True)

    # Karşılaştırma butonu
    compare_button = ttk.Button(new_window, text="Veri Tabanını Sorgula", command=display_differences)
    compare_button.pack(pady=10)
    def eyyo():
        open_new_window()
        new_window.destroy()
    acilçıkış = ttk.Button(new_window, text="Geri",command=eyyo)
    acilçıkış.pack()

    # Butonların arka plan rengini değiştir
    for button in [search_button, compare_button, compare_name_button]:
        button.configure(style='DarkButton.TButton')

    # Temayı oluştur
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', width=30)  # Dark mode için buton stil ayarı
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')

    new_window.mainloop()


def ödnçalmaşeyi():
    
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Kitap ÖDÜNÇ kaydı alma")
    new_window.geometry("720x500")

    label1 = tk.Label(new_window, text="Öğrencinin Adını giriniz",background='#1e1e1e', foreground='white')
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(new_window, text="Kitabın numarasını giriniz",background='#1e1e1e', foreground='white')
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(new_window, text="ÖDÜNÇ alma tarihini giriniz",background='#1e1e1e', foreground='white')
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(new_window, text="Geri getirme zamanını giriniz",background='#1e1e1e', foreground='white')
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(new_window,background='#1e1e1e', foreground='white')
    entry4.grid(row=3, column=1, padx=10, pady=10)

    onaybutoonu = tk.Button(new_window, text="ÖDÜNÇLÜĞÜ KAYDET" ,command=lambda: ödnçalmabilgiekle(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    onaybutoonu.grid(row=4, column=1, padx=10, pady=10)
    def eyyo():
        open_new_window()
        new_window.destroy()
    acilçıkış = tk.Button(new_window,text='Çıkar ve şifreler',command=eyyo)
    acilçıkış.grid(row=3, column=2, padx=10, pady=10)
    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [acilçıkış, onaybutoonu] :
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    new_window.mainloop()

def open_new_window():
    def eyyo():
        new_window.destroy()
        şifreleme()
    global new_window
    if new_window:
        new_window.destroy()  # Eski pencereyi yok et
    new_window = tk.Tk()
    new_window.title("Seçim Ekranı")
    new_window.geometry("400x200")
    label = tk.Label(new_window, text="Veriler Deşifre Edildi\n Ne yapmak istersiniz?", foreground='white', background='#1e1e1e')
    label.grid(row=1, column=0, padx=5, pady=5)
    seçim_butonu1 = tk.Button(new_window, text='Kitap Kaydı yap', command=open_new_window_but_more_dope)
    seçim_butonu1.grid(row=1, column=1, padx=5, pady=5)
    seçim_butonu2 = tk.Button(new_window, text='Ödünç verilenler', command=ödnçalmaşeyi)
    seçim_butonu2.grid(row=1, column=2, padx=5, pady=5)
    seçim_butonu3 = tk.Button(new_window, text='Sorgulama Paneli', command=bişeyler)
    seçim_butonu3.grid(row=2, column=1, padx=5, pady=5)
    seçim_butonu4 = tk.Button(new_window, text='Kitabı Getirenler', command=öğrenci_kitabı_getirdi)
    seçim_butonu4.grid(row=2, column=2, padx=5, pady=5)
    acilçıkış = tk.Button(new_window,text='Çıkar ve şifreler',command=eyyo)
    acilçıkış.grid(row=5, column=0, padx=5, pady=78)

    def on_enter(event):
        event.widget.config(bg='#777777')

    def on_leave(event):
        event.widget.config(bg='#333333')
    for buton in [seçim_butonu1 , seçim_butonu2, seçim_butonu3, seçim_butonu4 ,acilçıkış]:
        buton.configure(bg='#333333', fg='white', activebackground='#555555', activeforeground='white', relief='flat')
        buton.bind("<Enter>", on_enter)
        buton.bind("<Leave>", on_leave)

    new_window.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')
    new_window.config(bg="#1e1e1e")
    style = ttk.Style(new_window)
    style.configure('DarkButton.TButton', background='#555555', foreground='white', width=30)
    x = 0
    x = x + 1
    if x == 1:

        import pandas as pd
        from cryptography.fernet import Fernet
        import os

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


        #encrypt_file("kitaplar.csv", key)
        #encrypt_file2("ödÜnç_alınanlar.csv", key)

        # Dosyayı çözme
        decrypt_file("kitaplar.csv", key) 
        decrypt_file2("ödÜnç_alınanlar.csv", key) 
        decrypt_file3("getirenler.csv", key) 
    else:
        pass
   

def linkaç(event=None):
    import webbrowser
    webbrowser.open('https://github.com/ByReals/Library-managment-data-base/tree/main')

root = tk.Tk()
root.title("Giriş Ekranı")
root.geometry("700x350")

# Giriş bilgileri için etiketler ve giriş kutuları
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

# Fotoğrafı yeniden boyutlandır
img = Image.open("17145447_LOGO-2006.png")  
img = img.resize((150, 150), Image.ADAPTIVE) 
photo = ImageTk.PhotoImage(img)

# Fotoğraf etiketini oluştur
photo_label = tk.Label(root, image=photo)
photo_label.grid(row=0, column=5, rowspan=2, padx=78, pady=10 )

# 'Giriş Yap' butonu
login_button = tk.Button(root, text="Giriş Yap", width=10, command=login)
login_button.grid(row=2, column=1, padx=12, pady=10)

# Pencere ikonunu ayarla
root.iconbitmap('24131643_milli_eyitim_bakanlyyy_arma_logo_VzW_icon.ico')

reklam = tk.Label(root, text="Ekrem Emre tarafından Yapıldı\nGithub linkim için tıklayın")
reklam.grid(row=4, column=5, padx=13, pady=80)
reklam.config(cursor='hand2')
reklam.bind("<Button-1>", linkaç)


root.mainloop()
