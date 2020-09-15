#Extracts email addresses from a text file
#pt-1 prints number of email addresses with softwire.com domain

#open the file
#read the contents line by line
#check for the substring '@softwire.com'

import re
with open('sample.txt') as f:
    count = 0
    contents = f.read()
    for i in range(len(contents)):
        if (contents[i: i + 13] == '@softwire.com'):
            count = count + 1
    print(count)

    #pt-2 using regex to find all email addresses:
    x = re.findall('@\S+', contents)
    print(len(x))
