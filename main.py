import tkinter as tk                                # Library untuk membuat UI Paint
import AI                                           # Program AI yang digunakan
import numpy as np
import os
from PIL import Image, ImageTk, ImageDraw           # Library PIL dan object-object untuk program

model = AI.load_ai()                                # Load data set AI
window = tk.Tk()                                    # Menampilkan UI dari tkinter
img = Image.new(mode="1", size=(500, 500), color=0) # Membuat img untuk canvas
# Update tampilan UI setelah selesai menggambar
tkimage = ImageTk.PhotoImage(img)                   # Membuat img yang telah dibuat agar terbaca oleh UI tkinter = tkimage
canvas = tk.Label(window, image=tkimage)            # Menempatkan tkimage(canvas) untuk ditimpa ke UI (window)
canvas.pack()                                       # Update Tampilan UI
draw = ImageDraw.Draw(img)                          # Tools untuk dapat mengambar di UI
last_point = (0, 0)                                 # Titik start untuk menggambar (saat leftmost di klik)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)
def draw_image(event):                                          # Fungsi untuk menggambar pada UI
    global last_point, tkimage, prediction                      # Variabel global yang dibutuhkan pada fungsi ini
    current_point = (event.x, event.y)                          # titik saat ini
    draw.line([last_point, current_point], fill=255, width=50)  # Menggambar garis sesuai dengan titik awal dan akhir
    last_point = current_point                                  # perpindahan titik awal dan akhir agar terbentuk garis
    # Update tampilan UI setelah selesai menggambar
    tkimage = ImageTk.PhotoImage(img)               # Membuat img yang telah dibuat agar terbaca oleh UI tkinter = tkimage          
    canvas['image'] = tkimage                       # Menempatkan tkimage(canvas) untuk ditimpa ke UI (window) pada object image
    canvas.pack()                                   # Update Tampilan UI
    img_temp = img.resize((28, 28))                 # resize gambar untuk memudahkan AI
    img_temp = np.array(img_temp)                   # menggubah ke array agar bisa di flatten
    img_temp = img_temp.flatten()                   # flatten img_temp
    output = model.predict([img_temp])   # fungsi menyimpan prediksi dari AI
    if(output[0] == 0):                  # tampilkan prediction.set = kotak ke UI saat output [0] == 0
        prediction.set("kotak")          # fungsi set prediksi dari AI
    elif(output[0] == 1):                # tampilkan prediction.set = kotak ke UI saat output [1] == 1
        prediction.set("lingkaran")      # fungsi set prediksi dari AI
    else:                                # tampilkan prediction.set = kotak ke UI saat output [2] == 2
        prediction.set("segitiga")       # fungsi set prediksi dari AI
        label.pack()                     # Update label dari AI   
def start_draw(event):                        # Fungsi callback untuk menampung titik awqal saat leftmost di klik
    global last_point                         # Variabel global yang dibutuhkan pada fungsi ini
    last_point = (event.x, event.y)           # Menyimpan titik start ke variabel last_point
def reset_canvas(event):                      # Funsi callback untuk memperbaharui canvas saat rightmost di klick
    global tkimage, img, draw                 # Variabel global yang dibutuhkan pada fungsi ini
    img = Image.new(mode="1", size=(500, 500), color=0) # Membuat img untuk canvas
    draw = ImageDraw.Draw(img)                          # Tools untuk dapat mengambar di UI
    # Update tampilan UI setelah selesai menggambar
    tkimage = ImageTk.PhotoImage(img)               # Membuat img yang telah dibuat agar terbaca oleh UI tkinter = tkimage          
    canvas['image'] = tkimage                       # Menempatkan tkimage(canvas) untuk ditimpa ke UI (window) pada object image
    canvas.pack()                                   # Update Tampilan UI
kotak = len(os.listdir("kotak"))                    # Varibel penampung counter saat file kotak.png dibuat
lingkaran = len(os.listdir("lingkaran"))            # Varibel penampung counter saat file lingkaran.png dibuat
segitiga = len(os.listdir("segitiga"))              # Varibel penampung counter saat file segitiga.png dibuat

def save_image(event):                              # Fungsi callback untuk menyimpan file kotak, lingkaran, segitiga foldernya masing-masing
    global kotak, lingkaran, segitiga               # Varibel-variabel penampung counter 
    img_temp = img.resize((28, 28))
    if(event.char == "k"):                          # saat menggambar kotak pada canvas maka simpan file gambar tersebut dengan menggunakan tombol k
        img_temp.save(f"kotak/{kotak}.png")         # fungsi untuk menyimpan file kotak
        kotak += 1                                  # increment variabel untuk menyimpan file dengan index
    elif(event.char == "l"):                        # saat menggambar lingkaran pada canvas maka simpan file gambar tersebut dengan menggunakan tombol l
        img_temp.save(f"lingkaran/{lingkaran}.png") # fungsi untuk menyimpan file lingkaran
        lingkaran += 1                              # increment variabel untuk menyimpan file dengan index
    elif(event.char == "s"):                        # saat menggambar kotak pada canvas maka simpan file gambar tersebut dengan menggunakan tombol s
        img_temp.save(f"segitiga/{segitiga}.png")   # fungsi untuk menyimpan file segitiga
        segitiga += 1                               # increment variabel untuk menyimpan file dengan index
# bind tombol yang akan digunakan oleh macam-macam event
window.bind("<B1-Motion>", draw_image)              # bind tombol yang akan digunakan pada fungsi callback
window.bind("<ButtonPress-1>", start_draw)          # bind tombol yang akan digunakan pada fungsi callback
window.bind("<ButtonPress-3>", reset_canvas)        # bind tombol yang akan digunakan pada fungsi callback
window.bind("<Key>", save_image)                    # bind tombol yang akan digunakan pada fungsi callback
label.pack()                                        # Update label dari AI
window.mainloop()                                   # loop program