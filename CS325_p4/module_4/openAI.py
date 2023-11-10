#This file imports openai to connect to openAI API in order to send an API prompt
#It has a function that uses 50 comments from comments.txt and puts each separate comment into an ai call
#to determine the sentiment.

import time
from openai import OpenAI

client = OpenAI(
    api_key="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",
)

ResultsFile = 'CS325_p4/Data/Sentiments/resultsFile.txt'
Comments_File = 'CS325_p4/Data/processed/comments.txt'

def runAI():
    maxComments = 3
    commentsGoThru = 0
    
    with open(Comments_File, 'r', encoding='utf-8') as context, open(ResultsFile, 'w') as resultsFile:
        comment = []
        for line in context:
            line = line.strip() #remove white spaces
            if line:  
                comment.append(line) #joins comment to list
            else:
                if comment: 
                    commentText = ' '.join(comment) #join comment into string
                    
                    chat_completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", 
                            "content": "What is the sentiment of the comment: " + commentText + " Only answer the question with positive or negative. If you are not sure, say I don't know."}
                        ]
                    )
                
                    result = chat_completion.choices[0].message.content
                    resultsFile.write(result +'\n')
                    commentsGoThru += 1
                    if commentsGoThru>= maxComments:
                        break
              
                    time.sleep(20)
                    comment = []