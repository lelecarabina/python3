import sys
import os.path
import pyperclip
from datetime import datetime

try:
    x = 0
    t = datetime.now()
    tformatted = t.strftime("%m/%d/%Y, %H:%M:%S")
    print(tformatted + '\nCopying text...[' + str(x) + ']') # Feedback
    save_path = '/Users/Lel/Dropbox/LeDesignPro/Leticia/Texts'
    file = os.path.join(save_path, 'le_python_clipboard.txt')     
    f= open(file, 'a')
    text = pyperclip.paste() # content of clipboard
    print('> "' + text + '"\n') #Feedback
    f.write(tformatted + '\n' + text + '\n\n')
    f.close()
    print('Copy completed!\n---') #Feedback
    sys.exit(0)

except Exception as error:
    print(error)
