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
    addrs = re.findall('@\S+', contents)
    print(len(addrs))

#pt3-using a dictionary
    popular_domains = {}
    #add emails to the dictionary
    for addr in addrs:
        popular_domains[addr] = popular_domains.get(addr, 0) + 1
    list_popular_domains = (popular_domains.items())
    #lambda denotes the start of an Inline function.
    decending_popular_domains = sorted(list_popular_domains, reverse=True, key=lambda email_pair: email_pair[1])
    print(decending_popular_domains)
    
