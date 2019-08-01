# CECS 378                                  Spring 2019                                  Lab 2 - Malware

# Name: Thanh Le
# Student ID: 015809792
# Start Date: 3-13-2019
# End Date: 3-27-2019

# -------------------------------------------------------------------------------------------------------
# Hacking attributes' values of characters in Ultima V
# -------------------------------------------------------------------------------------------------------

def main():
    mainMenu(readData())
    

# Interactive menu with options of changing character stats and items
def mainMenu(data):
    print("========================= Welcome to Ultima 5 Hack =========================")
    
    while True:
        print("\nWhat would you like to alter?")
        print("1. Character Stats")
        print("2. Items")

        choice = input("Please enter 1 or 2 to confirm your choice: ")
        
        while(choice != "1" and choice != "2"):
            print("Your choice is invalid")
            choice = input("Please enter 1 or 2 to confirm your choice: ")
        
        if choice == "1":
            editStat(data)
        elif choice == "2":
            editItem(data)
        
        print("\n---------------------------------------------------------------------------------------")
        answer = input("Do you want to continue modifying the game? Please enter 'Y' for Yes and 'N' for No: ").lower()
        if answer == 'n':
            break
    
    print("\n================= Thank you for using Ultima 3 Hack! Enjoy your game! ================")

    
# Read the binary bytes from file and store it in data list
def readData():
    file = open("Ultima_5/SAVED.GAM", "rb")
    data = list(bytearray(file.read()))
    file.close()
    return data


# Write the data back to the file
def writeData(data):
    file = open("Ultima_5/SAVED.GAM", "wb")
    file.write(bytearray(data))
    print("\nCHANGE WAS SUCCESSFULLY SAVED!")
    print("\n---------------------------------------------------------------------------------------")
    file.close()
    

# Alter the character stats
def editStat(data):
    character = select("character", False)
    while True:
        stat = select("stat", False)
        value = select(stat, True)
        
        sOffset = characters[character] + stats[stat]
        replaceByte(data, value, sOffset)
        
        answer = input("Do you want to change another Stat of " + character + "? Please enter 'Y' for Yes and 'N' for No: ").lower()
        if answer == 'n':
            break
       
        
# After the item values
def editItem(data):
    while True:
        item = select("item", False)
        value = select(item, True)
        iOffset = items[item]
        
        replaceByte(data, value, iOffset)
        
        answer = input("Do you want to change another Item value? Please enter 'Y' for Yes and 'N' for No: ").lower()
        if answer == 'n':
            break
    
    
# Allow user to select characters, stats, and items to be altered
def select(selection, isValue):
    if isValue:
        if selection in list(maxStats.keys()):
            maxValue = maxStats[selection]
        else:
            maxValue = maxItems[selection]
        choice = int(input("Please enter value from 0 to " + str(maxValue) + " for the " + selection + ": "))
        
    else:
        if selection == "character":
            List = list(characters.keys())
        elif selection == "stat":
            List = list(stats.keys())
        elif selection == "item":
            List = list(items.keys())
        
        print("\n---------------------------------------------------------------------------------------")
        for i in range(len(List)):
            print(i+1, "-", List[i])
            
        choice = int(input("Please select the " + selection.upper() + " to be edited: "))
    
    while True:
        if isValue:
            if choice >= 0 and choice <= maxValue:
                return choice
        else:
            if choice >= 1 and choice <= len(List):
                return List[choice - 1]
            
        choice = int(input("Your choice is invalid!\nPlease enter your choice again: "))
      
        
# Replace the byte in data list at the offset with the value
def replaceByte(data, value, offset):
    bArray = list(value.to_bytes(2, byteorder = "little"))
    if value > 255:
        data[offset] = bArray[0]
        data[offset + 1] = bArray[1]
    else:
        data[offset] = bArray[0]
    writeData(data)
        

# -------------------------------------------------------------------------------------------------------------------------
characters =    {"PLAYER": int('0x02', 16),   "Shamino":   int('0x22', 16),    "Iolo":    int('0x42', 16),
                 "Mariah": int('0x62', 16),    "Geoffrey": int('0x82', 16),    "Jaana":   int('0xA2', 16),
                 "Julia":  int('0xC2', 16),    "Dupre":    int('0xE2', 16),    "Katrina": int('0x102',16),
                 "Sentri": int('0x122',16),    "Gwenno":   int('0x142',16),    "Johne":   int('0x162',16),
                 "Gorn":   int('0x182',16),    "Maxwell":  int('0x1A2',16),    "Toshi":   int('0x1C2',16),
                 "Saduj":  int('0x1E2',16)
                }



stats =         {"Str":   int('0x0C', 16),    "Int":    int('0xE',   16),    "Dex": int('0x0D', 16),
                 "HP":    int('0x10', 16),    "Max HP": int('0x12', 16),     "Exp": int('0x14', 16),
                 "Magic": int('0x0F', 16)
                }


maxStats =      {"Str":   255,      "Int":    255,      "Dex": 255,
                 "HP":    65535,    "Max HP": 65535,    "Exp": 65535,
                 "Magic": 255
                }


items =         {"Gold":      int('0x204', 16),     "Key":         int('0x206', 16),    "Skull Key":    int('0x20B', 16),
                 "Gem":       int('0x207', 16),     "Black Badge": int('0x218', 16),    "Magic Carpet": int('0x20A', 16),
                 "Magic Axe": int('0x240', 16)
                }

maxItems =      {"Gold":      65535,    "Key":         255,    "Skull Key":   255,
                 "Gem":       255,      "Black Badge": 255,    "Magic Carpet": 255,
                 "Magic Axe": 255
                }

main()