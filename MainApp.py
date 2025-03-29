from src import admin, auth, categories, employees, items, reports, suppliers, transactions, Config
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

#testing
# auth.controller.login()
listUser = auth.manage.PersonManager(Config.dataUser)
karyawan_baru = {
    "name" : "hiura",
    "username" : "hiura_imut",
    "email" : "hiura@gmail.com",
    "password" : "12345",
    "role" : "admin"
    }

listUser.addData(karyawan_baru)
dataBaru = listUser.findUser("hiura_imut")
print(dataBaru.getData())

# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana