from src import admin, auth, categories, employees, items, reports, suppliers, transactions 
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

#testing
newAdmin = admin.Schema.Admin("agmer", "agmerAja", "agmer@gmail.com", "pw", "admin")

print(newAdmin.getData())

# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana