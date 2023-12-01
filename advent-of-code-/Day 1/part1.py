# Pull in the Calibration document
f = open('input.txt', mode = "r")
fileContents = f.read()
rows = fileContents.splitlines()
# Create a list to store the integer values
#intlst = []


# Split the document into lines
#for row in rows:
    # Remove all non-numeric characters
    #digits ="".join(filter(str.isdigit, row))
    #value = int(digits[0]+digits[-1])
    #intlst.append(int(value))    

spowNum = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
finaltotal = 0
for row in rows:
    string = ""
    for letters in rows:
        if letters in spowNum:
            string = string + letters




