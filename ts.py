import platform
import os
import sys
import re

def HelperMethods():
    dirPath = os.getcwd()
    print("Current directory is: " + dirPath)
    folderName = os.path.basename(dirPath)
    print ('DirectoryName is' + folderName)
    print(platform.python_version())

#HelperMethods()
#print(os.listdir('./roza tel'))
#print ([x[0] for x in os.walk(".")])

def parseFileName(filenName):
    dotPosition = filenName.find('.')
    return filenName[:dotPosition]

def extractTelFromVFSContent(content):

    return re.search(r'.?\d{3,10}', content).group()

f= open("rozaTel.txt","w+")
tmp = 'str'
list = os.listdir('./roza tel')
print (list)
for i in list:
    tmp = open('./roza tel/' + i, "r")
    
    f.write(parseFileName(i)+' Tel:' + extractTelFromVFSContent(tmp.read()) + '\n')
    tmp.close()
f.close()