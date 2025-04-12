from src import admin, auth, categories, employees, items, reports, suppliers, transactions, Config, Dashboard
# nanti cara make modul nya gini 
# <nama_modul/folder>.<controller/schema>.<nama_fungsi>

if __name__ == "__main__":
    dataUser = auth.manage.PersonManager(Config.dataUser)
    # currentUser = auth.controller.authSection(dataUser)
    # print(type(currentUser))
    # Dashboard.mainMenu(currentUser)
    
    # admin.Controller.showEmployee(dataUser.items)
    currentUser = auth.controller.authSection(dataUser)
    Dashboard.mainMenu(currentUser, dataUser=dataUser)
    # admin.Controller.showSupllier(dataUser.items)
    #todo nanti lanjutin aja
# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana