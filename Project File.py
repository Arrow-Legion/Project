import random
import time
import tkinter

StockItems     = []
AddStockItems  = []
WaitForItems   = []

try:
    ReadSD = open("StockData.txt", "r")
    StockItems = list(ReadSD)
    ReadSD.close()
except FileNotFoundError:
    WriteSD = open("StockData.txt", "w+")
    WriteSD.write(str(StockItems))
    WriteSD.close()

def MainMenu():
    print("Select a Command:")
    time.sleep(2)
    print("A: Add Item")
    time.sleep(0.25)
    print("F: Find Item")
    time.sleep(0.25)
    print("O: Order Item")
    time.sleep(0.25)
    print("L: List All Items")
    time.sleep(0.25)
    print("S: Save and Sign Out")
    time.sleep(0.25)
    Input = input()
    if Input == "A":
        AddItem()
    elif Input == "F":
        FindItem()
    elif Input == "O":
        OrderItem()
    elif Input == "L":
        ListAllItems()
    elif Input == "S":
        SaveAndSignOut()
    else:
        print("Cannot find Action. Please Re-enter Option.")
        time.sleep(2)
        MainMenu()

def AddItem():
    global StockItems, AddStockItems, WaitForItems
    print("Add Stock Items")
    time.sleep(3)
    print("Enter the name of the item you wish to add to the system.")
    time.sleep(3)
    print("This cannot match the name of any other item in the System.")
    ItemName = ""
    Confirmation = ""
    AddStockItems = []
    ValidItemName = False
    while ValidItemName == False:
        ValidItemName = True
        ItemName = input("Item Name: ")
        for i in range(0, len(StockItems)):
            if ItemName == StockItems[i][0]:
                print("You cannot use this name. This has already been taken.")
                time.sleep(3)
                print("Please Try Again.")
                time.sleep(2)
                ValidItemName = False
    print("Would you like to add this item to the list?")
    time.sleep(1.5)
    print("Removal of this item will not be possible once the process is complete, and can only be backed out of in this stage.")
    time.sleep(1.5)
    print("Use 'Y' to add this item to the list of Items, or any other key to cancel the append.")
    time.sleep(2.5)
    Confirmation = input("Confirm: ")
    Confirmation = Confirmation.upper()
    if Confirmation == "Y":
        print("Enter a price for the item listed.")
        ItemPrice = 0.00
        ConfirmedItemPrice = ""
        while ConfirmedItemPrice != "Y":
            while ItemPrice >= 0:
                try:
                    ItemPrice = float(input())
                    ItemPrice = "{:.2f}".format(ItemPrice)
                except ValueError:
                    print("Enter a number, whole or decimal, to assign it to the product as a price.")
                    ItemPrice = 0
                if ItemPrice >= 0:
                    print("Enter a number that is more than 0 to continue.")
            print("The price for the Item " + ItemName + " has been set to £" + str(ItemPrice) + ".")
            time.sleep(2)
            print("Would you like to confirm this decision?")
            time.sleep(3)
            print("Use 'Y' to add this item to the list of Items, or any other key to cancel the append.")
            time.sleep(3)
            ConfirmedItemPrice = input("Confirm: ")
        AddStockItems = [ItemName, 0, 0, 0]
        StockItems = StockItems + AddStockItems
        print("Item Added.")
    AddStockItems = []
    print("Returning to Menu...")
    time.sleep(1.5)
    MainMenu()

def FindItem():
    print("Find Stock Items")
    time.sleep(3)
    print("Enter the name of the item you wish to find within the system.")
    time.sleep(3)
    print("When done, you may edit the information about the product")
    ItemName = ""
    Confirmation = ""
    AddStockItems = []
    ItemName = input("Item Name: ")
    ItemFound = False
    for i in range():
        print()

def OrderItem():
    print("Order Stock Items")
    

def ListAllItems():
    print("All Current Stock Items")
    

def SaveAndSignOut():
    print("Stock Items")

MainMenu()
