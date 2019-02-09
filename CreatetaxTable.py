
def modify(line, lineNum):
    rawBeg, rawEnd, rawRate, rawMinus = line.split('\t')

    truBag = rawBeg.replace(",", "")
    if rawEnd != "Over":
        truEnd = rawEnd.replace(",", "")
    else:
        truEnd = "0"

    tempRate = rawRate.replace("%", "")
    tempRate = float(tempRate)
    truRate = tempRate / 100

    truMinus = rawMinus.replace(",", "")
    output(truBag, truEnd, truRate, truMinus, lineNum)

def output(beg, end, rate, minus, lineNum):
    if lineNum == 1:
        print("     new TaxBracketItem() { Beginning = %s, Ending = %s, Rate = (decimal)%f, Minus = (decimal)%s }" % (beg, end, rate, minus))
    else:
        print("     new TaxBracketItem() { Beginning = %s, Ending = %s, Rate = (decimal)%f, Minus = (decimal)%s }," % (beg, end, rate, minus))

print("Enter Full Bracket, Ctrl+d to print table")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
print("private static List<TaxBracketItem> TaxBracket = new List<TaxBracketItem>\n{")

for i in range(len(contents)):
    modify(contents[i], (len(contents) - i) )
    
print("};")