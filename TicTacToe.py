import pickle

#savegame = open("savegame.txt", "w+")

def Entry():
    print("Welcome to Tic Tac Toe.\n" + "------------------------\n" + "Select one option below:\n\n" + "Begin - start a new game\n" + "Open - restart a prior game\n")
    NewGameStr = str(input("Enter option > "))
    if (NewGameStr == "Begin" or NewGameStr == "begin" ):
        NewGame = 1
    elif (NewGameStr == "Open" or NewGameStr == "open"):
        NewGame = 0
    return NewGame

def Exit():
    print("Select one option below:\n\n" + "Save - save and quit current game\n" + "Quit - quit current game without saving\n")
    ExitStr = str(input("Enter option > "))
    if (ExitStr == "Save" or ExitStr == "save"):
        Exit = 1
    elif (ExitStr == "Quit" or ExitStr == "quit"):
        Exit = 0
    return Exit

def Save(Data, Filename):
    with open(Filename, "wb") as f:
        pickle.dump(Data, f)

def Read(Filename):
    with open(Filename, "rb") as f:
        Temp = pickle.load(f)
        return Temp

def MakeVisTable():
    VisTable = "1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9"
    print("\n" + VisTable)

def InitGameTable():
    Columns = 3
    Rows = 3

    GameTable = [["-" for i in range(Columns)] for j in range(Rows)]
    return GameTable

def PrintTable(GameTable):
    for Rows in GameTable:
        print(" | ".join(map(str, Rows)))

def MainGame(NewGame, GameTable):
    CurrentPlayer = 0 # (0 = X, 1 = O)
    Winner = 0

    if (NewGame == 1):  #FOR DEBUG
        print("Starting Game\n")
    elif (NewGame == 0):
        print("Opening save\n")

    InitGameTable()

    if (NewGame == 0):
        GameTable = Read("savegame.txt")

    while(Winner == 0):
        PrintTable(GameTable)

        MakeVisTable()

        if (CurrentPlayer == 0):
            print("The current player is X\n")
        elif (CurrentPlayer == 1):
            print("The current player is O\n")
        CurrentLoc = int(input("Enter location > "))
# This is retarded please fix this shit also smth is broken noew :(
        if (CurrentPlayer == 0):  # Player X
            if (CurrentLoc == 1 and GameTable[0][0] == "-" or GameTable[0][0] != "O"):
                GameTable[0][0] = "X"
            elif (CurrentLoc == 2):
                GameTable[0][1] = "X"
            elif (CurrentLoc == 3):
                GameTable[0][2] = "X"
            elif (CurrentLoc == 4):
                GameTable[1][0] = "X"
            elif (CurrentLoc == 5):
                GameTable[1][1] = "X"
            elif (CurrentLoc == 6):
                GameTable[1][2] = "X"
            elif (CurrentLoc == 7):
                GameTable[2][0] = "X"
            elif (CurrentLoc == 8):
                GameTable[2][1] = "X"
            elif (CurrentLoc == 9):
                GameTable[2][2] = "X"
            else: print("You may not choose this location")

        if (CurrentPlayer == 1):  # Player O
            if (CurrentLoc == 1):
                GameTable[0][0] = "O"
            elif (CurrentLoc == 2):
                GameTable[0][1] = "O"
            elif (CurrentLoc == 3):
                GameTable[0][2] = "O"
            elif (CurrentLoc == 4):
                GameTable[1][0] = "O"
            elif (CurrentLoc == 5):
                GameTable[1][1] = "O"
            elif (CurrentLoc == 6):
                GameTable[1][2] = "O"
            elif (CurrentLoc == 7):
                GameTable[2][0] = "O"
            elif (CurrentLoc == 8):
                GameTable[2][1] = "O"
            elif (CurrentLoc == 9):
                GameTable[2][2] = "O"

        PrintTable(GameTable)

        if (CurrentPlayer == 0):
            CurrentPlayer = 1
        elif (CurrentPlayer == 1):
            CurrentPlayer = 0

        input("Press ENTER to continue")
        Save(GameTable, "savegame.txt")
        #GameTable = Read("savegame.txt") #for debug

        #PrintTable(GameTable)
    Exit()


MainGame(Entry(), InitGameTable())
