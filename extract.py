inputPath="./input.txt" #add your input file path
outputPath="./output.txt" #add your output text file path


inputFile=open(inputPath,'r')
data=inputFile.readlines()
inputFile.close()


def uniqueData(data):
    uniqueList=[]
    for word in data:
        if word not in uniqueList:
            uniqueList.append(word)
    return uniqueList

def ifSpecialChar(word):
    lst=[",","۔","؟","‘","’","/","\\","'","،","(",")"]
    for chr in lst:
        if chr in word:
            return False
    return True

def ifNumber(word):
    lst=["۰","۱","۲","۳","۴","۵","۶","۷","۹","0","1","2","3","4","5","6","7","8","9"] #list of numbers
    for chr in lst:
        if chr in word:
            return False
    return True


collection=list()
for line in data:
    for word in line.split():
        if ifSpecialChar(word) and ifNumber(word):
            collection.append(word)




print(len(collection))
collection=uniqueData(collection)
print(len(collection))
outputFile = open(outputPath,'w')
for word in collection:
    outputFile.write(word+"\n")
outputFile.close()
print(collection)