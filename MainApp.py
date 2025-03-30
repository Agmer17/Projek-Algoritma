from src import admin, auth, categories, employees, items, reports, suppliers, transactions, Config
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

#testing
listUser = auth.manage.PersonManager(Config.dataUser)
auth.controller.authSection(listUser)
listUser.deleteData("atmin_datang")

for user in listUser.items : 
    print(user)
# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana