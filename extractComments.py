import sys
from bs4 import BeautifulSoup #imported from miniconda

fileHtml = sys.argv[1]
#open file and read from it
with open(fileHtml, "r", encoding="utf-8") as fileRead:
    html = fileRead.read()

parse = BeautifulSoup(html,'html.parser')

#open comment.txt and write to it
with open("comments.txt", "w", encoding="utf-8") as file:
    #find all <blockquote> and remove <p> tags from them
    for blockTag in parse.find_all('blockquote'):
        pTagBlock = blockTag.find_all('p')
        for pTagQ in pTagBlock:
            pTagQ.extract()
    #find the <div> tags with data-type="comment"
    for divData in parse.select('div[data-type="comment"]'):
        divClass = divData.select_one('div[class="md"]') #selects one <div class="md"> 
        if divClass: #if there
            pTags = divClass.find_all('p') #finds all pTags in that divTag
            for pTagDiv in pTags: #goes through all the <p> tags
                file.write(pTagDiv.text + '\n') 
            