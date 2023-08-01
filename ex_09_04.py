'''
9.4 Write a program to read through the mbox-short.txt 
and figure out who has sent the greatest number 
of mail messages. 

The program looks for 'From ' lines and takes the second word of 
those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear 
in the file. After the dictionary is produced, 
the program reads through the dictionary 
using a maximum loop to find the most prolific 
committer.
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ec = dict()

for line in handle:
    if line == '':
        continue
    else:
        line.rstrip()
        if line.startswith('From '):
          wds = line.split()
          ea = wds[1]
          # print(ea)
          ec[ea] = ec.get(ea,0) + 1

mail_value = None
mail_count = None

for e,v in ec.items():
    if mail_value == None or v > mail_count:
        mail_value = e
        mail_count = v

print(mail_value,mail_count)