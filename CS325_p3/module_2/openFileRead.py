#This file imports BeautifulSoup to be used for extracting comments in extractComments.py
#This file provides both paths of the text files
#This file's openRead() funtion opens the URL.txt, from the data path given in the getTxt string, to read the file 
#contents and store it in a html variable
#The openRead() function returns the html varaible that is then called later in extractComments.py
#The getFile() funtion returns the the comments.txt path to the run.py file

from bs4 import BeautifulSoup #imported from miniconda
getCommentTxt ='Data/processed/comments.txt'
getTxt = 'Data/raw/URL.txt'
def openRead():
    with open(getTxt, "r", encoding="utf-8") as fileRead:
        html = fileRead.read()
        return html     
def getFile():
    return getCommentTxt    