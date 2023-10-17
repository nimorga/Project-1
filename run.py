#This file calls all of the module folders created and imports each of their .py files
#It has a main function that gets the URL from the terminal and stores it in inputURL (using getURL.py import of sys)
#That inputURL is then passed as a parameter into the function retrieveURL() located in the getURL.py file
#It executes all the work in that function not returning anything back to main
#Then the function goComment is called from extractComments.py that has a parameter that calls another function located in
#openFileRead.py the getFile() function returns the comment.txt file path to main
#Then goComments() is executed not returning anything to main
#The main() function is called and exectues these functions within it 
#main() is a void function

from module_1 import getURL
from module_2 import openFileRead
from module_3 import extractComments
def main():
    inputURL = getURL.sys.argv[1]
    getURL.retrieveURL(inputURL)
    extractComments.goComment(openFileRead.getFile())
main()