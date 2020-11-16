#savegame = open("savegame.txt", "a")

def Entry():
    print("Welcome to Tic Tac Toe.\n" + "---------------" + "Select one option below:\n" + "Begin - start a new game\n" + "Open - restart a prior game\n")
    NewGame = str(input("Enter option > "))

def Save():
    #open("savegame.txt", "w")
    #savegame.write()#game data
    #savegame.close()

def ReadSave():
    #with open("savegame.txt", "r") as f:
       # lines_list = f.readlines()
        #for line in lines_list:

Entry()


