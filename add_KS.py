import csv
import os
import sys

def loadData(fileName):
    reader = csv.reader(file(fileName, 'rb'))
    i=0
    allData=[]
    for line in reader:
        i+=1
        if i==1:
            catagory=line
        else:
            allData.append(line)
    return catagory,allData
folder = sys.argv[1]
peopleInforFile = folder + '/congress_people_info.csv'
catagory, allData = loadData(peopleInforFile)
ksScoreDict = {}
for eachdata in allData:
    name = eachdata[0]
    score = eachdata[-1]
    ksScoreDict[name] = score
newFile = open(folder + '/new_non-overlap.csv','w')

originalFile = folder + '/non-overlap.csv'
catagory, allData = loadData(originalFile)
catagory += ['K-S score']
newFile.write(','.join(catagory) + '\n')

for eachData in allData:
    tempname = eachData[0]
    tempScore = 'NaN'
    for key, value in ksScoreDict.iteritems():
        if key in tempname:
            tempScore = value
            break
    newVec = ['"' + tempname + '"'] + eachData[1:None] + [tempScore]
    newFile.write(','.join(newVec) + '\n')

newFile.close()
    
