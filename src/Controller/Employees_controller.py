
# import module json ke file
from src.Config import *
from src.Manager.ItemManager import ItemManager
# mencari item berdasarkan kategori atau nama. dari file items.json
# melihat daftar barang -> fitur pencarian barang berdasarkan nama/kategori -Aretta
def searchItem(name:str="",category="") :
    # Loading datanya dulu
    
        # data di parsing dari json string ke dictionary
    data_parsing = ItemManager(pathDataItem)
    # case 1: Name dan category kosong
    if name == "" and category == "":
        # iterating dictionary:
        for key, value in data_parsing.listData.items():
            dummyCurrentData = value.getAllData()
            print(f"Nama barang: {dummyCurrentData['name']} \nKategori: {dummyCurrentData['category']} \n")

    # case 2: name ada dan category kosong
    elif name != "" and category == "":
        # iterating dictionary:
        for key, value in data_parsing.listData.items():
            dummyCurrentData = value.getAllData()
            if value.name.lower().startswith(name.lower()):
                print(f"Nama barang: {dummyCurrentData['name']} \nKategori: {dummyCurrentData['category']} \n")

    # case 3: name ga ada dan category ada
    elif name == "" and category != "":
        # iterating dictionary:
        for key, value in data_parsing.listData.items():
            if value.category.lower().startswith(category.lower()):
                dummyCurrentData = value.getAllData()
                print(f"Nama barang: {dummyCurrentData['name']} \nKategori: {dummyCurrentData['category']} \n")
    # case 4: keduanya ada
    elif name != "" and category != "":
        # iterating dictionary:
        for key, value in data_parsing.listData.items():
            if value.category.lower().startswith(category.lower()) and value.name.lower().startswith(name.lower()):
                dummyCurrentData = value.getAllData()
                print(f"Nama barang: {dummyCurrentData['name']} \nKategori: {dummyCurrentData['category']} \n")
        

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




