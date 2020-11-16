#savegame = open("savegame.txt", "a")

def Entry():
    print("Welcome to Tic Tac Toe.\n" + "------------------------\n" + "Select one option below:\n\n" + "Begin - start a new game\n" + "Open - restart a prior game\n")
    NewGameStr = str(input("Enter option > "))
    if (NewGameStr == "Begin","begin"):
        NewGame = 1
    elif (NewGameStr == "Open", "open"):
        NewGame = 0

#def Save():
    #open("savegame.txt", "w")
    #savegame.write()#game data
    #savegame.close()

#def ReadSave():
    #with open("savegame.txt", "r") as f:
       # lines_list = f.readlines()
        #for line in lines_list:

Entry()


