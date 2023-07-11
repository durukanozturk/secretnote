from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import base64

#encrypted fonksiyonları
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



#save and encrypt button
def click_save_button():
    master_key = my_key_entry.get()
    baslik = my_title_entry.get()
    sifre = my_text_entry.get("1.0",END)


    if baslik == "" or str(sifre).isspace() or master_key == "":
        messagebox.showerror("showerror", "Lütfen İstenen Değerleri Giriniz")

    else:

        messagebox.showinfo("showinfo", "Dosyanız Başarıyla Oluşturulmuştur")


    message_encrypted = encode(master_key, sifre)

    with open("secretnote.txt", "a") as f:
        f.write("\n" + "Başlık: " + baslik + "\n" + "Şifre: " + message_encrypted)



    my_key_entry.delete(0,END)
    my_title_entry.delete(0,END)
    my_text_entry.delete("1.0","end")


#decrypt button
def click_decrypt_button():
    message =my_text_entry.get("1.0",END)
    master_secret = my_key_entry.get()


    if str(message).isspace() or master_secret == "" :
        messagebox.showerror("showerror", "Lütfen İstenen Değerleri Giriniz")
    else :
        try:
            decrypted_message = decode(master_secret, message)
            my_text_entry.delete("1.0",END)
            my_text_entry.insert("1.0", decrypted_message)
        except:
            messagebox.showerror("showerror","Lütfen doğru bir giriş yap")




#window
window = Tk()
window.title("Secret Notes")
window.geometry("375x750")


#image
image1 = Image.open("topsecret.png")
resize_image = image1.resize((90,90))
image_secret_app = ImageTk.PhotoImage(resize_image)

image_label = Label(image=image_secret_app)
image_label.place(x = 145,y=45)

icon_photo = PhotoImage(file="topsecreticon.png")
window.iconphoto(False, icon_photo)

#title

my_title_label = Label(text="Enter your title",font=("bold"))
my_title_label.place(x = 138,y=150)

my_title_entry = Entry(width=35)
my_title_entry.place(x = 80,y=180)

#text

my_text_label = Label(text="Enter your secret",font=("bold"))
my_text_label.place(x = 130,y=205)

my_text_entry = Text(width=26, height=20)
my_text_entry.place(x = 80, y=235)


#key
my_key_label = Label(text="Enter master key",font=("bold"))
my_key_label.place(x=125,y=570)

my_key_entry = Entry(width=35)
my_key_entry.place(x=80,y=595)

#button
save_button = Button(text="Save & Encrypt",font=("bold"),command=click_save_button)
save_button.place(x=120,y=625)

decrypt_button = Button(text="Decrypt",font=("bold"),command=click_decrypt_button)
decrypt_button.place(x=145,y=665)


window.mainloop()