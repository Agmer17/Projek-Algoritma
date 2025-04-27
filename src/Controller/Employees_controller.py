
# import module json ke file
import json
import os
currentDir = os.path.dirname(__file__)
itemJsonPath = os.path.join(currentDir, '../../data/items.json')
# mencari item berdasarkan kategori atau nama. dari file items.json
# melihat daftar barang -> fitur pencarian barang berdasarkan nama/kategori -Aretta
def searchItem(name="",category="") :
    # Loading datanya dulu
    with open(itemJsonPath) as dataBarang:
        isiData = dataBarang.read()
        # data di parsing dari json string ke dictionary
    data_parsing = json.loads(isiData)
    # case 1: Name dan category kosong
    if name == "" and category == "":
        # iterating dictionary:
        for key, value in data_parsing.items():
            print(f"Nama barang: {value['name']} \nKategori: {value['category']} \n")

    # case 2: name ada dan category kosong
    elif name != "" and category == "":
        # iterating dictionary:
        for key, value in data_parsing.items():
            if value['name'].startswith(name):
                print(f"Nama barang: {value['name']} \nKategori: {value['category']} \n")

    # case 3: name ga ada dan category ada
    elif name == "" and category != "":
        # iterating dictionary:
        for key, value in data_parsing.items():
            if value['category'].startswith(category):
                print(f"Nama barang: {value['name']} \nKategori: {value['category']} \n")
    # case 4: keduanya ada
    elif name != "" and category != "":
        # iterating dictionary:
        for key, value in data_parsing.items():
            if value['category'].startswith(category) and value['name'].startswith(name):
                print(f"Nama barang: {value['name']} \nKategori: {value['category']} \n")
        

# Update stok barang -> Input stock masuk dan keluar (tanpa bisa edit atau hapus barang) -Aretta
def updateItem(name,category):
    pass
    # # Modelan generator json kaya di package nodejs
    # objectName
    # name
    # category
    # stock
    # price
    # sellPrice
    # entryDate
    # desc
    # supplier
    # status
    # pass
# Melihat laporan sederhana -> Menampilkan jumlah barang masuk dan keluar per bulan.
def viewReport():
    pass
    # gua kepikiran buat bikin for loops satu-satu tiap item
    # abis itu di print out semuanya aja.

# Menerapkan algoritma searching (linear search /  binary search).
# Menerapkan algoritma sorting (Bubble sort/ Quick sort).




