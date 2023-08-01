name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        # iniom: retrive/create/update counter
        di[w] = di.get(w,0) + 1

largest = -1
theword = None

for k,v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        # Capture/remember the word that was largest
        theword = k

print('Done', theword, largest)