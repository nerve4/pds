'''
10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by 
finding the time and then splitting the string a 
second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

tm_hist=dict()
count = 0

for line in handle:
    if line == '':
        continue
    if 'From ' in line:
        words=line.split()
        #print(words)
        tm=words[5][:2]
        #print(tm)
        tm_hist[tm]=tm_hist.get(tm,0)+1
        
        count = count +1
#print(tm_hist)
tm_list=list()
for h,c in tm_hist.items():
    tm_list.append((h,c))
tm_list.sort()
#print(tm_list)
for k,v in tm_list:
    print(k,v)