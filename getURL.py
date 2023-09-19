import requests #imported from miniconda
import sys #included in STD library

outputFile = open("URL.txt","w")
url = sys.argv[1]

getURL=requests.get(url)

outputFile.writelines(getURL.text)
outputFile.close()