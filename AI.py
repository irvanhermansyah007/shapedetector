from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    # init Variabel untuk load dataset
    kotak = []
    lingkaran = []
    segitiga = []

    for file in os.listdir("kotak"):        # mencari file dan membuatnya ke gambar 1 dimensi
        img = Image.open("kotak/" + file)   # membuka file
        img = np.array(img)                 # mengubah ke array agar dapat di flatten
        img = img.flatten()                 # flatten img
        kotak.append(img)                   # menambahkan img yang sudah di flatten ke variabel 

    for file in os.listdir("lingkaran"):        # mencari file dan membuatnya ke gambar 1 dimensi
        img = Image.open("lingkaran/" + file)   # membuka file
        img = np.array(img)                     # mengubah ke array agar dapat di flatten
        img = img.flatten()                     # flatten img
        lingkaran.append(img)                   # menambahkan img yang sudah di flatten ke variabel

    for file in os.listdir("segitiga"):         # mencari file dan membuatnya ke gambar 1 dimensi
        img = Image.open("segitiga/" + file)    # membuka file
        img = np.array(img)                     # mengubah ke array agar dapat di flatten
        img = img.flatten()                     # flatten img
        segitiga.append(img)                    # menambahkan img yang sudah di flatten ke variabel
    
    return kotak, lingkaran, segitiga          # return kotak, lingkaran, segitiga

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5) # Membuat KNN
    print("[INFO] Loading Dataset")
    kotak, lingkaran, segitiga = load_dataset() # menyimpan data x
    print("[INFO] Loading Model")
    # menyimpan data y dalam Array
    y_kotak = np.zeros(len(kotak))
    y_lingkaran = np.ones(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 2
    X = kotak + lingkaran + segitiga                        # Menggabungkan semua data x
    #X = np.array(X).reshape(-1,1)
    y = np.concatenate([y_kotak, y_lingkaran, y_segitiga])  # Menggabungkan semua data x
    y = y.reshape(-1,1)
    model.fit(X, y)                                         # proses gambar
    return model                                            # return model