#author @talhakeskin
import random
spChList=['/','@','$','%','&','#','(',')','+','-','!']

password = str()


print("Generate Password\n_________________\n")
print("Types:\n1 - Numbers\n2 - Lowercase Characters\n3 - Uppercase Characters\n4 - Special Characters\nUsage: 1,2,3,4\n")

cleanSelection = list()
selectionList = list()
password = str()

def deleteReplicates(selectionList):
    cleanList = list()
    for i in range(0,len(selectionList)):
        if selectionList[i] in cleanList:
            continue #ignore if it has replicates
        else:
            cleanList.append(selectionList[i])
    return cleanList
    

while(True):
    passType = input("Enter your choice => ")
    passType = passType.split(',')

    for i in range(0,len(passType)):
        if(passType[i]!='1' and passType[i]!='2' and passType[i]!='3' and passType[i]!='4'):
            continue #ignore
        else:
            cleanSelection = passType[i]
            cleanSelection = cleanSelection.strip()
            cleanSelection = cleanSelection.replace(' ','')
            selectionList.append(cleanSelection)

    passType.clear()
    selectionList = deleteReplicates(selectionList)
    if(len(selectionList) < 1):
        print("At least one selection required!")
        continue
    else:
        passLength = int(input("Length of the password => "))
        for i in range(0,passLength):
            randNum = selectionList[int(random.random()*len(selectionList))]
            #print(randNum) #test
            if(int(randNum) == 1):
                password = password + chr(int((random.random()*10) + 48)) #10 ascii values 0-9 // random between (0-9 + 48)
            elif(int(randNum) == 2):
                password = password + chr(int((random.random()*26) + 97)) #25 ascii values a-z // random between (0-24 + 97)
            elif(int(randNum) == 3):
                password = password + chr(int((random.random()*26) + 65)) #25 ascii values A-Z // random between (0-24 + 65)
            elif(int(randNum) == 4): #special characters that are defined above.
                password = password + (spChList[int(random.random()*len(spChList))])
            else:
                continue

        print("Your generated password is = ",password)
        break
