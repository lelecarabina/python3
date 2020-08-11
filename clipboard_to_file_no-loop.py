import sys
import os.path
import pyperclip
from datetime import datetime

try:
    t = datetime.now() # catch sate and time
    tformatted = t.strftime("%m/%d/%Y, %H:%M:%S") #format date/time string
    print(tformatted + '\nCopying text...') # Feedback
    save_path = '/Users/Lel/Dropbox/LeDesignPro/Leticia/Texts' #path to generated file
    file = os.path.join(save_path, 'le_python_clipboard.txt') #generated file's name    
    f= open(file, 'a') #open file for appending
    text = pyperclip.paste() # catch clipboard content
    print('> "' + text + '"\n') #Feedback
    f.write(tformatted + '\n' + text + '\n\n') #write  clipboard content to file
    f.close() #close file
    print('Copy completed!\n---') #Feedback
    sys.exit(0) #end python program

except Exception as error: #catch error
    print(error) #print error
