'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lstWords = list()
for line in handle:
    if(line.startswith('From ')):
        x = line.split(' ')
        lstWords.append(x[1])
    else:
        continue;

dctSender = dict()
for mail in lstWords:
    dctSender[mail] = dctSender.get(mail,0)+1

numCount = 0
mailId = ""
for key,value in dctSender.items():
    if value > numCount:
        numCount = value
        mailId = key

print(mailId, numCount)
