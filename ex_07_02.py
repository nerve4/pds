'''
7.2 Write a program that prompts for a file name, then opens that 
file and reads through the file, looking for lines of the form: 

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each of 
the lines and compute the average of those values and produce an 
output as shown below. Do not use the sum() function or a 
variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

lncount = 0
fncount = 0
lps_total = 0.0

for line in fh:
    lncount=lncount + 1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    fncount=fncount + 1
    # Find the first "empty" record in the line
    fts=line.find(' ')
    wline=len(line)
    # Check the first-last postion
    lps=line[fts:wline+1]
    lps_rs=lps.rstrip()
    # Use float on strip reult
    lps_flt=float(lps_rs)
    lps_total=lps_total+lps_flt

avg=lps_total/fncount

print("Average spam confidence:",avg)