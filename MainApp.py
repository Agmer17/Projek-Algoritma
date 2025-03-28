from src import admin, auth, categories, employees, items, reports, suppliers, transactions, Config
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

#testing
data = auth.schema.PersonManager(Config.dataUser)

print(data.items["user_admin_01"].changeName("Agmer"))

# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana