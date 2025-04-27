
# import module json ke file
from src.Config import *
from src.Manager.ItemManager import ItemManager
# mencari item berdasarkan kategori atau nama. dari file items.json
# melihat daftar barang -> fitur pencarian barang berdasarkan nama/kategori -Aretta
def searchItem(name: str = "", category: str = ""):
    # Load data
    data_parsing = ItemManager(pathDataItem)

    # Normalisasi input supaya perbandingan lebih mudah
    name = name.lower()
    category = category.lower()

    for key, value in data_parsing.listData.items():
        item_data = value.getAllData()
        item_name = value.name.lower()
        item_category = value.category.lower()

        # Cek apakah item cocok dengan filter
        if (not name or item_name.startswith(name)) and (not category or item_category.startswith(category)):
            print(f"Nama barang: {item_data['name']}\nKategori: {item_data['category']}\n")

        

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




