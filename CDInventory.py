#-------------------------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Modifying CDInventory.py to replace inner data structure by dictionaires,
#add ability to load existing data, and ability to delete an entry
# Change Log:
# Rgoding, 8/9/2020, Created File
#Rgoding, 8/10/2020, Added ability to load existing data
#Rgoding, 8/11/2020, Added Ability to delete an requested entry, modified display
#choice to work with dictionary objects
#-------------------------------------------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
lstRow = []


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        for row in objFile:
            #Take each row and strip it of \n and seperate items by a comma
            lstRow = row.strip().split(',')
            #Take info from txt file and load it as dic object
            dicRow = {'id': lstRow[0], 'Title': lstRow[1], 'Artist': lstRow[2]}
            #append dicrow to list of dictionaries
            lstTbl.append(dicRow)
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        #Create dictionary object of input variables
        dicRow = {'id': intID, 'Title': strTitle, 'Artist': strArtist}
        #append to table of dictionaries
        lstTbl.append(dicRow)
        print()

        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',')
    elif strChoice == 'd':
       delEntry = int(input('Please Enter ID of CD you would like to delete: '))
       #create for loop to cycle through lstTbl to find requested entry to delete
       for row in lstTbl:
           if delEntry in row.values():
               lstTbl.remove(row)
               print('CD id: ' + str(delEntry) + ' has been deleted')
               print()
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')  
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

