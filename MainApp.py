from src import Manager, Config, Controller, Dashboard
# nanti cara make modul nya gini 
# <Controller/Schema>.<tipe>.<func/class>

if __name__ == "__main__":
    dataUser = Manager.UserManager(Config.dataUser)
    currentUser = Controller.Auth.authSection(dataUser)
    Dashboard.mainMenu(currentUser, dataUser)
    
# Nanti kalo ad ayg mau benerin, benerin ae
# gua masih bingung mau mulai bikin darimana