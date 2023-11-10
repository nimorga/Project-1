from module_1 import getURL
from module_2 import openFileRead
from module_3 import extractComments
from module_4 import openAI
commentTXT = 'CS325_p4/Data/processed/comments.txt'

def main():
    #inputURL = getURL.sys.argv[1]
    #getURL.retrieveURL(inputURL)
    extractComments.goComment(commentTXT)
    openAI.runAI()
main()