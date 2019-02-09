# Author: Nathan Lietha
# Purpose: Builds C# lists for GEOD wage calculator
# URL: https://apps.sd.gov/ge102wagecalculator/Index
# Version: 1.0
# Build Date: 2018.05.16
# Last Modified: 2018.05.16

def makeTable(line):
    print("private static List<%s> %s = new List<%s>\n{" % (tableItem, TableName, tableItem))
    i = 2
    for loop in range(len(line)-2):
        
        lineModify(line[i], i)
        i += 1
    print("};\n")

# prints item string
def lineModify(line, counter):
    print("    new %s() { "%(tableItem), end="")
    DecFlag = False
    StringFlag = False
    lineList = line.split('\t')
    for item in range(len(lineList)):
        currentPart = lineList[item]
        currentPart = currentPart.replace(" ", "")

        if(currentPart.find(',') != -1):
            retValue = currentPart.replace(',', "")        
        elif(currentPart.isalpha()):
            retValue = "\"" + currentPart + "\""
        elif(currentPart.find('%') != -1):
            tempRate = currentPart.replace("%", "")
            tempRate = float(tempRate)
            retValue = tempRate / 100

        elif(currentPart.find('-') != -1):
            retValue = '0'
        elif(currentPart.find("Over") != -1):
            retValue = '0'

        else:
            retValue = currentPart

        if(currentPart.find('.') != -1):
            DecFlag = True 

        if DecFlag:
            retValue = "(decimal)%s" % retValue
            DecFlag = False            


        if item == (len(lineList)-1):
           print("%s = %s " % (categories[item], retValue), end=" ")
        else:
            print("%s = %s, " % (categories[item], retValue), end=" ")
    if counter != (LineNumbers-1):
        print("},")
    else:
        print("}")

def ListOfLists(Name, categories):
    # print(categories)
    print("public class %s\n{" % Name)
    counter = 0
    for cat in range(len(categories)):
        #Type = findType()

        #print("    public %s %s;" % (Type, categories[cat]))
        counter += 1
    print("}\n")

def findType(Section):
    #decimal
    if Section.isalnum():
        return "decimal"
    #string

    #bool


def TableSearch(TableName, tableItem):
    print("%s selected = null;" % (tableItem))
    print("foreach (%s index in %s)\n{"% (tableItem, TableName))
    print("    if (/*enterItem*/ <= index.Ending || index.Ending == 0)\n    {")
    print("        selected = index;\n        break;\n    }\n}")

def GetTableName(name):
    tmp = name.replace(" ", "")
    tmp = tmp.replace('\t', "")
    return tmp

def FindDoc():
    # look for directory StateTables
    # Loop though .txt files in directory, append ouput into CompinedTables.txt
    



print("Enter Full Bracket, Ctrl+d to print table")
# get user input
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

# Get table name, Add item to end
TableName = GetTableName(contents[0])
tableItem = TableName + "Item"

# retrive categories, Remove spaces
categories = contents[1].split('\t')
for i in range(len(categories)):
    categories[i] = categories[i].replace(" ", "")

# Make Table
LineNumbers = len(contents)
makeTable(contents)

# Generate list of Variables
ListOfLists(tableItem, categories)
TableSearch(TableName, tableItem)
