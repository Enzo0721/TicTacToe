import os
import ast

SaveFile = 'ticsavegame.txt' # Save Game document/location (in this case it is the same location as the main script)

def CreateSaveGame():
    if not os.path.exists(SaveFile): # If savegame is not made; create it
        open(SaveFile, 'w') # create file

def Entry():
    Clear()
    print("Welcome to Tic Tac Toe.\n" + "------------------------\n" + "Select one option below:\n\n" + "Begin - start a new game\n" + "Open - restart a prior game\n")
    NewGameStr = str(input("Enter option > "))
    if (NewGameStr == "Begin" or NewGameStr == "begin"):
        NewGame = 1
    elif (NewGameStr == "Open" or NewGameStr == "open"):
        NewGame = 0
    return NewGame

def Exit():
    print("\nSelect one option below:\n\n" + "Continue - continue new game\n" + "Quit - quit current game\n")
    ExitStr = str(input("Enter option > "))
    if (ExitStr == "Continue" or ExitStr == "continue"):
        Exit = 1
        MainGame(Entry(), InitGameTable())
    elif (ExitStr == "Quit" or ExitStr == "quit"):
        Exit = 0
        exit()
    return Exit

def Clear():
    os.system("cls")

def Save(Data, Filename):
    f = open(Filename, "w") #open file for write
    temp = ','.join(map(str, Data)) # turns 2d array into string
    f.write(temp) # writes string to savegame
    f.close() # close file

def Read(Filename):
    with open(Filename, 'r') as f: #open file for reading
        temp = f.read() #read string from savegame
        out2 = ast.literal_eval(temp) #parse data into (in this case) 2dArray
        #print(out2[0] + out2[1] + out2[2])
        f.close() # close file
        return out2 #return so it can be used outside this function

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

def CheckRow(GameTable):
    RowDone = 0
    if (GameTable[0][0] == GameTable[0][1] == GameTable[0][2] != "-"):
        RowDone = 1
    elif (GameTable[1][0] == GameTable[1][1] == GameTable[1][2] != "-"):
        RowDone = 1
    elif (GameTable[2][0] == GameTable[2][1] == GameTable[2][2] != "-"):
        RowDone = 1
    return RowDone

def CheckColumn(GameTable):
    ColumnDone = 0
    if (GameTable[0][0] == GameTable[1][0] == GameTable[2][0] != "-"):
        ColumnDone = 1
    elif (GameTable[0][1] == GameTable[1][1] == GameTable[2][1] != "-"):
        ColumnDone = 1
    elif (GameTable[0][2] == GameTable[1][2] == GameTable[2][2] != "-"):
        ColumnDone = 1
    return ColumnDone

def CheckDiag(GameTable):
    DiagDone = 0
    if (GameTable[0][0] == GameTable[1][1] == GameTable [2][2] != "-"):
        DiagDone = 1
    elif (GameTable[0][2] == GameTable[1][1] == GameTable[2][0] != "-"):
        DiagDone = 1
    return DiagDone

def CheckWinner(GameTable):
    GameWinner = 0

    if (CheckRow(GameTable) == 1):
        GameWinner = 1
    elif (CheckColumn(GameTable) == 1):
        GameWinner = 1
    elif (CheckDiag(GameTable) == 1):
        GameWinner = 1
    return GameWinner

def MainGame(NewGame, GameTable):
    CurrentPlayer = 0 # (0 = X, 1 = O)
    Winner = 0

    CreateSaveGame()

    if (NewGame == 1):  #FOR DEBUG
        print("Starting Game\n")
    elif (NewGame == 0):
        print("Opening save\n")

    Clear()

    InitGameTable()

    if (NewGame == 0):
        GameTable = Read(SaveFile)


    while(Winner == 0):
        PrintTable(GameTable)

        MakeVisTable()

        if (CurrentPlayer == 0):
            print("The current player is X\n")
        elif (CurrentPlayer == 1):
            print("The current player is O\n")
        CurrentLoc = int(input("Enter location > "))
# This is stupid please fix
        if (CurrentPlayer == 0):  # Player X
            if (CurrentLoc == 1 and GameTable[0][0] == "-"):
                GameTable[0][0] = "X"
            elif (CurrentLoc == 2 and GameTable[0][1] == "-"):
                GameTable[0][1] = "X"
            elif (CurrentLoc == 3 and GameTable[0][2] == "-"):
                GameTable[0][2] = "X"
            elif (CurrentLoc == 4 and GameTable[1][0] == "-"):
                GameTable[1][0] = "X"
            elif (CurrentLoc == 5 and GameTable[1][1] == "-"):
                GameTable[1][1] = "X"
            elif (CurrentLoc == 6 and GameTable[1][2] == "-"):
                GameTable[1][2] = "X"
            elif (CurrentLoc == 7 and GameTable[2][0] == "-"):
                GameTable[2][0] = "X"
            elif (CurrentLoc == 8 and GameTable[2][1] == "-"):
                GameTable[2][1] = "X"
            elif (CurrentLoc == 9 and GameTable[2][2] == "-"):
                GameTable[2][2] = "X"
            else:
                print("You may not choose this location")

        if (CurrentPlayer == 1):  # Player O
            if (CurrentLoc == 1 and GameTable[0][0] == "-"):
                GameTable[0][0] = "O"
            elif (CurrentLoc == 2 and GameTable[0][1] == "-"):
                GameTable[0][1] = "O"
            elif (CurrentLoc == 3 and GameTable[0][2] == "-"):
                GameTable[0][2] = "O"
            elif (CurrentLoc == 4 and GameTable[1][0] == "-"):
                GameTable[1][0] = "O"
            elif (CurrentLoc == 5 and GameTable[1][1] == "-"):
                GameTable[1][1] = "O"
            elif (CurrentLoc == 6 and GameTable[1][2] == "-"):
                GameTable[1][2] = "O"
            elif (CurrentLoc == 7 and GameTable[2][0] == "-"):
                GameTable[2][0] = "O"
            elif (CurrentLoc == 8 and GameTable[2][1] == "-"):
                GameTable[2][1] = "O"
            elif (CurrentLoc == 9 and GameTable[2][2] == "-"):
                GameTable[2][2] = "O"
            else:
                print("You may not choose this location")

        #PrintTable(GameTable) #for debug

        if (CurrentPlayer == 0):
            CurrentPlayer = 1
        elif (CurrentPlayer == 1):
            CurrentPlayer = 0

        Save(GameTable, SaveFile)

        if (CheckWinner(GameTable) == 1):
            print("GAME OVER")
            input("Press ENTER to continue")  # for debug
            Exit()

        #PrintTable(GameTable)
        #input("Press ENTER to continue")# deez nuts

        Clear()


MainGame(Entry(), InitGameTable())
