from src import admin, auth, categories, employees, items, reports, suppliers, transactions, Config
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

if __name__ == "__main__":
    dataUser = auth.manage.PersonManager(Config.dataUser)
    currentUser = auth.controller.authSection(dataUser);
    print(currentUser.getData())
# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana