#This file has the URL passed into the function retreieveURL() from run.py 
#The text file, URL.txt, is then accessed from the Data/raw path stored in getTxt and then the file is 
#opened using the open() function. It is now able to be written to and is stored in the outputFile varaible
#From there the code calls upon request.get(url) which retrieves the data content from the URL and is stored in getURL
#The outputFile then has the getURL data write lines of html text to the the outputFile
#The URL.txt file is now full of html data from the link provided. The file is then closed. 
#retrieveURL() is a void function

import requests #imported from miniconda
import sys #included in STD library
getTxt = 'CS325_p4/Data/raw/URL.txt'

def retrieveURL(url):
    outputFile = open(getTxt,"w",encoding="utf-8")

    getURL=requests.get(url)

    outputFile.writelines(getURL.text)
    outputFile.close()
